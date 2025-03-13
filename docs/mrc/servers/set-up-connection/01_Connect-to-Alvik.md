---
title: Connect to Alvik
---

# Connect to Alvik
This is a guide on how to connect to MR Center's computational server for data analysis. To connect, you need a username and password for the server.

As a user you can only connect to Alvik and your home directory will be `/data/myuser`.

To **connect to the server**, you must be on the **KI network** either via a wired connection or by using [FortiClient](https://staff.ki.se/tools-and-support/it-and-telephony/tools-for-working-off-campus/vpn-service-ki-vpn).

## Connect to Alvik with TurboVNC
Running VNC has the advantage of giving you the whole desktop of Alvik and to allow you to shut down your laptop or desktop while keeping your batch running on the server.
1. **Download** and **install** the software here: [TurboVNC](https://www.turbovnc.org/)
2.  Make a new **TurboVNC connection**. Write your <mark style="color:purple;">**username**</mark> followed by **@193.10.16.82:**

![]({{ picture_path }}/mrcturboVNC_login.png)

1. Click "**Connect**," and you will be prompted to enter your **password**.

### Setup TurboVNC on Windows ?


## Connect to Alvik via Terminal

You can log in to Alvik via terminal with the following command:

`ssh`<mark style="color:purple;">`<username>`</mark>`@193.10.16.82`

# Data transfer

The transfer protocol for copying/reading files to/from Alvik is **sftp**. Simple ftp is not allowed. 

This is a guide on how to transfer data from or to Alvik using the terminal or via Filezilla

## Using Filezilla

1. **Download** and **install** the [FileZilla client](https://filezilla-project.org) for your OS.
2. Connect to the server with the following settings: \
   **Hostname**: `193.10.16.82`, **port**: `22`, your **username** and **password**. \
   Once connected, you can upload or download files between Alvik and your local machine.

## Using the terminal

1. **Connect** to the server with sftp:

&#x20;`sftp _username_@193.10.16.82` and enter your password when prompted.

2. To **download data** from Alvik to your computer, you can use the following command:

`get -r <remote_directory> <local_directory>`

3. To **upload data** to Alvik from your computer, you can use the following command:

`put -r <local_directory> <remote_directory>`
