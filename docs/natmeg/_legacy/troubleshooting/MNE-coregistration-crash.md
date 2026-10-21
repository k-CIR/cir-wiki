---
title: MNE coregistration crash
tags: [MNE-Python, troubleshooting]
---

## Issues

??? failure "MNE coregistration crashes the session"
    MNE coregistration `mne.gui.coregistration()` in Python crashes the entire session.

    !!! note ""
        This might be due to some incompatibility between the 3D render function and the video driver, or lack thereof on Compute.

    !!! success ""
        Run this snippet of code in the terminal before starting Spyder: `export MESA_GL_VERSION_OVERRIDE=3.3`
