---
title: MNE errors when plotting
tags: [MNE-Python, troubleshooting]
---

## Issues

??? failure "MNE plotting functions do not work"
    The various MNE functions for plotting do not work. Especially 3D graphics such as plotting source estimates on cortical surfaces. In Spyder it might even crash the entire Python session.

    !!! note ""
        This might be due to some incompatibility between the 3D render function and the video driver, or lack thereof on Compute. Possible also inconsistencies in Python dependencies.

    !!! success ""
        Run this snippet of code in the terminal before starting Spyder: `export MESA_GL_VERSION_OVERRIDE=3.3`. Also, make sure that you install MNE according to the [install instructions](../../software/mne-python.md).
