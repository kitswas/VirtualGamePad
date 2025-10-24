---
lang: bn
layout: default
---

# VirtualGamePad

AI-translated {: .ai-banner}

[![GitHub License](https://img.shields.io/github/license/kitswas/VirtualGamePad)
![GitHub Stars](https://img.shields.io/github/stars/kitswas/VirtualGamePad?style=social)](https://github.com/kitswas/VirtualGamePad/)

VirtualGamePad আপনাকে আপনার Android ফোনকে আপনার PC-র জন্য একটি গেমপ্যাড হিসেবে ব্যবহার করতে দেয়।  
এটি DroidJoy-এর মতো, কিন্তু ***বিনামূল্যে*** এবং ***ওপেন-সোর্স***।

> **কোনো বিজ্ঞাপন নেই, কোনো ট্র্যাকিং নেই, কোনো পেওয়াল নেই।**
{:.lead}

- this list will be replaced by the table of contents
{:toc}

## VirtualGamePad ব্যবহারের সুবিধা

- **বিনামূল্যে এবং ওপেন সোর্স**: কোনো বিজ্ঞাপন নেই, কোনো ট্র্যাকিং নেই, কোনো পেওয়াল নেই।
- **নিরাপদ**: কোডটি যে কারও পর্যালোচনা করার জন্য উন্মুক্ত। কোথা-থেকে-এসেছে-জানা-নেই এমন একটি র‍্যান্ডম অ্যাপকে বিশ্বাস করার দরকার নেই।
- **ব্যবহার করা সহজ**: শুধু আপনার ফোনে অ্যাপটি ইনস্টল করুন এবং আপনার PC-তে পোর্টেবল সার্ভার ডাউনলোড করুন।
Wi-Fi-র মাধ্যমে সংযুক্ত হন ([অথবা USB](FAQ.md#usb-connection)) এবং উপভোগ করুন!
- **কোনো বোঝা নেই**: সার্ভার একটি পোর্টেবল অ্যাপ। কোনো ইনস্টলেশন নেই। কোনো অতিরিক্ত ড্রাইভার (যেমন vJoy) প্রয়োজন নেই।
- **অর্থনৈতিক ও পরিবেশবান্ধব**: নতুন গেমপ্যাড কেনার দরকার নেই। পরিবর্তে আপনার পুরানো ফোন ব্যবহার করুন। অর্থ সাশ্রয় করুন এবং ই-বর্জ্য কমান।

## স্ক্রিনশট

একটি Android 12 ডিভাইসে চলমান VirtualGamePad:

![VirtualGamePad]({{ '/assets/VGP.svg' | relative_url }})

![VirtualGamePad Dark]({{ '/assets/VGP_night.svg' | relative_url }})

একটি PC-তে চলমান VirtualGamePad Server:

![VirtualGamePad Server]({{ '/assets/VGP_Server.png' | relative_url }})

## ইনস্টলেশন

VirtualGamePad ব্যবহার করতে, আপনাকে আপনার ফোনে Android অ্যাপ (ক্লায়েন্ট) ইনস্টল করতে হবে এবং আপনার PC-তে পোর্টেবল PC অ্যাপ (সার্ভার) ডাউনলোড করতে হবে।

নতুন আপডেট সম্পর্কে অবহিত হতে, আপনি GitHub-এ সোর্স রিপোজিটরিগুলিকে star ⭐ বা watch 👁️ করতে পারেন।

![GitHub Star and Watch]({{ '/assets/GitHub_Star_Watch.png' | relative_url }})

### Android

F-Droid এবং GitHub-এ পাওয়া যায়।

[<img src="{{ '/assets/badge_F_Droid_download.svg' | relative_url }}" alt="Get it on F-Droid" style="height:4em;"> ![Downloads last month](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgithub.com%2Fkitswas%2Ffdroid-metrics-dashboard%2Fraw%2Frefs%2Fheads%2Fmain%2Fprocessed%2Fmonthly%2Fio.github.kitswas.virtualgamepadmobile.json&query=%24.total_downloads&logo=fdroid&label=Downloads%20last%20month)
![F-Droid latest version](https://img.shields.io/f-droid/v/io.github.kitswas.virtualgamepadmobile?logo=f-droid)](https://f-droid.org/packages/io.github.kitswas.virtualgamepadmobile/)

অথবা, [releases page](https://github.com/kitswas/VirtualGamePad-Mobile/releases) থেকে সর্বশেষ APK নিন এবং আপনার ফোনে ইনস্টল করুন।  
[<img src="{{ '/assets/badge_Github_download.svg' | relative_url }}" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-Mobile/total)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-Mobile?logo=github)](https://github.com/kitswas/VirtualGamePad-Mobile/releases/latest)

### Windows

[releases page](https://github.com/kitswas/VirtualGamePad-PC/releases) থেকে সর্বশেষ archive(Virtual-GamePad-Windows.zip) নিন, এটি extract করুন এবং `VGamepadPC.exe` চালান।  
পরীক্ষামূলক Gamepad Input mode-এর অতিরিক্ত প্রয়োজনীয়তা রয়েছে, Preferences পৃষ্ঠায় in-app বর্ণনা দেখুন।  
[<img src="{{ '/assets/badge_Github_download.svg' | relative_url }}" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (specific asset, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-PC/Virtual-GamePad-Windows.zip)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-PC?logo=github)](https://github.com/kitswas/VirtualGamePad-PC/releases/latest)

### Linux

[releases page](https://github.com/kitswas/VirtualGamePad-PC/releases) থেকে সর্বশেষ archive(Virtual-GamePad-Ubuntu.zip) নিন, এটি extract করুন, `chmod +x bin/VGamepadPC` এবং `bin/VGamepadPC` চালান।  
যদি Qt `xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin` সম্পর্কে অভিযোগ করে, `sudo apt install libxcb-cursor0` এটি ঠিক করা উচিত।  
Preferences পৃষ্ঠায় in-app বর্ণনা দেখুন।  
[<img src="{{ '/assets/badge_Github_download.svg' | relative_url }}" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (specific asset, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-PC/Virtual-GamePad-Ubuntu.zip)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-PC?logo=github)](https://github.com/kitswas/VirtualGamePad-PC/releases/latest)

আমরা এটি শুধুমাত্র Ubuntu/Debian-এ পরীক্ষা করেছি। তবে এটি অন্যান্য distribution-এও কাজ করা উচিত।

[releases page](https://github.com/kitswas/VirtualGamePad-PC/releases) থেকে সর্বশেষ archive(Virtual-GamePad-Ubuntu.zip) ডাউনলোড করুন, extract করুন, `chmod +x bin/VGamepadPC` এবং `bin/VGamepadPC` চালান।  
Qt যদি 'xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin' বলে, `sudo apt install libxcb-cursor0` চালান।  
Preferences পেজে বিস্তারিত দেখুন।  

[<img src="{{ '/assets/badge_Github_download.svg' | relative_url }}" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (specific asset, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-PC/Virtual-GamePad-Ubuntu.zip)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-PC?logo=github)](https://github.com/kitswas/VirtualGamePad-PC/releases/latest)

Ubuntu/Debian-এ পরীক্ষা করা হয়েছে। অন্য distribution-এও কাজ করার কথা।

## ব্যবহার

আপনার PC-তে সার্ভার এবং আপনার ফোনে ক্লায়েন্ট চালান।  
সার্ভারের IP address এবং port লিখে Android অ্যাপ থেকে সার্ভারের সাথে সংযুক্ত হন।  
উভয় ডিভাইসকে একই নেটওয়ার্কে থাকতে হবে।

[**এখানে FAQ পড়ুন**](FAQ.md)।

সমস্যা হচ্ছে? [Troubleshooting ডকুমেন্ট](Troubleshooting.md) দেখুন।

## সোর্স কোড

খুশি হলাম যে আপনি জিজ্ঞাসা করলেন! VirtualGamePad ওপেন সোর্স এবং [GPLv3 licence]({{ '/LICENCE.TXT' | relative_url }})-এর অধীনে লাইসেন্সপ্রাপ্ত।

VirtualGamePad ওপেন-সোর্স লাইব্রেরি এবং অ্যাসেট ব্যবহার করে যা তাদের নিজস্ব লাইসেন্স দ্বারা পরিচালিত হয়।

Android অ্যাপের সোর্স কোড [kitswas/VirtualGamePad-Mobile](https://github.com/kitswas/VirtualGamePad-Mobile)-এ পাওয়া যায়।

Windows অ্যাপের সোর্স কোড [kitswas/VirtualGamePad-PC](https://github.com/kitswas/VirtualGamePad-PC)-তে পাওয়া যায়।  
ডকুমেন্টেশন দেখতে [companion website](https://kitswas.github.io/VirtualGamePad-PC/) ভিজিট করুন।

[kitswas/VGP_Data_Exchange](https://github.com/kitswas/VGP_Data_Exchange/) ক্লায়েন্ট এবং সার্ভারের মধ্যে যোগাযোগ হ্যান্ডেল করতে ব্যবহৃত হয়।

### Star History

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date&theme=dark" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date" />
 <img loading="lazy" alt="VirtualGamePad Star History Chart" src="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date" />
