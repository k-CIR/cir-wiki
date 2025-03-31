---
title: Connect to server
tags: [server, connect]
---

## Prerequisites

- Activate [KI VPN](https://staff.ki.se/tools-and-support/it-and-telephony/tools-for-working-off-campus/vpn-service-ki-vpn)
- Server address: `compute.kcir.se` (193.10.16.5)

## SSH connection
/// tab | Windows
Use Windows PowerShell or PuTTY

Basic connection command:
  ```
  ssh <username>@compute.kcir.se
  ```
/// 

/// tab | MacOS/Linux
Open a new terminal window and type: `ssh <username>@compute.kcir.se`, where `username` is your personal username. Enter your password when asked. You are now connected to the CIR computing server.

## Mac ssh connection with X11 forwarding

Install XQuartz for Mac: [Download from XQuartz Official Site](https://www.xquartz.org/)

  ```
  ssh -X <username>@compute.kcir.se
  ```

The -X flag enables X11 forwarding: it allows you to run graphical applications remotely.
/// 

### Troubleshooting
If you get the following error:
`no matching host key type found. Their offer: ssh-rsa,ssh-dss`

Add the following lines to your `.ssh/config`-file:

```bash
HostKeyAlgorithms ssh-rsa
PubkeyAcceptedKeyTypes ssh-rsa
```

If you encounter the following host key error: 
`no matching host key type found. Their offer: rsa-sha2-512,rsa-sha2-256,ecdsa-sha2-nistp256,ssh-ed25519` , try:
  ```
  ssh -oHostKeyAlgorithms=+ssh-rsa <username>@compute.kcir.se
  ```

## File transfer (SFTP)

### Recommended tool: FileZilla
1. Download [FileZilla](https://filezilla-project.org/)
2. Configure SFTP:
    * Protocol: SFTP
    * Host: `compute.kcir.se`
    * User: Your provided username
    * Password: Your server password

![SFTP configuration]({{ picture_path }}/username_filezilla.png)
/// caption
SFTP configuration for FileZilla.
///

## Remote Desktop (xRDP)
A graphical desktop environment is installed on the CIR server. 
### Windows
- Use Windows **Remote Desktop Connection**
- Server IP: `compute.kcir.se`

### Mac
- Download Remote Desktop from App Store: [Windows App](https://apps.apple.com/us/app/windows-app/id1295203466?mt=12)

![RDC_clientwindow]({{ picture_path }}/RDC_clientwindow.png)
/// caption
RDC client window.
///


### Connection Tips
To access the server, enter the server **IP address** in the *Computer field* of the remote desktop connection client and press *connect*. 
If you click on the button **‘Show Options’** you can access more advanced configuration. 

It is recommended that you save your settings, for example on your desktop, so you don’t have to type in the IP address every time you wish to connect. 
There is also an option to save your login information so you don’t have to enter the information every time you connect.

### Recommended Settings

#### First-Time xRDP Login

When you login for the first time using xRDP, you will see the following screen:

![xRDP login screen]({{ picture_path }}/xrdp_login.png)
/// caption
xRDP login screen.
///
- Type in your username and password and press enter (or click ok). If successful, you will be connected to the desktop.
- Select English as preferred language

![welcome screen]({{ picture_path }}/welcomescreen.png)
/// caption
Welcome screen of the desktop. 
///

Click on the top corner of the screen to access the quick access bar. You can unpin programs from the quick access bar by right-clicking on the icons. 
In a similar way, you can also pin program icons that you find when using the search option to your quick access bar.

![quick access bar]({{ picture_path }}/quick_access_bar.png)
/// caption
Quick access bar.
///

You can customize your desktop layout and settings by right clicking somewhere on the desktop space and select *display settings*.

![customize layout]({{ picture_path }}/display_settings.png)
/// caption
Display settings.
///

It is recommended that you **disable the screen lock** feature in **Settings -> Privacy & Security**. 
This way you won’t be prompted for a password when you leave the desktop session inactive (this security feature is essentially redundant when using a remote connection).

![PrivacySecurity settings]({{ picture_path }}/privacy_security_settings.png)
/// caption
Privacy & Security settings panel.
///

#### Optimizing the xRDP session

The RDP protocol has been optimized to work as efficiently as possible on the server side. 
However, due to connection latency and other issues that are outside of our control, you may wish to consider adjusting 
a few settings in the RDP client to make sure you get the most comfortable experience.

Settings to adjust:
- **Color depth**: Set color depth to 15-bit for best performance

![Color depth]({{ picture_path }}/color_depth.png)
/// caption
Color bit depth.
///

- **Connection speed**: Ensure that you selected **LAN 10Mbit >** setting in the **Experience tab**. This will enable compression protocols for your RDP session.

![Connection speed]({{ picture_path }}/LAN10.png)
/// caption
Performance settings.
///