---
lang: hi
layout: default
---

# VirtualGamePad

AI-translated
{:.label.warning}

[![GitHub License](https://img.shields.io/github/license/kitswas/VirtualGamePad)
![GitHub Stars](https://img.shields.io/github/stars/kitswas/VirtualGamePad?style=social)](https://github.com/kitswas/VirtualGamePad/)

VirtualGamePad आपको अपने Android phone को अपने PCs के लिए gamepad के रूप में उपयोग करने देता है।  
यह DroidJoy के समान है, लेकिन ***free*** और ***open-source*** है।

> **No ads, no tracking, no paywalls।**
{:.lead}

- this list will be replaced by the table of contents
{:toc}

## VirtualGamePad का उपयोग करने के Benefits

- **Free और Open Source**: कोई ads नहीं, कोई tracking नहीं, कोई paywalls नहीं।
- **Secure**: Code किसी के भी review के लिए खुला है। किसी random app पर trust करने की ज़रूरत नहीं है जो न जाने कहाँ से आया हो।
- **Easy to Use**: बस अपने phone पर app install करें और अपने PC पर portable server download करें।
Wi-Fi के माध्यम से connect करें ([या USB](FAQ.md#usb-connection)) और enjoy करें!
- **No Bloat**: Server एक portable app है। कोई installation नहीं। कोई extra drivers (जैसे vJoy) की ज़रूरत नहीं।
- **Economical & Eco-friendly**: नया gamepad खरीदने की ज़रूरत नहीं। अपने पुराने phone का उपयोग करें। पैसे बचाएँ और e-waste कम करें।

## Screenshots

VirtualGamePad एक Android 12 device पर running है:

![VirtualGamePad]({{ '/assets/VGP.svg' | relative_url }})

![VirtualGamePad Dark]({{ '/assets/VGP_night.svg' | relative_url }})

VirtualGamePad Server एक PC पर running है:

![VirtualGamePad Server]({{ '/assets/VGP_Server.png' | relative_url }})

## Installation

VirtualGamePad का उपयोग करने के लिए, आपको अपने phone पर Android app (client) install करना होगा और अपने PC पर portable PC app (server) download करना होगा।

नए updates की notification पाने के लिए, आप GitHub पर source repositories को star ⭐ या watch 👁️ कर सकते हैं।

![GitHub Star and Watch]({{ '/assets/GitHub_Star_Watch.png' | relative_url }})

### Android

F-Droid और GitHub पर available है।

[<img src="{{ '/assets/badge_F_Droid_download.svg' | relative_url }}" alt="Get it on F-Droid" style="height:4em;"> ![Downloads last month](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgithub.com%2Fkitswas%2Ffdroid-metrics-dashboard%2Fraw%2Frefs%2Fheads%2Fmain%2Fprocessed%2Fmonthly%2Fio.github.kitswas.virtualgamepadmobile.json&query=%24.total_downloads&logo=fdroid&label=Downloads%20last%20month)
![F-Droid latest version](https://img.shields.io/f-droid/v/io.github.kitswas.virtualgamepadmobile?logo=f-droid)](https://f-droid.org/packages/io.github.kitswas.virtualgamepadmobile/)

या, [releases page](https://github.com/kitswas/VirtualGamePad-Mobile/releases) से latest APK grab करें और इसे अपने phone पर install करें।  
[<img src="{{ '/assets/badge_Github_download.svg' | relative_url }}" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-Mobile/total)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-Mobile?logo=github)](https://github.com/kitswas/VirtualGamePad-Mobile/releases/latest)

### Windows

[Releases page](https://github.com/kitswas/VirtualGamePad-PC/releases) से latest archive (Virtual-GamePad-Windows.zip) grab करें, इसे extract करें और `VGamepadPC.exe` run करें।  
Experimental Gamepad Input mode की extra requirements हैं, Preferences page पर in-app description देखें।  
[<img src="{{ '/assets/badge_Github_download.svg' | relative_url }}" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (specific asset, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-PC/Virtual-GamePad-Windows.zip)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-PC?logo=github)](https://github.com/kitswas/VirtualGamePad-PC/releases/latest)

### Linux

[Releases page](https://github.com/kitswas/VirtualGamePad-PC/releases) से latest archive (Virtual-GamePad-Ubuntu.zip) grab करें, इसे extract करें, `chmod +x bin/VGamepadPC` और `bin/VGamepadPC`।  
अगर Qt complain करता है `xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin`, तो `sudo apt install libxcb-cursor0` इसे fix कर देना चाहिए।  
Preferences page पर in-app description देखें।  
[<img src="{{ '/assets/badge_Github_download.svg' | relative_url }}" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (specific asset, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-PC/Virtual-GamePad-Ubuntu.zip)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-PC?logo=github)](https://github.com/kitswas/VirtualGamePad-PC/releases/latest)

हमने इसे केवल Ubuntu/Debian पर test किया। लेकिन यह दूसरे distributions पर भी काम करना चाहिए।

## Usage

अपने PC पर server और अपने phone पर client run करें।  
Server के IP address और port enter करके Android app से server से connect करें।  
दोनों devices एक ही network पर होने चाहिए।

[**यहाँ FAQ पढ़ें**](FAQ.md)।

Problems हो रही हैं? [Troubleshooting document](Troubleshooting.md) देखें।

## Source Code

खुशी है कि आपने पूछा! VirtualGamePad open source है और [GPLv3 licence]({{ '/LICENCE.TXT' | relative_url }}) के तहत licensed है।

VirtualGamePad open-source libraries और assets का उपयोग करता है जो उनके अपने licences द्वारा governed होते हैं।

Android app के लिए source code [kitswas/VirtualGamePad-Mobile](https://github.com/kitswas/VirtualGamePad-Mobile) पर available है।

Windows app के लिए source code [kitswas/VirtualGamePad-PC](https://github.com/kitswas/VirtualGamePad-PC) पर available है।  
Documentation देखने के लिए [companion website](https://kitswas.github.io/VirtualGamePad-PC/) visit करें।

[kitswas/VGP_Data_Exchange](https://github.com/kitswas/VGP_Data_Exchange/) client और server के बीच communication को handle करने के लिए use किया जाता है।

### Star History

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date&theme=dark" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date" />
 <img loading="lazy" alt="VirtualGamePad Star History Chart" src="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date" />
</picture>
