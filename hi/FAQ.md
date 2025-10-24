---
lang: hi
description: |
  Virtual GamePad सिस्टम के बारे में अक्सर पूछे जाने वाले सवाल, जिसमें गेम compatibility, control mapping, performance, आदि शामिल हैं।
layout: default
---

# FAQ

AI-translated
{:.label.warning}

- this list will be replaced by the table of contents
{:toc}

## आप इसके साथ कौन से गेम्स खेलते हैं?

ज़्यादातर ऐसे गेम्स जिनमें gamepad support की कमी है।  
इसमें पुराने गेम्स और कई indie गेम्स शामिल हैं।

RPGs विशेष रूप से उपयुक्त हैं, क्योंकि उनमें अक्सर सरल controls होते हैं और quick reflexes की ज़रूरत नहीं होती।

Action गेम्स भी खेले जा सकते हैं, लेकिन आप प्रैक्टिस के लिए तैयार रहें।

## कोई लोकप्रिय titles?

मैंने [Assassin's Creed 4: Black Flag](https://en.wikipedia.org/wiki/Assassin's_Creed_IV%3A_Black_Flag), [Dave the Diver](https://en.wikipedia.org/wiki/Dave_the_Diver), [Ys X: Nordics](https://en.wikipedia.org/wiki/Ys_X:_Nordics), [Cassette Beasts](https://en.wikipedia.org/wiki/Cassette_Beasts) और [Dead Cells](https://en.wikipedia.org/wiki/Dead_Cells) इसके साथ खेले हैं।

## USB connection?

USB support पहले से मौजूद है।

यहाँ steps हैं:

- अपने फ़ोन को USB cable के माध्यम से अपने PC से connect करें।
- अपने फ़ोन पर, connection mode को USB tethering पर set करें।
- (Optional) अगर आपके पास limited data plan है, तो अपने फ़ोन पर mobile data बंद कर दें।
- Server चालू करें, सही IP चुनें और connect करें।

निम्नलिखित image USB के माध्यम से connected ऐप को दिखाती है।

![USB Tethering]({{ '/assets/VGP_USB_Tethering.png' | relative_url }})

## Default mapping मेरे लिए काम नहीं करती। मुझे क्या करना चाहिए?

आप कर सकते हैं:

1. अगर गेम इसे support करता है, तो in-game controls बदलें।
2. Controls को remap करने के लिए server में profile editor का उपयोग करें।

![Profile Editor]({{ '/assets/VGP_Profile_Editor.png' | relative_url }})

थोड़ी सी remapping के साथ, लगभग सब कुछ playable है।  

आप यहाँ कुछ [sample profiles](https://gist.github.com/kitswas/b7a100954de7dd7dcbe52cd38a27c8cf) पा सकते हैं।

## Laggy/unresponsive महसूस होता है

Server आपके inputs पर्याप्त तेज़ी से receive नहीं कर रहा है।  
यह अलग-अलग solutions वाले दो अलग-अलग issues का common symptom है।

$$\text{Max response time} = \text{Network delay} + \text{Polling interval}$$  
$$ \text{Min response time} = \text{Network delay}$$

_Processing time negligible है। मैंने यह पता लगाने के लिए दोनों apps में (v0.3.0 का उपयोग करके) measure किया।_

### High polling interval

Mobile app gamepad state को fixed intervals पर sample लेता है।  
आप इसे app settings में बदल सकते हैं।

कम polling interval gamepad को अधिक responsive महसूस कराएगा, लेकिन इससे network traffic और battery usage भी बढ़ेगी।

दूसरी ओर, higher polling interval के साथ combos pull off करना आसान है।

### High latency (अक्सर मुख्य culprit)

सरल शब्दों में, इसका मतलब है कि network delay बहुत अधिक है।

यहाँ मैंने जो observe किया है (2.4GHz Wi-Fi पर):

1. **Direct connection (फ़ोन या PC पर Hotspot)** सबसे कम latency है (< 5ms)
2. **एक ही कमरे में Router** कम latency है (5-20ms)
3. पड़ोसी का router / अलग कमरे में router की latency अधिक है (20-50ms)
4. Enterprise networks में सबसे अधिक latency होती है

Best experience के लिए 1 या 2 का उपयोग करें।  
_5GHz WiFi band बेहतर performance provide कर सकता है।_

## आपने [cool upcoming features](Roadmap.md) का mention किया। वे कब available होंगे?

जैसे ही मेरे पास इस पर काम करने का समय होगा। :)  
अगर आप उन्हें जल्दी चाहते हैं, तो आप _project में contribute_ कर सकते हैं।

## Help प्राप्त करें

### सवाल हैं?

- Existing issues check करें - हो सकता है किसी ने पहले ही पूछ लिया हो
- General questions के लिए एक [Discussion](https://github.com/kitswas/VirtualGamePad/discussions) शुरू करें
- Specific problems के लिए एक issue create करें

### Chat करना चाहते हैं?

अभी, GitHub Discussions हमारी बात करने की main जगह है। हम बाद में Discord add कर सकते हैं जब हमारे पास moderate करने में मदद करने के लिए अधिक लोग होंगे।

## Bug reports और feature requests?

[Contributing guide](Contributing.md#-how-to-report-issues) देखें।

### Bonus XKCD Comic

Bugs fix करना:

![XKCD 1739](https://imgs.xkcd.com/comics/fixing_problems.png)

> 'वह original problem क्या थी जिसे आप fix करने का प्रयास कर रहे थे?' 'Well, मैंने देखा कि जिन tools का मैं उपयोग कर रहा था उनमें से एक में inefficiency थी जिससे मेरा समय waste हो रहा था।'
> — [XKCD 1739](https://xkcd.com/1739/)
