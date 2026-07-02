---
title: R/Rstudio trouble shooting
tags: [R, Rstudio, troubleshooting]
---

Here are some know issues with R/Rstudio on Compute.

## Install R/Rstudio
See [here](../install-software/Guide-for-setting-up-R-and-RStudio-on-Compute.md).

## Issues

??? failure "r-stan problems"
    Issues installing `rstan` dependencies.

    !!! success ""
        Set static download of the `V8` library:

        ```r
        Sys.setenv(DOWNLOAD_STATIC_LIBV8=1)
        install.packages("V8")
        ```

??? failure "Update R"
    When starting RStudio it may inform you that it is an outdated version and that you should get the latest version from the website. Click ignore.

    !!! success ""
        To update R, do it through Anaconda:

        ```bash
        conda update r-base
        ```

??? failure "Error messages when starting Rstudio"
    Several error messages may appear in the terminal when starting RStudio.

    !!! success ""
        Ignore them if RStudio starts and works as expected.

??? failure "Install packages"
    Some packages, such as `lme4`, cannot be installed through RStudio.

    !!! success ""
        First install `CMake` through Anaconda:

        ```bash
        conda install -c anaconda cmake
        ```

        After this, install `lme4` through R as usual:

        ```r
        install.packages("lme4")
        ```
