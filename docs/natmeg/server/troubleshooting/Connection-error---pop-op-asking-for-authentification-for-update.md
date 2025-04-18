---
title: Connection error - pop-op asking for authentification for update
---

**Problem**: a pop-op prompt saying "*Authentification is required to set the network proxy used for downloading packages*" keeps appears but require sudo right to continue.

![]({{ picture_path }}/Fig_4-1.png)

This is possibly the same/related error:

![]({{ picture_path }}/Fig_5-1.png)

**Cause**: It seems to be a generic error message caused outdated driver somewhere. **Update 2021-01-21:** this should be fixed now (@mcvinding)

**Solution**: Probably that the drivers need to be updated by someone with sudo access. Until then, this post tells how to ignore the pop-up message permanently: Launch a Terminal Console and type `gnome-session-properties` and then uncheck the PackageKit Update Applet. Then restart your [VNC server](../set-up-connection/03_Connect-to-Compute.md).

The solution is from https://unix.stackexchange.com/questions/242423/banish-a-popup-error-message.