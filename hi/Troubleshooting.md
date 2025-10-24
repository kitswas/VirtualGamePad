---
lang: hi
description: |
  Virtual GamePad के लिए troubleshooting guide।
layout: default
---

# Troubleshooting

AI-translated {: .ai-banner}

अगर आपकी problem यहाँ covered नहीं है, तो [एक issue file करें](FAQ.md#bug-reports-and-feature-requests)।

- this list will be replaced by the table of contents
{:toc}

## Help! मैं server से connect नहीं कर सकता

अगर आपको server से connect करने में trouble हो रही है, तो अपने firewall को disable करने या server के लिए एक exception add करने की कोशिश करें।  
Windows पर, जब आप इसे पहली बार run करेंगे तो आपसे server को firewall के through communicate करने की permission देने के लिए prompt किया जाएगा।

![Firewall]({{ '/assets/VGP_UAC_Dialog.png' | relative_url }})

**अगर आपको अभी भी trouble हो रहा है, तो अपने phone पर hotspot start करें और अपने PC को उससे connect करें।** (या vice-versa, दोनों try करें)  
फिर, server restart करें और फिर से connecting try करें।

_App के काम न करने की complain करने से पहले यह करें।_

## Help! Client connected है लेकिन Gamepad किसी भी game के लिए काम नहीं करता

Server में Preferences screen check करें। अलग-अलग input methods (Keyboard/Mouse या Gamepad) की अलग-अलग requirements होती हैं।

![Screenshot of the Preferences screen at the time of writing]({{ '/assets/Server_preferences_Windows.png' | relative_url }})

Windows पर, Keyboard/Mouse mode out of the box काम करता है। Gamepad mode के लिए require होता है:

1. Admin privilege। (Right click करें और Run as admin)
2. App sideloading (developer mode) enabled। [(Settings > System > For developers > Developer mode)](ms-settings:developers)।

![Settings App sideloading]({{ '/assets/settings_app_sideloading.png' | relative_url }})  
![Turn on developer mode]({{ '/assets/developer_mode_UAC.png' | relative_url }})

Linux पर, server को `/dev/uinput` के लिए rw access की ज़रूरत होती है। इसे achieve करने के कई तरीके in-app describe किए गए हैं।

## Help! Gamepad किसी game के लिए काम नहीं करता

Server को admin के रूप में run करने की कोशिश करें। 🛡️

**Game को admin के रूप में run नहीं होना चाहिए।** यह input injection को prevent करता है।

Gamepad support के बिना games को out of the box काम करना चाहिए।

[How it works](https://kitswas.github.io/VirtualGamePad-PC/#how-it-works) पढ़ें यह जानने के लिए कि क्यों।

## Help! Gamepad laggy/unresponsive महसूस होता है

यह [FAQ](FAQ.md#feels-laggyunresponsive) में covered है।

## Bonus XKCD Comic

Tech Support Cheat Sheet — [XKCD 627](https://xkcd.com/627/):

![XKCD 627](https://imgs.xkcd.com/comics/tech_support_cheat_sheet_2x.png)
