---
title: Connect to Storage
---

# Connect to Storage

This is a guide on how to connect to NatMEG's storage server to access your home folder and shared data. To connect, you need a username and password for the server.

There are three options:

1. Using an SFTP app like FileZilla or Beyond-compare 
2. Using SFTP from command line
3. Using a samba file share 

## 1. Using FileZilla
Download the FileZilla client (https://filezilla-project.org) for the OS you are using and install it.

Connect to the sever with hostname: `storage02.natmeg.se`, port: `22`, your username and password. You can now copy files from the server to your local machine.

## 2. Using command line
Connect to the server with `sftp username@storage02.natmeg.se` and enter your password when prompted. 

You can view the files and folders in your current remote (i.e., on the server) directory with `ls`, view the current remote directory with `pwd`, and change it with `cd REMOTEPATH`. To do the same for your local directory (i.e., on your computer) use `lls`, `lpwd` and `lcd LOCALPATH`, respectively. You can download files with `get REMOTE [LOCALPATH]`. _REMOTE_ can be a file or folder. If you want to download an entire folder use `get -R REMOTE [LOCALPATH]`. If you do not specify _LOCALPATH_ the downloaded files will go to your current local directory.

## 3. Using a samba file share
Using samba you can map your home and shared folders from the server to your local computer. You need additional access from the core group for this so start by contacting them. 
Once you have samba access you can map a network drive with "\\storage02.natmeg.se\username" (Windows) or "smb://username@storage02.natmeg.se/" and your samba credentials . 

## Known connection issues

You need to be connected to the KI network via VPN.
 