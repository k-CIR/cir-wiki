---
title: PyQt5.QtWebKitWidgets error in Spyder
tags: [Python, PyQt5, Spyder, troubleshooting]
---

**Problem:** Spyder cannot open and gives an error `ModuleNotFoundError: No module named 'PyQt5.QtWebKitWidgets'`

**Cause:** The problem seems to be due to inconsistencies in where the package PyQt is located in the Anaconda environments. Can be due to using `pip` to install into an Anaconda environment (maybe). Might also be due to outdated versions of the package `PyQt `or `PyQt5`.

**Solution:** In lack of a better solution, I removed the entirety of my Anaconda environment and created it again from scratch. If anybody has a better or simpler solution please add it!

In this example, I create the environment by reinstalling MNE from the source. In other cases where the environment is not defined elsewhere, you might want to backup the environment into a text file. Like this: `conda env export > environment.yaml`

**1) Remove old environment**

```bash
conda env remove --name mne
```
**2) Create new environment (from MNE)**
```bash
conda install --channel=conda-forge --name=base mamba
mamba create --override-channels --channel=conda-forge --name=mne mne
```
For more information on installing MNE, see here: https://mne.tools/stable/install/manual_install.html

**3 Reinstall Spyder**
```bash
mamba install spyder
```