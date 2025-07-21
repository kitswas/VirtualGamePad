---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''

---

**What happened**
Describe the problem

**What you expected**
What should have happened instead

**To Reproduce**
Steps to make it happen again:

1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Your setup**  

**Desktop (please complete the following information):**

- OS: [e.g. Windows 11, Linux]
- Server Version: [e.g. 0.3.0]

**Smartphone (please complete the following information):**

- Device: [e.g. Samsung Galaxy M21]
- OS: [e.g. Android 12]
- App Version: [e.g. 0.3.3]

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Log Files (Optional, but helpful)**
Attach `.log` files from the same folder as `VGamepadPC.exe`.

**Additional context**
Add any other context about the problem here.

Example good bug report:

> **Title**: "Virtual buttons gets stuck on Samsung Galaxy M21"
>
> **Description**: When I press a button, sometimes it gets stuck in the 'pressed' position and my character keeps moving even after I let go.
>
> **Steps to reproduce**:
>
> 1. Open the Android app on my phone
> 2. Connect to my PC
> 3. Start playing any game
> 4. Use the arrow keys to move around
> 5. After a few minutes, it gets stuck
>
> **Workaround**: Press the button again to unstick it
>
> **My setup**:
>
> - Samsung Galaxy M21, Android 12
> - PC running Windows 11
>
> **Screenshot**: [attached]

[This was a real bug which was fixed](https://github.com/kitswas/VirtualGamePad-PC/commit/eb681a793872465eda68b62fa2623e2f4329a8b3).  
Notice that while the problem seemed to be with the Android app, it was actually a bug in the PC server.
