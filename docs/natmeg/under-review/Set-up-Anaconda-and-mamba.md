Anaconda is an open-source and free package and environment management system which allows you to install eg. python or R packages into separate virtual environments. Miniconda is a lightweight version.

Read here how to download and install Anaconda or Miniconda
https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

Once you have installed and set-up Anaconda it is recommended that you use it to install mamba, basically speeding up all future installations.

````bash
conda install --channel=conda-forge --name=base mamba
````

The conda-forge channel used above is commonly used so you can save some effort by adding it to the defailt channel list.

````bash
conda config --add channels conda-forge
````

Also activate a strict priority

````bash
conda config --set channel_priority strict
````

