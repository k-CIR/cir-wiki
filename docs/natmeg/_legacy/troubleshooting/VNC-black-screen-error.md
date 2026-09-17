---
title: VNC black screen error
tags: [troubleshooting]
---

## Issues

??? failure "VNC shows a black screen error"
    You might experience a black screen with an error message when you first log in to a new VNC server.

    ![]({{ picture_path }}/Fig_1-1.png)

    ![]({{ picture_path }}/Fig_2-1.png)

    !!! note ""
        The error seems to be due to Anaconda or Python initiation, which messes with the VNC config in some way. The procedure below circumvents the problem.

    !!! success ""
        Open PuTTY to [connect to Compute](../set-up-connection/03_Connect-to-Compute.md) as usual. Then in the terminal edit `.bash_profile` so it does not call `.bashrc` when you log in with SSH.

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

        You should now be able to open the VNC viewer. If not, try to kill the VNC server (`vncserver -kill :X` where `X` is your VNC number) and start a new VNC server.

        With this fix Anaconda will only be started when you open a new terminal window in your VNC session. You do not need to modify `.bashrc` any more.
