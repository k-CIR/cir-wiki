---
title: Activate Anaconda
---

Anaconda is an open-source and free package and environment management system which allows you to install eg. python or R packages into separate virtual environments. Miniconda is a lightweight version.

The anaconda package is installed on the server. If you wish to use the installed version, type the following commands into the terminal:

```bash
source /opt/anaconda3/bin/activate
conda init
```

Next step is to set-up for installing environments locally

```bash
# Create directory for conda cache
mkdir -p ~/.conda/pkgs/cache

# Configure conda to use your directories
conda config --add pkgs_dirs ~/.conda/pkgs
conda config --add envs_dirs ~/.conda/envs
```
Now your new packages should be installed located in `~/.conda/envs`
