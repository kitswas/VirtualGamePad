
# Troubleshooting

If your problem is not covered here, [file an issue](https://github.com/kitswas/VirtualGamePad/issues/new/choose).

## Help! I cannot connect to the server

If you're having trouble connecting to the server, try disabling your firewall or adding an exception for the server.  
On Windows, you will be prompted to allow the server to communicate through the firewall when you run it for the first time.

![Firewall](assets/VGP_UAC_Dialog.png)

**If you're still having trouble, start a hotspot on your phone and connect your PC to it.** (or vice-versa, try both)  
Then, restart the server and try connecting again.

_Do this before complaining about the app not working._

## Help! The QR code scanner doesn't work

[Google code scanner](https://developers.google.com/ml-kit/vision/barcode-scanning/code-scanner) is an optional module in Google Play Services. It's fast but the delivery is unreliable when installing apps from outside the Play Store.

Update to [Mobile app version 0.3.0](https://github.com/kitswas/VirtualGamePad-Mobile/releases/tag/v0.3.0) or later.
The app will now guide you through downloading and installing the required module directly in-app.

> [!IMPORTANT]  
> Google Play Services is required.

## Help! The Gamepad doesn't work for a game

If it is a newer title with built-in support for Gamepads on PC, you might face some problems.  
Try running the server as admin. 🛡️

**The game should not be running as admin.** This prevents input injection.

Games without gamepad support should work out of the box.

Read [How it works](https://kitswas.github.io/VirtualGamePad-PC/#how-it-works) to know why.

## Help! The gamepad feels laggy/unresponsive

This is covered in [the FAQ.](FAQ.md#feels-laggyunresponsive)
