---
title: R/Rstudio trouble shooting
tags: [R, Rstudio, troubleshooting]
---

Here are some know issues with R/Rstudio on Compute.

## Install R/Rstudio
See [here](../install-software/Guide-for-setting-up-R-and-RStudio-on-Compute.md).
 
## r-stan problems
<u>Problem</u>: issues installing rstan-dependencies

<u>Solution</u>: Set static download of V8 library

```r
Sys.setenv(DOWNLOAD_STATIC_LIBV8=1)
install.packages("V8")
```

## Update R
When starting RStudio it informs you that it is an outdated version and you should get the latest version from the website. Just click ignore. To update R your need to do it through Anaconda:

```bash
conda update r-base
```

## Error messages when starting Rstudio
I get several error messages in the terminal when I start Rstudio. Those I ignore. Rstudio starts and it works ok.

## Install packages
Some packages (like _lme4_) cannot be installed through RStudio. To fix this, I needed to first install _CMake_. Cmake can be installed though Anaconda, like this:

```Bash
conda install -c anaconda cmake 
```
After this, it was possible to install lme4 through R as usual:

```r
install.packages("lme4")
```
