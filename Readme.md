
# VirtualGamePad

[![GitHub License](https://img.shields.io/github/license/kitswas/VirtualGamePad)
![GitHub Stars](https://img.shields.io/github/stars/kitswas/VirtualGamePad?style=social)](https://github.com/kitswas/VirtualGamePad/)

VirtualGamePad lets you use your Android phone as a gamepad for your Windows and Linux PCs.  
Free and Open-Source with no ads or tracking.

**For more information, downloads, etc. visit [the official VirtualGamePad website](https://kitswas.github.io/VirtualGamePad).**

This repository contains the source code for the website.

## Building the website

Requires [Hugo](https://gohugo.io/getting-started/installing/).

Dev server:

```bash
hugo server --disableFastRender
```

Production build:

```bash
hugo build
# pnpx server public # Or any other server of your choice, to see the built site
```

A GitHub Actions workflow handles build and deployment.
