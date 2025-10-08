---
description: |
  Contribution guide for VirtualGamePad
---

# Contributing to VirtualGamePad

Welcome to the VirtualGamePad project! We're building a virtual gamepad that lets you use your Android phone as a game controller for PCs, and **we need YOUR help** - whether you're a gamer or someone who just wants a better way to play games.

- this list will be replaced by the table of contents
{:toc}

## 🎮 Who We Need

**You don't need to be a programmer to help!** We especially need:

- **Gamers** who can test with real games
- **Mobile users** testing on different Android devices
- **Anyone** who finds bugs or has ideas

## 🚧 Project Status

**Heads up**: This project is changing fast! We're still figuring things out, so:

- Features might break between updates
- New stuff gets added regularly
- Your feedback directly shapes what we build next

Go see [the roadmap](Roadmap.md).

## ⚠️ What to Expect

**The Reality:**

- I'm the only maintainer right now, so responses might take a week or two
- Things break sometimes (we're still figuring it out!)
- Your idea might not get implemented immediately
- But every bug report and suggestion helps make this better!

## 🎯 Our Goal

We want VirtualGamePad to be the **easiest, lightest, most reliable way** to use your phone as a game controller. Your testing and feedback is what gets us there!

## 🤝 How YOU Can Help (No Coding Required!)

### Find and Report Bugs

*This is HUGE for us!*

- Try to break things (seriously!)
- Test with your favorite games
- Try weird button combinations
- Test on different Android devices

**How to report**: [Create an issue](https://github.com/kitswas/VirtualGamePad/issues/new/choose) and tell us:

- What you were doing
- What went wrong
- What device you're using (phone model, Android version)
- Screenshots help a lot!

### Test on Your Devices

*We can't test everything ourselves!*

- Different Android phones/tablets
- Different screen sizes
- Older Android devices
- Any games that don't work well?

### Share Ideas

- How could we make it easier to use?
- What's confusing about the current setup?
- What features would make this awesome?

### Help Others

- Answer questions in [Discussions](https://github.com/kitswas/VirtualGamePad/discussions)
- Share tips and tricks you discover
- Help other users with setup problems

### Spread the Word

- Make videos showing it working
- Post about it on gaming forums, Reddit, Discord
- Tell your friends

## 🏗️ What Is VirtualGamePad?

It's actually 4 connected projects:

- **[VirtualGamePad](https://github.com/kitswas/VirtualGamePad)** - The project website and documentation
- **[VirtualGamePad-PC](https://github.com/kitswas/VirtualGamePad-PC)** - The PC (Windows or Linux) app that receives your inputs
- **[VirtualGamePad-Mobile](https://github.com/kitswas/VirtualGamePad-Mobile)** - Android app version
- **[VGP_Data_Exchange](https://github.com/kitswas/VGP_Data_Exchange)** - The behind-the-scenes communication code

*Don't worry about the technical details - just know that bugs could happen in any part!*

## 📋 How to Report Issues

Please open an issue on the Github issue tracker of the relevant repository:

- [VirtualGamePad-PC](https://github.com/kitswas/VirtualGamePad-PC/issues/new/choose)
- [VirtualGamePad-Mobile](https://github.com/kitswas/VirtualGamePad-Mobile/issues/new/choose)
- [VirtualGamePad Website](https://github.com/kitswas/VirtualGamePad/issues/new/choose)

If you are not sure which repository to use, just use the VirtualGamePad Website and I will move it to the right place.

## 🎮 Testing Help We Really Need

### Priority Testing Areas

1. **Device Testing**
   - Older Android phones
   - Different screen sizes

2. **Game Compatibility**
   - Steam games
   - Indie games
   - Emulators (Visual Boy Advance, RetroArch, Dolphin, etc.)
   - Browser games

3. **Child-Friendly Testing**
   - Is it easy for children to use?
   - Are instructions clear enough?

## 🔧 For Developers

If you DO code and want to help:

### Easy Starting Points

- Fix typos in documentation
- Improve error messages
- Verify reported bugs

### Setup Each Component

Each repository has its own README with setup instructions. Pick the one that matches your skills:

- **Desktop server**: VirtualGamePad-PC (C++/Qt)
- **Android client**: VirtualGamePad-Mobile (Kotlin/Android)

---

**Remember: Using VirtualGamePad and giving feedback IS contributing!**

You don't need to write a single line of code to make a huge difference. Every bug you find, every game you test, every suggestion you make helps build something awesome for the gaming community! 🎮

**Ready to help?** Start by [trying it out](https://kitswas.github.io/VirtualGamePad/#installation) and [let us know](https://github.com/kitswas/VirtualGamePad/issues) how it goes!
