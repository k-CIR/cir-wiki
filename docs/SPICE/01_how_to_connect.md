---
title: How to connect
---

If you already have a user account on SPICE and received access to a new project, you need to log out and back in <br>again with: `pkill -u yourusername` for your permissions to be updated.

On your first connection to SPICE you will be prompted to change your password and set up two-factor authentication (TOTP). See the [New user guide](02_new_user.md) for detailed instructions on how to do this.

## Terminal access
Open a terminal (Linux/macOS) or Command Prompt (Windows):material-help-circle-outline:{ .hint title="Press ⊞ + R on your keyboard, type cmd and press Enter to open" }

    ssh yourusername@compute.kcir.se

You are prompted for your password and then a 6-digit code from your authenticator app. Enter these correctly and you are in!

## SSH key access
Make your life easier by setting up SSH key access to SPICE. This way you won't have to enter your password and 6-digit code every time you log in. To do this, you need to generate an SSH key pair on your local machine and add the public key to your SPICE account.

It's called a key-pair, but really you can think of it as a lock (public key) and a key (private key). You generate a key pair, put the lock (public key) on the service you want to access and keep the key (private key) on your local machine. When you connect, the server checks if you have the right key to unlock the lock.

!!! warning "SSH key security"
    An SSH key-pair provide the same access to SPICE as your username and password+TOTP, so keep your private key (file) secure and do not share it with anyone. The key is saved on your local machine, make sure it is at least as secure as you need your access to SPICE to be.

First, generate an SSH key pair on your local machine by running this command, with your email address, in your terminal:

  ```
  ssh-keygen -t ed25519 -C "youremail@mail.com"
  ```

You will be prompted to enter a file in which to save the key. You can press enter to accept the default location, but should pay attention to where on your local machine the key will be saved. You will also be prompted to enter a passphrase, which is optional and defeats the purpose of setting up SSH keys without password. Simply press enter to continue without a passphrase.

Your computer runs an SSH agent in the background that keep tracks of your keys. Add your new key to the SSH agent by running this command:

/// tab | Windows
in git bash:
```sh
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```
///

/// tab | Mac

```sh
eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```
///

/// tab | Linux

```sh
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```
///

??? warning "~/.ssh/id_ed25519 already exists - Overwrite?"

    If you have created other SSH keys on your machine (e.g. for github or accessing other servers) you may already have a key-pair with the standard name `id_ed25519` and `id_ed25519.pub`. You will then encounter a warning that says:

        /home/you/.ssh/id_ed25519 already exists.
        Overwrite (y/n)?

    In this case, you can either overwrite the existing key-pair (not recommended) or save the new key-pair with a different name, e.g. `id_ed25519_spice` and `id_ed25519_spice.pub`. To keep track of which key is used for which service, use a descriptive name for the key-pair. Create a config file for your SSH client to tell it which key to use for SPICE. Create a file called `config` (no file extension, edit in any text editor) in the same folder as your keys and add the following lines, replacing the placeholder with your username and `id_ed25519_spice` with the name of your key-pair:

        Host yourusername-SPICE
            HostName compute.kcir.se
            User yourusername
            IdentityFile ~/.ssh/id_ed25519_spice
            IdentitiesOnly yes

    With this config file in place, you connect to SPICE with the command `ssh yourusername-SPICE` instead of `ssh yourusername@compute.kcir.se`. You can include as many `Host` entries in the config file as you want, for example if you have multiple key-pairs for different services. This way you explicitly tell your SSH client which key to use for which service instead of it trying all keys in your SSH agent until it finds one that works.

Go to the file where the key was saved (default is `~\.ssh\`) and open the file `id_ed25519.pub` with a text editor. This is the public part of your SSH key-pair, your private, top-secret, key will be in the file `id_ed25519`. Copy the entire contents of the public `id_ed25519.pub` file to your clipboard.

In a terminal, logged in to SPICE, run the command:
    
    my-SPICE-keys

This will open an interactive menu that you can use to add your public key to your SPICE account.

![My SPICE Keys]({{ picture_path }}/my-SPICE-keys1.png){ width="600" }
/// caption
The interactive menu of the `my-SPICE-keys` command. You can add, remove and list your SSH keys here. Here the user *cirtest3* is adding a new key to key slot 1 and naming it "HP-laptop".
///

You may be used to storing public keys in the `~/.ssh/authorized_keys` file on the server. Now, the `my-SPICE-keys` command is used to manage your keys centrally. Your keys are stored in the same authentication system that manages your username, password and TOTP. This is a security measure that allows CIR to limit the number of keys per user, revoke keys if they are compromised and retire old keys.

Each user can have up to 3 keys simultaneous keys, i.e. access SPICE via SSH from up to 3 different devices. Keys are retired after 1 year, but you can add/update a new key at any time. If a key expires you simply have to log in with your username and password+TOTP and add a new key to your account.

![My SPICE Keys]({{ picture_path }}/my-SPICE-keys2.png){ width="600" }
/// caption
The my-SPICE-keys command will show you a list of your keys and their expiration date. Here the user *cirtest3* has 1 key that expire 2027-09-27. 
///

## Remote desktop access
Before the proccess of opening SPICE to external users is completed remote desktop has to be accessed via a remote SSH tunnel you set up yourself. To open the tunnel, open a terminal **on your local machine** and run this command, replacing `yourusername` with your SPICE username:

    ssh -L 8443:127.0.0.1:443 yourusername@193.10.16.5

Once logged in, go to [https://localhost:8443/spice/](https://localhost:8443/spice/) in your local browser and log in to the remote desktop with your SPICE credentials.

Once the migration of SPICE is complete, you will be able to access the remote desktop directly via https://spice.kcir.se without having to set up a tunnel. But sometimes you have to make things a little more complicated to make them a lot simpler in the long run, thank you for your patience!

![My SPICE Keys]({{ picture_path }}/thunar.png){ width="400" }
/// caption
The first time you navigate on the remote desktop you will be prompted to select a default file manager. We recommend the faster more lightweight Thunar file manager.
///

## Change password/TOTP
Logged in to SPICE, you can change your password interactively with the command `passwd`. This does **not** change your TOTP, but you can reset your TOTP by running the command `reset-totp`. This will generate a new QR code that you can scan with your authenticator app to set up a new TOTP.
