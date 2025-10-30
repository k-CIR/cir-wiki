---
title: Tips for using VScode
---

## Login without password
You can set up [an SSH key pair in VScode](https://code.visualstudio.com/docs/remote/ssh#_using-ssh-keys) to avoid having to enter your password every time you connect. To do this, you need to generate an SSH key pair (one private and one public key) on your local machine and add the public key to the `~/.ssh/authorized_keys` file on SPICE.

!!! warning "SSH key security"
    An SSH key-pair provide the same access to SPICE as your username and password, so keep your private key (file) secure and do not share it with anyone. The key is saved on your local machine, make sure it is at least as secure as you need your access to SPICE to be.

First, generate an SSH key pair on your local machine:

/// tab | Local Windows
Use Windows PowerShell or [Git Bash](https://git-scm.com/downloads) and run:
  ```
  ssh-keygen -t ed25519 -C "youremail@mail.com"
  ```

You will be prompted to enter a file in which to save the key. You can press enter to accept the default location. You will also be prompted to enter a passphrase, which is optional and defeats the purpose of setting up SSH keys without password. Press enter to continue without a passphrase.

Go to the file where the key was saved (default is `C:\Users\yourusername\.ssh\`) and open the file `id_ed25519.pub` with a text editor. This is the public part of your SSH key-pair. Copy the entire contents of the file to your clipboard.

Now, you will have to put the public key in: `~/.ssh/authorized_keys` in your home directory on SPICE.

Already connected to SPICE, paste the key by running the following terminal command:
  ```
  echo "paste the contents of your clipboard here" >> ~/.ssh/authorized_keys
  ```

/// 

/// tab | Local Linux/macOS
Use the terminal and run:
  ```
  ssh-keygen -t ed25519 -C "youremail@mail.com"
  ```

You will be prompted to enter a file in which to save the key. You can press enter to accept the default location. You will also be prompted to enter a passphrase, which is optional and defeats the purpose of setting up SSH keys without password. Press enter to continue without a passphrase.

**Option 1 - Using ssh-copy-id (recommended):**
Now, copy the public key to SPICE using `ssh-copy-id`:
  ```
  ssh-copy-id -i ~/.ssh/id_ed25519.pub yourusername@compute.kcir.se
  ```
You will be prompted to enter your SPICE password one last time. After this, the key will be automatically added to `~/.ssh/authorized_keys` on SPICE and you can connect without a password.

**Option 2 - Manually copy the key:**
Go to the file where the key was saved (default is `~/.ssh`) and open the file `id_ed25519.pub` with a text editor. This is the public part of your SSH key-pair. Copy the entire contents of the file to your clipboard.

When connected to SPICE, paste the key by running the following terminal command:
  ```
  echo "paste the contents of your clipboard here" >> ~/.ssh/authorized_keys
  ```
/// 

## Version control with Git
Using [Git](https://git-scm.com/) for version control is highly recommended when working with code. VScode has built-in support for Git and makes it easy to manage your repositories and compare changes.

## AI assisted coding
Use the github copilot extension in VScode for AI assisted coding. This can help you write code faster and with fewer errors. See the [GitHub Copilot documentation](https://docs.github.com/en/copilot/getting-started-with-github-copilot/about-github-copilot) for more information on how to use it.

![VScode-extensions]({{ picture_path }}/github_copilot.png){ width="500" }
/// caption
The github copilot extension in VScode.
///



