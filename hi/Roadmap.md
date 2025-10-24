---
lang: hi
description: |
  Virtual GamePad सिस्टम के लिए एक roadmap, जिसमें planned features, ongoing experiments, और future considerations शामिल हैं।
layout: default
---

# Roadmap

AI-translated {: .ai-banner}

Code की हर line एक liability है।

Changes करने से पहले, मैं खुद से पूछता हूँ:

1. क्या इस feature के बिना app unusable या extremely inconvenient है? यह कितने लोगों को affect करता है?
2. क्या long run में इसे maintain करना आसान होगा? **कम features वाला app abandoned वाले से बेहतर है।**
3. क्या यह time और effort के लायक है implement करना?
4. क्या यह security या performance को negatively affect करता है?

मैं mostly अपने college breaks के दौरान इस पर काम करता हूँ। (सालाना 1-4 releases)

- this list will be replaced by the table of contents
{:toc}

## Not Planned

निकट भविष्य में implement नहीं किया जाएगा।

- Bluetooth को connection mode के रूप में।
- Single server के साथ multiple clients के लिए support। [यह issue](https://github.com/kitswas/VirtualGamePad-PC/issues/8) देखें।

## Completed

- Linux support - Keyboard/Mouse और Gamepad input modes दोनों।  
  [Tracking issue](https://github.com/kitswas/VirtualGamePad-PC/issues/9) देखें।  
  **Completed और released! Server अब Linux के लिए available है। Packaging improvements और आगे की testing जारी है।**
- Gamepad layout में दो triggers जोड़ना।

## Ongoing Experiments

ये feasibility और potential implementation paths determine करने के लिए experiments हैं।  
ये future में feature बन भी सकते हैं और नहीं भी।

- True Gamepad input के साथ `winrt::Windows::UI::Input::Preview::Injection::InputInjector`।  
  _Implemented है लेकिन कभी-कभी server start पर crash हो जाता है।_

## Planned

जब मेरे पास time हो तो मैं ये करने की कोशिश करना चाहता हूँ।

- Sockets पर Symmetric Key Encryption।  
  हर session के लिए server पर एक random key generate की जा सकती है। हमारे पास key share करने का पहले से ही एक secure तरीका है। _(User QR code scan कर सकता है या key type कर सकता है।)_  
  असली questions हैं  
  1. क्या यह necessary है?
  2. Performance के terms में इसकी cost क्या होगी?

## Bonus XKCD Comic

Code Lifespan:

![XKCD 2730](https://imgs.xkcd.com/comics/code_lifespan_2x.png)

> निश्चित रूप से (कोई नहीं/हर कोई) (यह recognize करेगा कि यह architecture कितना flexible और useful है/20 minutes में लिखे गए इस garbage को preserve और update करने में huge amount of effort खर्च करेगा)
> — [XKCD 2730](https://xkcd.com/2730/)
