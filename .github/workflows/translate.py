#!/usr/bin/env python3
"""
Translate markdown files using the translators library.

This script parses markdown to AST using mistletoe, translates text nodes with translate_text,
and renders back to markdown to ensure proper handling of markdown syntax during translation.

Dependencies:
    uv pip install translators python-frontmatter mistletoe mdformat

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
import mistletoe
from mistletoe import Document
from mistletoe.markdown_renderer import MarkdownRenderer


def translate_token_tree(token, source_lang, target_lang, translator):
    """
    Recursively translate text nodes in the mistletoe Token tree.

    Skips translation for:
    - Jekyll tags: {:toc}, {:lead}, etc.
    - Liquid template syntax: {{ ... }}
    - HTML tags and raw HTML content
    - Code blocks and inline code
    - Image markdown syntax ![...](...)
    - Link URLs
    """
    # Import here to avoid issues if mistletoe internals change
    from mistletoe.span_token import RawText
    from mistletoe.span_token import InlineCode

    if isinstance(token, RawText):
        text = token.content

        # Skip translation for various non-translatable patterns
        skip_patterns = [
            r"\{:[^}]*\}",  # Jekyll tags: {:toc}, {:lead}
            r"\{\{.*?\}\}",  # Liquid templates: {{ ... }}
            r"^<[^>]+>.*",  # HTML tags
            r"relative_url",  # relative_url filter
            r"^!\[.*?\]\(.*?\)",  # Image markdown: ![alt](url)
            r"^\[.*?\]\(.*?\)",  # Link markdown: [text](url)
            r"^https?://.*",  # URLs
            r"^/assets/.*",  # Asset paths
        ]

        if any(re.fullmatch(pattern, text.strip()) for pattern in skip_patterns):
            return

        if text.strip():
            # Preserve leading and trailing whitespace
            leading_ws = len(text) - len(text.lstrip())
            trailing_ws = len(text) - len(text.rstrip())
            text_to_translate = text.strip()

            try:
                translated = ts.translate_text(
                    text_to_translate,
                    translator=translator,
                    from_language=source_lang,
                    to_language=target_lang,
                )
                # Restore original whitespace
                if leading_ws > 0:
                    translated = text[:leading_ws] + translated
                if trailing_ws > 0:
                    translated = translated + text[-trailing_ws:]
                token.content = translated
            except Exception as e:
                print(
                    f"Warning: Failed to translate text '{text[:50]}...': {e}",
                    file=sys.stderr,
                )
    elif isinstance(token, InlineCode):
        # Skip translation of inline code - it's code, not text
        return
    elif hasattr(token, "children") and isinstance(token.children, list):
        for child in token.children:
            translate_token_tree(child, source_lang, target_lang, translator)


def translate_markdown_content(content, source_lang, target_lang, translator):
    """
    Translate markdown content by parsing to AST, translating text nodes, and rendering back.

    This function:
    1. Parses markdown to an Abstract Syntax Tree (AST) using mistletoe
    2. Recursively traverses the tree and translates RawText nodes
    3. Skips non-translatable content (code, HTML, Jekyll/Liquid syntax, URLs)
    4. Renders the modified AST back to markdown

    Args:
        content: Raw markdown content to translate
        source_lang: Source language code
        target_lang: Target language code
        translator: Translation service name

    Returns:
        Translated markdown content as a string
    """
    try:
        # Parse markdown to AST
        doc: Document = mistletoe.Document(content)
    except Exception as e:
        print(
            f"Warning: Failed to parse markdown: {e}",
            file=sys.stderr,
        )
        return content

    # Recursively translate text nodes in the token tree
    translate_token_tree(doc, source_lang, target_lang, translator)

    # Render back to markdown (preserve whitespace)
    try:
        renderer = MarkdownRenderer(normalize_whitespace=False)
        return renderer.render(doc)
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
