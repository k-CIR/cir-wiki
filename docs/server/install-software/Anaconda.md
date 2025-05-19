---
title: Activate Anaconda
---

Anaconda is an open-source and free package and environment management system which allows you to install eg. python or R packages into separate virtual environments. Miniconda is a lightweight version.

## Use the pre-installed Anaconda
Anaconda with a base package is installed on the server. 

Activate and initate the common version by typing the following commands into the terminal:

```bash
source /opt/anaconda3/bin/activate
conda init
```

## Prepare for local installation
Next step is to set-up for installing environments locally by doing the following:

```bash
# Create directory for conda cache
mkdir -p ~/.conda/pkgs/cache

# Configure conda to use your directories
conda config --add pkgs_dirs ~/.conda/pkgs
conda config --add envs_dirs ~/.conda/envs
```
Now your new packages will be installed locally in `~/.conda/envs`

## Create a new environment


To create a new environment, you can use the following command:

```bash
conda create -n <env_name> python=<python_version>
```
Replace `<env_name>` with the name you want to give to your environment. You can also specify the version of Python you want to use (e.g., `python=3.8`).

You can then check you environments by typing:

```bash
conda info --envs
```

## Activate the environment
To activate the environment, use the following command:

```bash
conda activate <env_name>
```
Replace `<env_name>` with the name of the environment you created.
## Install packages
To install packages in the activated environment, you can use the following command:

```bash
conda install <package_name>
```
Replace `<package_name>` with the name of the package you want to install. You can also specify multiple packages separated by spaces.
For example, to install `numpy` and `pandas`, you can use:

```bash
conda install numpy pandas
```
## Deactivate the environment
To deactivate the environment, use the following command:

```bash
conda deactivate
```
This will return you to the base environment.

See the [Anaconda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html) for more information on how to use Anaconda and manage environments.