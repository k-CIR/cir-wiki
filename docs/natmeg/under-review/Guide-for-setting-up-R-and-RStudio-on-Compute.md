_R_ is a statistical programming language and _Rstudio _is a development environment for R. R/Rstudio is good software for running advanced statistical analysis, e.g. statistical modelling with the _lme4 _or _brms _packages and nice plotting features with _ggplot2_.

Neither R nor RStudio is pre-installed on Compute. You have to install it yourself. At the moment it is not possible to install directly from the source. However, with minimal hacks, it can be installed through Anaconda. 

However, it appears that R/Rstudio only has little support from the developers, so this does not appear to give the latest version of R.

For an up to date list of known issues with R/Rstudio on Compute see [here](R-trouble-shooting).

## Install RStudio through Anaconda

The first step is to make sure you have Anaconda installed: https://docs.anaconda.com/anaconda/install/linux/#installation

Make a new environment for RStudio. This will create an environment called `r_env`:

````bash
mamba create --name r_env
````
Activate the environment: 

````bash
source activate r_env 
````

Install RStudio from Conda Forge (https://anaconda.org/conda-forge/rstudio-desktop). This will install Rstudio and all dependencies (like R itself):

````bash
mamba install -c conda-forge rstudio-desktop 
````
When it is done with the installation you simple write `rstudio` in the terminal and you are ready to do some fun statistics :)

I get several error messages in the terminal when I start Rstudio. Those I ignore. Rstudio starts and works just fine.

## Update R
When starting RStudio it informs you that it is an outdated version and you should get the latest version from the website. Just click ignore. To update R your need to do it through Anaconda:

````bash
mamba update r-base
````

## Install packages
Most packages can be installed as usual though R with `install.packages`. Some packages (like _lme4_) cannot be installed through RStudio as a default. To fix this, I needed to first install _CMake_. Cmake can be installed through Anaconda, like this:

````Bash
mamba install -c anaconda cmake 
````

After this, it was possible to install lme4 through R as usual:

````r
install.packages("lme4")
````


