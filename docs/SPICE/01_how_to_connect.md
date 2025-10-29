---
title: How to connect
---

To get access to SPICE you need to be a member of a research group that has an active project at CIR. Fill out the [the webform on the KI web page](https://ki.se/en/research/research-areas-centres-and-networks/research-centres/centre-for-imaging-research-cir/request-to-access-the-cir-server)  to request a new user account. Access is granted after approval by the projects PI. Your user credentials (username and password) will be sent to you in the email address you provided in the form.

!!! warning "Password security"
    Your first course of action after receiving your credentials should be to change your password to something only you know. Use the command `passwd` after logging in for the first time and follow the prompts.

    Obviously - create a unique and strong password that you do not use anywhere else and never share your password with anyone. Best practice is to use a [password manager](https://staff.ki.se/tools-and-support/it-and-telephony/accounts-and-passwords#heading-6) to generate and store strong passwords.

## Connecting to SPICE
There are three ways to connnect to SPICE using secure shell ([SSH](https://en.wikipedia.org/wiki/Secure_Shell)).

- In a terminal, useful for running occasional commands or processing jobs from command line.
- Using an [Integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment), like [VScode](https://code.visualstudio.com/) or [Spyder](https://www.spyder-ide.org/). This is useful for editing code (with AI assistance), developing analysis and running scripts. Preferred for most tasks and the recommended way to work with SPICE.
- Using a remote desktop client, useful if you need to use a graphical interface on the server.

!!! note "KI VPN"
    You have to be connected to the [KI VPN](https://staff.ki.se/tools-and-support/it-and-telephony/tools-for-working-off-campus/vpn-service-ki-vpn) to access SPICE.

## In terminal
Open a Terminal (Linux/macOS) or Command Prompt (Windows). Note,  windows _power shell_ does not support SSH by default, seach for `cmd` or `command prompt` in the start menu to find the correct application.

With your username, type the following command:
  ```
  ssh <username>@compute.kcir.se
  ```

Enter your password when asked. You are now connected to the CIR computing server, located in your home directory.

### First time?
The first time you connect to the server, you will be asked to confirm the server's fingerprint:

```
The authenticity of host 'compute.kcir.se (193.10.16.5) can't be established.
ECDSA key fingerprint is SHA256:...
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Type `yes` and press enter to continue.

## Connecting in VsCode
1. Install [Visual Studio Code](https://code.visualstudio.com/) and the extension: Remote - SSH.

![VScode-extensions]({{ picture_path }}/vscode_extensions.png){ width="500" }
/// caption
Navigate to the extensions tab in VScode, search for and install the extension "Remote-SSH".
///

2. You can now go to the Remote Explorer tab in VScode and add a "new remote".

![VScode-extensions]({{ picture_path }}/remote_explorer.png){ width="500" }
/// caption
Add new remote in the remote explorer tab.
///

3. Enter the SSH connection command, your username and the remote adress like: `ssh <username>@compute.kcir.se`
4. Choose the SSH configuration file to update (usually the default is fine).
5. "compute.kcir.se" will now show up in the list of configured remotes. Click the arrow to connect in current window.
6. The first time you connect, you are prompted for the platform of the remote host, choose Linux. 
7. You are prompted for your password, enter it and press enter.

You are now connected to SPICE and can open folders, files and run code on the server. Open a terminal by going to Terminal -> New Terminal or open a folder by going to File -> Open Folder.

Finally, be sure to check out the [tips for using VScode](./02_Vscode_tips.md) to be more productive and make your life easier.

## Using remote desktop
Using a remote desktop client is useful if you need to use a graphical interface on the server but is generally a bit more clunky than using VScode or a terminal. If your connection is slow, try lowering the display resolution and color depth in the remote desktop client settings.

Most windows installations have the Remote Desktop Client pre-installed. On macOS, download the "Windows App" from the [App Store](https://apps.apple.com/us/app/microsoft-remote-desktop/id1295203466?mt=12).

![VScode-extensions]({{ picture_path }}/remote_desktop.png){ width="500" }
/// caption
The Remote Desktop Client and login screen.
///

Open the Remote Desktop Client and create a new connection to `compute.kcir.se` or the server IP: `193.10.16.5`. Use your username and password when prompted.

!!! note "Log out to log in"
    If you previously logged in using terminal or VScode your user session may be active without a grapical interface. In this case, you need to log out from your active session before connecting with Remote Desktop. You can log out by running the command `pkill -u <username>` in a terminal where `<username>` is your SPICE username.


...