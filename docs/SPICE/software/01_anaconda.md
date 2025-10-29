---
title: Anaconda on SPICE
---

Anaconda comes pre-installed on SPICE and is the recommended way to manage your python environments and packages. By default, enviroments you create with Anaconda are stored in your home directory under `~/.conda/envs/` with packages in `~/.conda/pkgs/`.

Simply run `conda` in your terminal to see the available commands. You'll find some useful commands to get you started below.

Consult the [Anaconda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html) for more detailed information.

```bash
# Create a new conda environment "myenv" with a specific Python version
conda create --name myenv python=3.9

# Activate the environment
conda activate myenv

# List installed packages in the active environment
conda list

# Install packages in the active environment
conda install pandas numpy matplotlib

# List all conda environments
conda env list

# Deactivate the current environment
conda deactivate
```

## Global environments
If you want to create an environment that is available to all users on SPICE, you can create a global environment by running:

```bash
conda-create-global <environment_name> <conda create options>
```  

To activate on of the global environments, use its full path, for example:

```bash
conda activate /opt/anaconda3/envs/<environment_name>
```

Global environments and their path are visible to all users when running `conda env list` so only create global environments as neccessary for collaborative projects and clean up after use.