---
description: |
  A roadmap for the Virtual GamePad system, detailing planned features, ongoing experiments, and future considerations.
---

# Roadmap

Every line of code is a liability.

Before making changes, I ask myself:

1. Is the app unusable or extremely inconvenient without this feature? How many people does it affect?
2. Will it be easy to maintain in the long run? **An app with less features is better than an abandoned one.**
3. Is it worth the time and effort to implement?
4. Does it negatively affect security or performance?

I mostly work on this during my college breaks. (1-4 releases yearly)

- this list will be replaced by the table of contents
{:toc}

## Not Planned

Won't be implemented in the foreseeable future.

- Bluetooth as a connection mode.
- Support for multiple clients with a single server. See [this issue](https://github.com/kitswas/VirtualGamePad-PC/issues/8).

## Ongoing Experiments

These are experiments to determine feasibility and potential implementation paths.  
They may or may not lead to a feature in the future.

- True Gamepad input with `winrt::Windows::UI::Input::Preview::Injection::InputInjector`.
- Linux support - Both Keyboard/Mouse and Gamepad input modes.  
  See [tracking issue](https://github.com/kitswas/VirtualGamePad-PC/issues/9).  
  **Completed. Need to test some more and fix the packaging.**

## Planned

I want to try doing these when I have time.

- Symmetric Key Encryption on the sockets.  
  A random key can be generated on the server for each session. We already have a secure way to share the key. _(The user can scan the QR code or type the key.)_  
  The real questions are  
  1. Is it necessary?
  2. What will it cost in terms of performance?

- Adding the two triggers to the gamepad layout.  
  - Need to determine the position of the triggers on the screen. (Mobile app)  
  - Handle the input on the server side. (PC app)
  - The data exchange format does not need changes.

## Bonus XKCD Comic

Code Lifespan:

![XKCD 2730](https://imgs.xkcd.com/comics/code_lifespan_2x.png)

> Surely (no one/everyone) will (recognize how flexible and useful this architecture is/spend a huge amount of effort painstakingly preserving and updating this garbage I wrote in 20 minutes)
> — [XKCD 2730](https://xkcd.com/2730/)
