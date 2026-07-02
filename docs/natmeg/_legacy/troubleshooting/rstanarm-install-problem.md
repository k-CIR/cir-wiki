---
title: rstanarm install problem
tags: [R, rstanarm, troubleshooting]
---

## Issues

??? failure "rstanarm installation dependency troubles"
    If you run into dependency troubles trying to install the `rstanarm` package, this works if `V8` fails to install.

    !!! success ""
        For Linux, download `libv8` during installation:

        ```r
        Sys.setenv(DOWNLOAD_STATIC_LIBV8=1)
        install.packages("V8")
        ```
