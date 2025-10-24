---
lang: te
layout: default
---

# VirtualGamePad

AI-translated {: .ai-banner}

[![GitHub License](https://img.shields.io/github/license/kitswas/VirtualGamePad)
![GitHub Stars](https://img.shields.io/github/stars/kitswas/VirtualGamePad?style=social)](https://github.com/kitswas/VirtualGamePad/)

VirtualGamePad మీ Android ఫోన్‌ను మీ PC ల కోసం గేమ్‌పాడ్‌గా ఉపయోగించడానికి అనుమతిస్తుంది.  
ఇది DroidJoy లాగా ఉంటుంది, కానీ ***ఉచితం*** మరియు ***ఓపెన్-సోర్స్***.

> **ప్రకటనలు లేవు, ట్రాకింగ్ లేదు, పేవాల్స్ లేవు.**
{:.lead}

- ఈ జాబితా విషయ సూచిక ద్వారా భర్తీ చేయబడుతుంది
{:toc}

## VirtualGamePad ఉపయోగించడం వల్ల లాభాలు

- **ఉచితం మరియు ఓపెన్ సోర్స్**: ప్రకటనలు లేవు, ట్రాకింగ్ లేదు, పేవాల్స్ లేవు.
- **సురక్షితం**: కోడ్ ఎవరైనా సమీక్షించడానికి తెరిచి ఉంది. ఎవరికి-ఎక్కడ-నుండి అనే యాప్‌ను విశ్వసించాల్సిన అవసరం లేదు.
- **ఉపయోగించడానికి సులభం**: మీ ఫోన్‌లో యాప్ ఇన్‌స్టాల్ చేసి మీ PC లో పోర్టబుల్ సర్వర్ డౌన్‌లోడ్ చేయండి.
Wi-Fi ([లేదా USB](FAQ.md#usb-connection)) ద్వారా కనెక్ట్ చేసి ఆనందించండి!
- **బ్లోట్ లేదు**: సర్వర్ పోర్టబుల్ యాప్. ఇన్‌స్టాలేషన్ లేదు. అదనపు డ్రైవర్లు (vJoy లాంటివి) అవసరం లేదు.
- **ఆర్థికంగా & పర్యావరణ స్నేహపూర్వకం**: కొత్త గేమ్‌పాడ్ కొనవలసిన అవసరం లేదు. బదులుగా మీ పాత ఫోన్ ఉపయోగించండి. డబ్బు ఆదా చేయండి మరియు ఇ-వేస్ట్ తగ్గించండి.

## స్క్రీన్‌షాట్‌లు

Android 12 పరికరంలో VirtualGamePad రన్ అవుతోంది:

![VirtualGamePad]({{ '/assets/VGP.svg' | relative_url }})

![VirtualGamePad Dark]({{ '/assets/VGP_night.svg' | relative_url }})

PC లో VirtualGamePad సర్వర్ రన్ అవుతోంది:

![VirtualGamePad Server]({{ '/assets/VGP_Server.png' | relative_url }})

## ఇన్‌స్టాలేషన్

VirtualGamePad ఉపయోగించడానికి, మీరు మీ ఫోన్‌లో Android యాప్ (క్లయింట్) ఇన్‌స్టాల్ చేసి మరియు మీ PC లో పోర్టబుల్ PC యాప్ (సర్వర్) డౌన్‌లోడ్ చేయాలి.

కొత్త అప్‌డేట్‌ల గురించి నోటిఫికేషన్ పొందడానికి, మీరు GitHub లో సోర్స్ రిపోజిటరీలను స్టార్ ⭐ లేదా వాచ్ 👁️ చేయవచ్చు.

![GitHub Star and Watch]({{ '/assets/GitHub_Star_Watch.png' | relative_url }})

### Android

F-Droid మరియు GitHub లో అందుబాటులో ఉంది.

[<img src="{{ '/assets/badge_F_Droid_download.svg' | relative_url }}" alt="Get it on F-Droid" style="height:4em;"> ![Downloads last month](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgithub.com%2Fkitswas%2Ffdroid-metrics-dashboard%2Fraw%2Frefs%2Fheads%2Fmain%2Fprocessed%2Fmonthly%2Fio.github.kitswas.virtualgamepadmobile.json&query=%24.total_downloads&logo=fdroid&label=Downloads%20last%20month)
![F-Droid latest version](https://img.shields.io/f-droid/v/io.github.kitswas.virtualgamepadmobile?logo=f-droid)](https://f-droid.org/packages/io.github.kitswas.virtualgamepadmobile/)

లేదా, [విడుదలల పేజీ](https://github.com/kitswas/VirtualGamePad-Mobile/releases) నుండి తాజా APK పొందండి మరియు మీ ఫోన్‌లో ఇన్‌స్టాల్ చేయండి.  
[<img src="{{ '/assets/badge_Github_download.svg' | relative_url }}" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-Mobile/total)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-Mobile?logo=github)](https://github.com/kitswas/VirtualGamePad-Mobile/releases/latest)

### Windows

[విడుదలల పేజీ](https://github.com/kitswas/VirtualGamePad-PC/releases) నుండి తాజా ఆర్కైవ్ (Virtual-GamePad-Windows.zip) పొందండి, దానిని ఎక్స్‌ట్రాక్ట్ చేసి `VGamepadPC.exe` రన్ చేయండి.  
ప్రయోగాత్మక గేమ్‌పాడ్ ఇన్‌పుట్ మోడ్‌కు అదనపు అవసరాలు ఉన్నాయి, Preferences పేజీలోని ఇన్-యాప్ వివరణ చూడండి.  
[<img src="{{ '/assets/badge_Github_download.svg' | relative_url }}" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (specific asset, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-PC/Virtual-GamePad-Windows.zip)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-PC?logo=github)](https://github.com/kitswas/VirtualGamePad-PC/releases/latest)

### Linux

[విడుదలల పేజీ](https://github.com/kitswas/VirtualGamePad-PC/releases) నుండి తాజా ఆర్కైవ్ (Virtual-GamePad-Ubuntu.zip) పొందండి, దానిని ఎక్స్‌ట్రాక్ట్ చేసి, `chmod +x bin/VGamepadPC` మరియు `bin/VGamepadPC` చేయండి.  
Qt `xcb-cursor0 లేదా libxcb-cursor0 Qt xcb ప్లాట్‌ఫారమ్ ప్లగిన్ లోడ్ చేయడానికి అవసరం` అని ఫిర్యాదు చేస్తే, `sudo apt install libxcb-cursor0` పరిష్కరిస్తుంది.  
Preferences పేజీలోని ఇన్-యాప్ వివరణ చూడండి.  
[<img src="{{ '/assets/badge_Github_download.svg' | relative_url }}" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (specific asset, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-PC/Virtual-GamePad-Ubuntu.zip)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-PC?logo=github)](https://github.com/kitswas/VirtualGamePad-PC/releases/latest)

మేము దీన్ని Ubuntu/Debian లో మాత్రమే పరీక్షించాము. కానీ ఇది ఇతర డిస్ట్రిబ్యూషన్లలో కూడా పనిచేయాలి.

## ఉపయోగం

మీ PC లో సర్వర్ మరియు మీ ఫోన్‌లో క్లయింట్ రన్ చేయండి.  
Android యాప్ నుండి సర్వర్ యొక్క IP అడ్రస్ మరియు పోర్ట్ ఎంటర్ చేయడం ద్వారా సర్వర్‌కు కనెక్ట్ చేయండి.  
రెండు పరికరాలు ఒకే నెట్‌వర్క్‌లో ఉండాలి.

[**ఇక్కడ FAQ చదవండి**](FAQ.md).

సమస్యలు ఉన్నాయా? [ట్రబుల్షూటింగ్ డాక్యుమెంట్](Troubleshooting.md) చూడండి.

## సోర్స్ కోడ్

అడిగినందుకు సంతోషం! VirtualGamePad ఓపెన్ సోర్స్ మరియు [GPLv3 లైసెన్స్]({{ '/LICENCE.TXT' | relative_url }}) క్రింద లైసెన్స్ పొందింది.

VirtualGamePad ఓపెన్-సోర్స్ లైబ్రరీలు మరియు అసెట్‌లను ఉపయోగిస్తుంది, ఇవి వాటి స్వంత లైసెన్స్‌లచే నియంత్రించబడతాయి.

Android యాప్ కోసం సోర్స్ కోడ్ [kitswas/VirtualGamePad-Mobile](https://github.com/kitswas/VirtualGamePad-Mobile) వద్ద అందుబాటులో ఉంది.

Windows యాప్ కోసం సోర్స్ కోడ్ [kitswas/VirtualGamePad-PC](https://github.com/kitswas/VirtualGamePad-PC) వద్ద అందుబాటులో ఉంది.  
డాక్యుమెంటేషన్ చూడటానికి [కంపానియన్ వెబ్‌సైట్](https://kitswas.github.io/VirtualGamePad-PC/) సందర్శించండి.

క్లయింట్ మరియు సర్వర్ మధ్య కమ్యూనికేషన్ హ్యాండిల్ చేయడానికి [kitswas/VGP_Data_Exchange](https://github.com/kitswas/VGP_Data_Exchange/) ఉపయోగించబడుతుంది.

### స్టార్ చరిత్ర

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date&theme=dark" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date" />
 <img loading="lazy" alt="VirtualGamePad Star History Chart" src="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date" />
</picture>
