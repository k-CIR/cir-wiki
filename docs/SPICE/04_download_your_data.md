---
title: Download your data
---

To download your data from SPICE to your local machine, you can use the SFTP (Secure File Transfer Protocol) client. Download and install the [FileZilla client here](https://filezilla-project.org/).

The are two ways to download your data. Select either method A or B depending on your needs in setup step 3 below.

**A)** Quick and easy setup, with your password and TOTP, keeping one connection kept open for occasionally downloading up to ~10GB of data. <br>
**B)** Setting up FileZilla with your SSH key, which allows FileZilla to open multiple simultaneous connections which speed up the download of large datasets. This is the recommended method if you have a lot of data to download or need to download data frequently.

1. In both cases start by opening FileZilla and open the Site Manager (File -> Site Manager).

![Filezilla]({{ picture_path }}/filezilla1.png){ width="500" }
/// caption
The Site Manager in FileZilla.
///

2. Create a new site with the following settings:
    * Protocol: SFTP - SSH File Transfer Protocol
    * Host: `compute.kcir.se`
    * Port: Leave blank (default is 22)
    * User: Your provided username

3. **A)** Select `Logon Type: Interactive`. Go to the tab "Transfer Settings" and check "Limit number of simultaneous connections" and set the value to 1. This makes FileZilla prompt you for your password and TOTP when you connect, but keep it from opening parallel connections that force you to authenticate multiple times.

![Filezilla-prompt]({{ picture_path }}/FileZilla_totp.png){ width="500" }
/// caption
Pay attention to if FileZilla is asking for your password or TOTP (6-digit passcode from your authenticator app) when you log in. You are prompted for these separately.
///

3. **B)** See the guide on [how to connect using SSH keys](../01_how_to_connect/#ssh-key-access) for how to set up SSH key access. With your SSH key in place, select `Logon Type: Key file` and browse to the location of, and select, your private key file(e.g. `~\.ssh\id_ed25519`).

4. Click "Connect" to establish the connection to SPICE. The first time you connect, you may be prompted to accept the server's host key. Click "OK" to proceed.

FileZilla will now connect to SPICE, and you will see your local files on the left side and the remote server files on the right side. Generally, data connected to your project are stored in the `/data/projects/<project_name>/` directory on SPICE or your home directory (`/data/users/<username>/`).

If you are new to using FileZilla, the interface can be a bit confusing, but the basics are straightforward:

![Filezilla-2]({{ picture_path }}/filezilla2.png){ width="500" }
/// caption
The FileZilla interface.
///

1. Use the top left pane to navigate your local files.
2. Use the top right pane to navigate the remote server files.
3. The bottom right pane shows the contents of the selected remote directory.
4. The bottom left pane shows the contents of the selected local directory.

Right click -> Download, or drag and drop files and folders from the right pane (remote) to the left pane (local) to download files from SPICE to your local machine. Similarly, you can upload files by dragging and dropping from the left pane to the right pane.
