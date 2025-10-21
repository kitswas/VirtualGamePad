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
    """
    # Import here to avoid issues if mistletoe internals change
    from mistletoe.span_token import RawText

    if isinstance(token, RawText):
        text = token.content
        # Skip translation for tokens like {:toc}, {:lead}, or anything in {:...}
        # Also skip anything inside double curly braces, e.g., {{ ... }} (including pipes, slashes, etc.)
        # Also skip raw HTML blocks (single or multi-line)
        # Additionally, ensure 'relative_url' is never translated inside {{ ... }}
        if (
            re.fullmatch(r"\{:[^}]*\}", text.strip())
            or re.fullmatch(r"\{\{.*?\}\}", text.strip())
            or re.match(r"^<[^>]+>.*", text.strip(), re.DOTALL)
            or re.fullmatch(r"relative_url", text.strip())
        ):
            return
        if text.strip():
            try:
                translated = ts.translate_text(
                    text,
                    translator=translator,
                    from_language=source_lang,
                    to_language=target_lang,
                )
                token.content = translated
            except Exception as e:
                print(
                    f"Warning: Failed to translate text '{text[:50]}...': {e}",
                    file=sys.stderr,
                )
    elif hasattr(token, "children") and isinstance(token.children, list):
        for child in token.children:
            translate_token_tree(child, source_lang, target_lang, translator)


def translate_markdown_content(content, source_lang, target_lang, translator):
    """
    Translate markdown content by parsing to AST, translating text nodes, and rendering back.
    """
    # Parse markdown to AST
    doc: Document = mistletoe.Document(content)

    # Recursively translate text nodes in the token tree
    translate_token_tree(doc, source_lang, target_lang, translator)

    # Render back to markdown
    renderer = MarkdownRenderer(normalize_whitespace=True)
    return renderer.render(doc)


def translate_file(source_path, target_path, source_lang, target_lang, translator):
    """
    Translate a markdown file from source language to target language.

    Args:
        source_path: Path to the source markdown file
        target_path: Path to the target markdown file
        source_lang: Source language code (e.g., 'en')
        target_lang: Target language code (e.g., 'bn', 'hi')
        translator: Translation service to use (e.g., 'google', 'bing', 'baidu')
    """
    # Read the source file
    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Load the post with frontmatter
    post = frontmatter.loads(content)

    # Update or add lang key in frontmatter
    post.metadata["lang"] = target_lang

    # Translate the markdown content using AST parsing
    translated_body = translate_markdown_content(
        post.content, source_lang, target_lang, translator
    )

    # Update the post content with translated body
    post.content = translated_body

    # Write the translated file
    frontmatter.dump(post, target_path)

    print(f"Successfully translated {source_path} -> {target_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Translate markdown files using the translators library."
    )
    parser.add_argument(
        "--source-file", required=True, help="Path to the source markdown file"
    )
    parser.add_argument(
        "--target-file", required=True, help="Path to the target markdown file"
    )
    parser.add_argument(
        "--source-lang", required=True, help="Source language code (e.g., en)"
    )
    parser.add_argument(
        "--target-lang", required=True, help="Target language code (e.g., bn, hi)"
    )
    parser.add_argument(
        "--translator",
        required=True,
        help="Translation service to use (e.g., google, bing, baidu)",
    )

    args = parser.parse_args()

    translate_file(
        args.source_file,
        args.target_file,
        args.source_lang,
        args.target_lang,
        args.translator,
    )


if __name__ == "__main__":
    main()
