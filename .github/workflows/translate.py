#!/usr/bin/env python3
"""
Translate markdown files using the translators library.

This script parses markdown to AST using markdown-it-py, translates text nodes with translate_text,
and renders back to markdown using mdformat's built-in renderer.

Dependencies:
    uv pip install translators python-frontmatter markdown-it-py mdformat

Usage:
    uv run translate.py --source-file en/index.md --target-file bn/index.md --source-lang en --target-lang bn --translator google

Example:
    uv run translate.py --source-file en/index.md --target-file bn/index.md --source-lang en --target-lang bn --translator google
"""

import argparse
import sys
import frontmatter
import re
import translators as ts
from markdown_it import MarkdownIt
from mdformat.renderer import MDRenderer

# Compile skip patterns once and reuse
SKIP_PATTERNS = [
    re.compile(r"\{:[^}]*\}"),  # Jekyll tags: {:toc}, {:lead}
    re.compile(r"\{\{.*?\}\}"),  # Liquid templates: {{ ... }}
    re.compile(r"^<[^>]+>.*"),  # HTML tags
    re.compile(r"relative_url"),  # relative_url filter
    re.compile(r"^!\[.*?\]\(.*?\)"),  # Image markdown: ![alt](url)
    re.compile(r"^\[.*?\]\(.*?\)"),  # Link markdown: [text](url)
    re.compile(r"^https?://.*"),  # URLs
    re.compile(r"`.*?`"),  # Inline code: `...`
    re.compile(r"`{3}.*?`{3}"),  # Code blocks
    re.compile(r"^\$.*\$$"),  # Inline math: $...$
    re.compile(r"^\$\$.*\$\$$"),  # Display math: $$...$$
]


class CustomMDRenderer(MDRenderer):
    """MDRenderer that avoids escaping content matching SKIP_PATTERNS.

    The MDRenderer from mdformat may escape some characters aggressively. We
    override the text renderer to leave token.content alone when it matches
    one of the skip patterns (Jekyll/Liquid tags, math, URLs, asset paths,
    image/link markdown, etc.).
    """

    def text(self, tokens, idx, options, env):
        content = tokens[idx].content
        # If the entire token content matches any skip pattern, return it unchanged
        s = content.strip()
        for patt in SKIP_PATTERNS:
            if patt.fullmatch(s):
                return content
        # Otherwise, fall back to default behavior
        return super().text(tokens, idx, options, env)


def translate_tokens(tokens, source_lang, target_lang, translator):
    """
    Recursively translate text in tokens from markdown-it-py AST.

    Args:
        tokens: List of Token objects from markdown-it-py
        source_lang: Source language code
        target_lang: Target language code
        translator: Translation service name
    """
    for token in tokens:
        # Log token type and content for debugging
        token_type = token.type
        token_content = token.content[:100] if token.content else ""
        print(
            f"DEBUG: Processing token: {token_type} - Content: {repr(token_content)}",
            file=sys.stderr,
        )

        # Translate content if it's a text token
        if token.type == "text" and token.content.strip():
            text = token.content

            # Skip translation for various non-translatable patterns
            s = text.strip()
            if not any(patt.fullmatch(s) for patt in SKIP_PATTERNS):
                # Preserve leading and trailing whitespace using regex
                match = re.match(r"^(\s*)(.*?)(\s*)$", text, re.DOTALL)
                if match:
                    leading_ws, text_to_translate, trailing_ws = match.groups()

                    try:
                        translated = ts.translate_text(
                            text_to_translate,
                            translator=translator,
                            from_language=source_lang,
                            to_language=target_lang,
                        )
                        # Restore original whitespace (including newlines)
                        token.content = leading_ws + translated + trailing_ws
                    except Exception as e:
                        print(
                            f"Warning: Failed to translate text '{text}...': {e}",
                            file=sys.stderr,
                        )

        # Recursively process children tokens
        if token.children:
            translate_tokens(token.children, source_lang, target_lang, translator)


def translate_markdown_content(content, source_lang, target_lang, translator):
    """
    Translate markdown content by parsing to AST, translating text nodes, and rendering back.

    This function:
    1. Parses markdown to an Abstract Syntax Tree (AST) using markdown-it-py
    2. Recursively traverses the tree and translates text nodes
    3. Skips non-translatable content (code, HTML, Jekyll/Liquid syntax, URLs)
    4. Renders the modified AST back to markdown using mdformat's built-in renderer

    Args:
        content: Raw markdown content to translate
        source_lang: Source language code
        target_lang: Target language code
        translator: Translation service name

    Returns:
        Translated markdown content as a string
    """
    try:
        # Parse markdown to AST using markdown-it-py
        md = MarkdownIt()
        tokens = md.parse(content)
    except Exception as e:
        print(
            f"Warning: Failed to parse markdown: {e}",
            file=sys.stderr,
        )
        return content

    # Recursively translate text nodes in the token tree
    translate_tokens(tokens, source_lang, target_lang, translator)

    # For tokens matching SKIP_PATTERNS, replace their content with a
    # unique placeholder so the renderer can't mangle/escape them, then
    # restore the originals after rendering. This preserves the exact
    # original text for skip-pattern tokens.
    placeholder_map = {}
    counter = 0

    def inject_placeholders(toks):
        nonlocal counter
        for tk in toks:
            if getattr(tk, "content", None):
                s = tk.content.strip()
                for patt in SKIP_PATTERNS:
                    if patt.fullmatch(s):
                        # use an alphanumeric-only placeholder to avoid mdformat
                        # escaping underscores or other punctuation
                        ph = f"VGPPLACEHOLDER{counter}"
                        placeholder_map[ph] = tk.content
                        tk.content = ph
                        counter += 1
                        break
            if getattr(tk, "children", None):
                inject_placeholders(tk.children)

    inject_placeholders(tokens)

    # Render back to markdown using mdformat's built-in renderer
    try:
        renderer = CustomMDRenderer()
        options = {
            "number": True,  # switch on consecutive numbering of ordered lists
            "end-of-line": "keep",
        }
        env = {}
        rendered = renderer.render(tokens, options, env)

        # Restore placeholders with the original raw content
        if placeholder_map:
            for ph, original in placeholder_map.items():
                rendered = rendered.replace(ph, original)

        return rendered
    except Exception as e:
        print(
            f"Warning: Failed to render markdown: {e}",
            file=sys.stderr,
        )
        return content


def translate_file(source_path, target_path, source_lang, target_lang, translator):
    """
    Translate a markdown file from source language to target language.

    Args:
        source_path: Path to the source markdown file
        target_path: Path to the target markdown file
        source_lang: Source language code (e.g., 'en')
        target_lang: Target language code (e.g., 'bn', 'hi')
        translator: Translation service to use (e.g., 'google', 'bing', 'baidu')

    Raises:
        FileNotFoundError: If source file does not exist
        IOError: If unable to read source or write target file
    """
    # Read the source file
    try:
        with open(source_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Source file not found: {source_path}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error: Failed to read source file: {e}", file=sys.stderr)
        sys.exit(1)

    # Load the post with frontmatter
    try:
        post = frontmatter.loads(content)
    except Exception as e:
        print(f"Warning: Failed to parse frontmatter: {e}", file=sys.stderr)
        # Fall back to treating the entire content as body
        post = frontmatter.Post("")
        post.content = content

    # Update or add lang key in frontmatter
    post.metadata["lang"] = target_lang

    # Translate the markdown content using AST parsing
    translated_body = translate_markdown_content(
        post.content, source_lang, target_lang, translator
    )

    # Update the post content with translated body
    post.content = translated_body

    # Write the translated file
    try:
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(frontmatter.dumps(post))
        print(f"✓ Successfully translated {source_path} → {target_path}")
    except IOError as e:
        print(f"Error: Failed to write target file: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Translate markdown files using the translators library.",
        epilog="Example: python translate.py --source-file en/index.md --target-file bn/index.md --source-lang en --target-lang bn --translator google",
    )
    parser.add_argument(
        "--source-file", required=True, help="Path to the source markdown file"
    )
    parser.add_argument(
        "--target-file", required=True, help="Path to the target markdown file"
    )
    parser.add_argument(
        "--source-lang", required=True, help="Source language code (e.g., en, es, fr)"
    )
    parser.add_argument(
        "--target-lang", required=True, help="Target language code (e.g., bn, hi, es)"
    )
    parser.add_argument(
        "--translator",
        required=True,
        choices=["google", "bing", "baidu", "youdao"],
        help="Translation service to use",
    )

    args = parser.parse_args()

    # Validate language codes
    if not args.source_lang or not args.target_lang:
        parser.error("Language codes cannot be empty")

    if args.source_lang == args.target_lang:
        print(
            "Warning: Source and target languages are the same. No translation will occur."
        )

    translate_file(
        args.source_file,
        args.target_file,
        args.source_lang,
        args.target_lang,
        args.translator,
    )


if __name__ == "__main__":
    main()
