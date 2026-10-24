
# VirtualGamePad

[![GitHub License](https://img.shields.io/github/license/kitswas/VirtualGamePad)
![GitHub Stars](https://img.shields.io/github/stars/kitswas/VirtualGamePad?style=social)](https://github.com/kitswas/VirtualGamePad/)

VirtualGamePad lets you use your Android phone as a gamepad for your Windows and Linux PCs.  
Free and Open-Source with no ads or tracking.

**For more information, downloads, etc. visit [the official VirtualGamePad website](https://kitswas.github.io/VirtualGamePad).**

This repository contains the source code for the website.

## Building the website

Requires [Hugo](https://gohugo.io/getting-started/installing/). The pinned version (same as CI, see `[tools]` in `mise.toml`) installs with [mise](https://mise.jdx.dev/): `mise install`, then prefix commands with `mise exec --`.

Dev server:

```bash
hugo server --disableFastRender
```

Production build:

```bash
hugo build --minify # --watch to rebuild automatically on change
# pnpx server public # Or any other server of your choice, to see the built site
```

A GitHub Actions workflow handles build and deployment.

## Git hooks

Enable the repository hooks once per clone:

```bash
git config core.hooksPath .githooks
```

`pre-push` runs `hugo --gc --minify` and blocks pushing a site that does not build (`git push --no-verify` to bypass); `post-merge` runs the same build check after merges/pulls. Disable with `git config --unset core.hooksPath`.

## Writing blog posts

Posts live in `content/blog/`. Create one with the archetype, which fills in the
title from the file name, today's date and `draft: true`:

```bash
hugo new content blog/my-post.md
```

Preview drafts before publishing:

```bash
hugo server --buildDrafts
```

The "last updated" date shown on a post comes from the Git author date of the
commit that last touched the file. Set `lastmod` in the front matter to
override it.

## Star History

[![VirtualGamePad Star History Chart](https://raw.githubusercontent.com/kitswas/generate-star-history/refs/heads/main/assets/star-history-virtualgamepad.svg)](https://github.com/kitswas/generate-star-history)
