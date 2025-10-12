---
lang: bn
layout: default
---

# VirtualGamePad

[![GitHub License](https://img.shields.io/github/license/kitswas/VirtualGamePad)
![GitHub Stars](https://img.shields.io/github/stars/kitswas/VirtualGamePad?style=social)](https://github.com/kitswas/VirtualGamePad/)

VirtualGamePad আপনাকে আপনার Android ফোনকে PC-র জন্য গেমপ্যাড হিসেবে ব্যবহার করতে দেয়।  
এটি DroidJoy-এর মতো, কিন্তু ***ফ্রি*** এবং ***ওপেন-সোর্স***।

> **কোনো বিজ্ঞাপন নেই, কোনো ট্র্যাকিং নেই, কোনো পেওয়াল নেই।**
{:.lead}

- এই তালিকাটি টেবিল অফ কনটেন্টস দ্বারা প্রতিস্থাপিত হবে
{:toc}

## VirtualGamePad ব্যবহারের সুবিধা

- **ফ্রি এবং ওপেন সোর্স**: কোনো বিজ্ঞাপন, ট্র্যাকিং, পেওয়াল নেই।
- **নিরাপদ**: কোড ওপেন, যে কেউ পর্যালোচনা করতে পারে।
- **সহজ ব্যবহার**: ফোনে অ্যাপ ইনস্টল করুন, PC-তে সার্ভার ডাউনলোড করুন।
Wi-Fi ([বা USB](FAQ.md#usb-connection)) দিয়ে সংযোগ করুন এবং উপভোগ করুন!
- **অতিরিক্ত কিছু নেই**: সার্ভারটি পোর্টেবল অ্যাপ। কোনো ইনস্টলেশন নেই। কোনো অতিরিক্ত ড্রাইভার (যেমন vJoy) লাগবে না।
- **সাশ্রয়কর ও পরিবেশবান্ধব**: নতুন গেমপ্যাড কিনতে হবে না। পুরনো ফোন ব্যবহার করুন। টাকা বাঁচান ও ই-ওয়েস্ট কমান।

## স্ক্রিনশট

Android 12 ডিভাইসে VirtualGamePad:

![VirtualGamePad](../assets/VGP.svg)

![VirtualGamePad Dark](../assets/VGP_night.svg)

PC-তে VirtualGamePad Server:

![VirtualGamePad Server](../assets/VGP_Server.png)

## ইনস্টলেশন

ব্যবহার করতে চাইলে ফোনে Android অ্যাপ (ক্লায়েন্ট) ইনস্টল করুন এবং PC-তে পোর্টেবল অ্যাপ (সার্ভার) ডাউনলোড করুন।

নতুন আপডেট জানতে GitHub-এ স্টার ⭐ বা ওয়াচ 👁️ দিন।

![GitHub Star and Watch](../assets/GitHub_Star_Watch.png)

### Android

F-Droid এবং GitHub-এ পাওয়া যায়।

[<img src="../assets/badge_F_Droid_download.svg" alt="Get it on F-Droid" style="height:4em;"> ![Downloads last month](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgithub.com%2Fkitswas%2Ffdroid-metrics-dashboard%2Fraw%2Frefs%2Fheads%2Fmain%2Fprocessed%2Fmonthly%2Fio.github.kitswas.virtualgamepadmobile.json&query=%24.total_downloads&logo=fdroid&label=Downloads%20last%20month)
![F-Droid latest version](https://img.shields.io/f-droid/v/io.github.kitswas.virtualgamepadmobile?logo=f-droid)](https://f-droid.org/packages/io.github.kitswas.virtualgamepadmobile/)

অথবা, [releases page](https://github.com/kitswas/VirtualGamePad-Mobile/releases) থেকে সর্বশেষ APK ডাউনলোড করুন এবং ফোনে ইনস্টল করুন।  

[<img src="../assets/badge_Github_download.svg" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-Mobile/total)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-Mobile?logo=github)](https://github.com/kitswas/VirtualGamePad-Mobile/releases/latest)

### Windows

[releases page](https://github.com/kitswas/VirtualGamePad-PC/releases) থেকে সর্বশেষ archive(Virtual-GamePad-Windows.zip) ডাউনলোড করুন, extract করুন এবং `VGamepadPC.exe` চালান।  
Experimental Gamepad Input mode-এর জন্য অতিরিক্ত কিছু লাগতে পারে, Preferences পেজে দেখুন।  

[<img src="../assets/badge_Github_download.svg" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (specific asset, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-PC/Virtual-GamePad-Windows.zip)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-PC?logo=github)](https://github.com/kitswas/VirtualGamePad-PC/releases/latest)

### Linux

[releases page](https://github.com/kitswas/VirtualGamePad-PC/releases) থেকে সর্বশেষ archive(Virtual-GamePad-Ubuntu.zip) ডাউনলোড করুন, extract করুন, `chmod +x bin/VGamepadPC` এবং `bin/VGamepadPC` চালান।  
Qt যদি 'xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin' বলে, `sudo apt install libxcb-cursor0` চালান।  
Preferences পেজে বিস্তারিত দেখুন।  

[<img src="../assets/badge_Github_download.svg" alt="Get it on GitHub" style="height:4em;"> ![GitHub Downloads (specific asset, all releases)](https://img.shields.io/github/downloads/kitswas/VirtualGamePad-PC/Virtual-GamePad-Ubuntu.zip)
![GitHub Latest Release](https://img.shields.io/github/v/release/kitswas/VirtualGamePad-PC?logo=github)](https://github.com/kitswas/VirtualGamePad-PC/releases/latest)

Ubuntu/Debian-এ পরীক্ষা করা হয়েছে। অন্য distribution-এও কাজ করার কথা।

## ব্যবহার

PC-তে সার্ভার চালান, ফোনে ক্লায়েন্ট চালান।  
Android অ্যাপ থেকে সার্ভারের IP ও port দিন এবং সংযোগ করুন।  
দুই ডিভাইস একই নেটওয়ার্কে থাকতে হবে।

[**FAQ পড়ুন এখানে**](FAQ.md)।

সমস্যা হলে [Troubleshooting document](Troubleshooting.md) দেখুন।

## সোর্স কোড

VirtualGamePad ওপেন সোর্স এবং [GPLv3 licence](../LICENCE.TXT)-এ লাইসেন্সকৃত।

VirtualGamePad ওপেন সোর্স লাইব্রেরি ও অ্যাসেট ব্যবহার করে, যেগুলোর নিজস্ব লাইসেন্স আছে।

Android অ্যাপের সোর্স কোড: [kitswas/VirtualGamePad-Mobile](https://github.com/kitswas/VirtualGamePad-Mobile)

Windows অ্যাপের সোর্স কোড: [kitswas/VirtualGamePad-PC](https://github.com/kitswas/VirtualGamePad-PC)।  
[companion website](https://kitswas.github.io/VirtualGamePad-PC/) দেখুন।

[kitswas/VGP_Data_Exchange](https://github.com/kitswas/VGP_Data_Exchange/) ক্লায়েন্ট ও সার্ভারের মধ্যে যোগাযোগের জন্য ব্যবহৃত হয়।

### স্টার হিস্ট্রি

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date&theme=dark" />
 <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date" />
 <img loading="lazy" alt="VirtualGamePad Star History Chart" src="https://api.star-history.com/svg?repos=kitswas/VirtualGamePad,kitswas/VirtualGamePad-PC,kitswas/VirtualGamePad-Mobile&type=Date" />
