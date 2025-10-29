---
title: Download your data
---

To download your data from SPICE to your local machine, you can use an SFTP (Secure File Transfer Protocol) client. Below are instructions for using the recommended tool, FileZilla.

1. Download and install the [FileZilla client](https://filezilla-project.org/)

2. Open FileZilla and open the Site Manager (File -> Site Manager).

![VScode-extensions]({{ picture_path }}/filezilla1.png){ width="500" }
/// caption
The Site Manager in FileZilla.
///

3. Create a new site with the following settings:
    * Protocol: SFTP - SSH File Transfer Protocol
    * Host: `compute.kcir.se`
    * Port: Leave blank (default is 22)
    * Logon Type: Normal
    * User: Your provided username
    * Password: Your server password

4. Click "Connect" to establish the connection to SPICE. The first time you connect, you may be prompted to accept the server's host key. Click "OK" to proceed.

FileZilla will now connect to SPICE, and you will see your local files on the left side and the remote server files on the right side. Generally, data connected to your project are stored in the `/data/projects/<project_name>/` directory on SPICE or your home directory (`/data/users/<username>/`).

If you are new to using FileZilla, the interface can be a bit confusing, but the basics are straightforward:

![VScode-extensions]({{ picture_path }}/filezilla2.png){ width="500" }
/// caption
The FileZilla interface.
///

1. Use the top left pane to navigate your local files.
2. Use the top right pane to navigate the remote server files.
3. The bottom right pane shows the contents of the selected remote directory.
4. The bottom left pane shows the contents of the selected local directory.

Right click -> Download, or drag and drop files and folders from the right pane (remote) to the left pane (local) to download files from SPICE to your local machine. Similarly, you can upload files by dragging and dropping from the left pane to the right pane.
