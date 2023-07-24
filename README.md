# VirtualGamePad

VirtualGamePad lets you use your Android phone as a gamepad for your Windows PC.  
It's similar to DroidJoy, but free and open source.

## Screenshots

VirtualGamePad running on an Android 12 device:

![VirtualGamePad](VGP.svg)

![VirtualGamePad Dark](VGP_night.svg)

VirtualGamePad Server running on Windows 11:

![VirtualGamePad Server](VGP_Server.png)

## Installation

To use VirtualGamePad, you need to install the Android app (client) on your phone and the Windows app (server) on your PC.

### Android

Grab the latest APK from the [releases page](https://github.com/kitswas/VirtualGamePad-Mobile/releases) and install it on your phone.

### Windows

Grab the latest archive(.zip) from the [releases page](https://github.com/kitswas/VirtualGamePad-PC/releases), extract it and run `VGamepadPC.exe`.

## Usage

Run the server on your PC and the client on your phone.  
Connect to the server from the Android app by entering the IP address and port of the server.  
Both devices need to be on the same network.

## Troubleshooting

If you're having trouble connecting to the server, try disabling your firewall or adding an exception for the server.  
On Windows, you will be prompted to allow the server to communicate through the firewall when you run it for the first time.

![Firewall](VGP_UAC_Dialog.png)

If you're still having trouble, start a hotspot on your phone and connect your PC to it.  
Then, restart the server and try connecting again.

The built-in QR code scanner might stop working after a while. This is a known issue and caused by a bug in the Google library used for scanning. Clear the data for Google Play Services to fix it. Or use a third-party QR code scanner.

