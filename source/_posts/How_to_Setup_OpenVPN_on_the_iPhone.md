title: How to Setup OpenVPN on the iPhone
author: zxy
tags:
  - VPN
  - PROXY
  - SOCKS
  - IOS
categories:
  - Technology application
date: 2019-09-30 12:41:00
---
## Background

This lesson demonstrates how to configure the iOS OpenVPN client to authenticate with certificates and configure the SOCKS proxy.

## Prerequisites

- Device with iOS 9.0 and up
- Internet connectivity and Apple ID to access App Store and download OpenVPN application.
- Hosted a .pac file on a Web Server

> On iOS is possible to create TUN tunnels only, as TAP tunnels are not supported by the operating system itself. For more information, please refer to [OpenVPN iOS client FAQs](https://docs.openvpn.net/connecting/connecting-to-access-server-with-apple-ios/faq-regarding-openvpn-connect-ios/#Why_doesnt_the_app_support_tap-style_tunnels). The [OpenVPN server instance](https://help.endian.com/hc/it/articles/218145318-Set-up-of-a-VPN-Server-Instance) has to be configured to use TUN device.

## Step by Step Tutorial

### OpenVPN Connect Setup

1. Open iTunes on your computer, connect your iPhone or iPad, click on "File Sharing" and select "OpenVPN". Then click on "Add...".
![upload successful](openvpn-0.png)</br>

2. Download the [OpenVPN configuration file](https://member.hide.me/en/server-status), unzip it and select the .ovpn file. Then click on "Add".
![upload successful](openvpn-1.png)</br>

3. Install the profile in OpenVPN Connect, for that click on the green plus button.
![upload successful](openvpn-2.png)</br>

4. Enter your login credentials and click on the "Add" button. Optionally you can save your password.
![upload successful](openvpn-3.png)
A dialog window will open asking you to allow the OpenVPN iOS application to add a VPN configuration to the system. This is a default warning message advising you that your network connection will be redirected over the VPN and you can safely tap "Allow".
![upload successful](openvpn-4.png)</br>

5. When activating the connection, a dialog window will ask you to confirm that you want to enable the connection to VPN. Confirm with "Yes".
![upload successful](openvpn-5.png)</br>

6. If connection has been successfully established, the status is shown in the menu bar. You can manage your VPN connection with the OpenVPN app.
![upload successful](openvpn-6.png)</br>

7. Afterwards you can easily access that profile by clicking on "OVPN Profile" in "OpenVPN Connect" app.
![upload successful](openvpn-7.png)</br>

### SOCKS proxy Setup

1. Open up **settings > wifi**.

2. Click on the **blue arrow** next to your wifi connection.

3. Scroll to the bottom where there is a section for **HTTP Proxy**.

4. Select **Auto** from this section.

5. In the URL field, key in the URL of the *.pac file you created and made web-accessible.

## Reference

1. [OpenVPN](https://en.wikipedia.org/wiki/OpenVPN)

2. [SOCKS](https://en.wikipedia.org/wiki/SOCKS)

3. [Proxy_auto-config](https://en.wikipedia.org/wiki/Proxy_auto-config)

4. [如何下载OpenVPN](http://www.capjsj.cn/ios_openvpn.html)

5. [How To Use a .pac File in iOS](https://www.amsys.co.uk/how-to-use-a-pac-file-in-ios/)

6. [How to Setup OpenVPN on iPad / iPhone](https://hide.me/en/vpnsetup/ios/openvpn/)

7. [How To Configure IOS OpenVPN Client With Certificate Authentication](https://help.endian.com/hc/it/articles/360008350974-How-to-configure-iOS-OpenVPN-client-with-certificate-authentication)

8. [How to connect an iOS device to your computer via a SOCKS proxy](https://gist.github.com/austinhappel/5614113)
