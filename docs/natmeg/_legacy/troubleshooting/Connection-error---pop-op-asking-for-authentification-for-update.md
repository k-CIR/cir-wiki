---
title: Connection error - pop-op asking for authentification for update
---

## Issues

??? failure "Authentication pop-up keeps appearing for updates"
    A pop-op prompt saying "*Authentification is required to set the network proxy used for downloading packages*" keeps appearing but requires sudo rights to continue.

    ![]({{ picture_path }}/Fig_4-1.png)

    This is possibly the same or a related error:

    ![]({{ picture_path }}/Fig_5-1.png)

    !!! note ""
        It seems to be a generic error message caused by an outdated driver somewhere. Update 2021-01-21: this should be fixed now (@mcvinding).

    !!! success ""
        Probably the drivers need to be updated by someone with sudo access. Until then, launch a Terminal Console and type `gnome-session-properties`, then uncheck the PackageKit Update Applet. Then restart your [VNC server](../set-up-connection/03_Connect-to-Compute.md).

    !!! note ""
        The solution is from https://unix.stackexchange.com/questions/242423/banish-a-popup-error-message.
