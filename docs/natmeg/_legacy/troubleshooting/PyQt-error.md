---
title: PyQt5.QtWebKitWidgets error in Spyder
tags: [Python, PyQt5, Spyder, troubleshooting]
---

## Issues

??? failure "Spyder cannot open because PyQt5.QtWebKitWidgets is missing"
    Spyder cannot open and gives an error `ModuleNotFoundError: No module named 'PyQt5.QtWebKitWidgets'`.

    !!! note ""
        The problem seems to be due to inconsistencies in where the package PyQt is located in the Anaconda environments. It can be due to using `pip` to install into an Anaconda environment. It might also be due to outdated versions of the package `PyQt` or `PyQt5`.

    !!! success ""
        In lack of a better solution, remove the entirety of the Anaconda environment and create it again from scratch.

        In this example, the environment is recreated by reinstalling MNE from the source. In other cases where the environment is not defined elsewhere, you might want to back up the environment into a text file like this: `conda env export > environment.yaml`

        **1) Remove old environment**

        ```bash
        conda env remove --name mne
        ```

        **2) Create new environment (from MNE)**

        ```bash
        conda install --channel=conda-forge --name=base mamba
        mamba create --override-channels --channel=conda-forge --name=mne mne
        ```

        For more information on installing MNE, see https://mne.tools/stable/install/manual_install.html.

        **3) Reinstall Spyder**

        ```bash
        mamba install spyder
        ```
