---
title: VNC black screen error
tags: [troubleshooting]
---
You might experience a black screen with an error message when you first log in to a new VNC server.

![](https://github.com/natmegsweden/NatMEG_Wiki/blob/main/wiki_images/Fig_1-1.png)

![](https://github.com/natmegsweden/NatMEG_Wiki/blob/main/wiki_images/Fig_2-1.png)

The error seems to be due to Anaconda/Python initiation, which messes with the VNC config in some way. I have not been able to solve the problem definitly [if you know, please tell me! @mcvinding], but the following procedure circumvents the problem:

Open PuTTy to connect to Compute as [usual](https://github.com/natmegsweden/NatMEG_Wiki/wiki/Connect-to-Compute). Then in terminal edit .bash_profile (the file that is executed when you log in with SSH) so it does not call .bashrc (the file that is executed every time you open a new terminal window).

To edit the file:
1. Type `vim .bash_profile`. 
2. Type `i` to enter edit mode.
3. Replace the lines:

````bash
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi
````
with 

````bash
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi
````
4. Press `Esc` to exit edit mode and then type `:wq!` to exit.

You should now be able to open the VNC viewer. If not, try to kill the VNC server (`vncserver -kill :X` where `X` is your VNC number) and start a new vncserver.

With this fix Anaconda will only be started when you open a new terminal window in your VNC session. You do not need to modify .bashrc any more.