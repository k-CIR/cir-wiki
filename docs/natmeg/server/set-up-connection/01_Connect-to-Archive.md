---
title: Connect to Archive
---

# Connect to Archive

This is a guide on how to connect to NatMEG's archive server to access your data. To connect, you need a username and password for the server.

There are two options for connecting:

1. Using a FTP app like FileZilla client
2. Using command line  

## 1. Using FileZilla
Download the FileZilla client (https://filezilla-project.org) for the OS you are using and install it.

Connect to the sever with hostname: `archive.natmeg.se`, port: `22`, your username and password. You can now copy files from the server to your local machine.

## 2. Using command line
Connect to the server with `sftp username@archive.natmeg.se` and enter your password when prompted. 

You can view the files and folders in your current remote (i.e., on the server) directory with `ls`, view the current remote directory with `pwd`, and change it with `cd REMOTEPATH`. To do the same for your local directory (i.e., on your computer) use `lls`, `lpwd` and `lcd LOCALPATH`, respectively. You can download files with `get REMOTE [LOCALPATH]`. _REMOTE_ can be a file or folder. If you want to download an entire folder use `get -R REMOTE [LOCALPATH]`. If you do not specify _LOCALPATH_ the downloaded files will go to your current local directory.

## Known connection issues

You should not need to be connected to KI via VPN, but you are not able to connect via eduroam. Use another secure network.

If you get the following error:
`no matching host key type found. Their offer: ssh-rsa,ssh-dss`

Add the following lines to your `.ssh/config`-file:

```bash
HostKeyAlgorithms ssh-rsa
PubkeyAcceptedKeyTypes ssh-rsa
```
 