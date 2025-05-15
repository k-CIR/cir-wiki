---
title: R
---

# Global installation of R
[Statistics software **R**](https://www.r-project.org) is installed globally and can be accessed typing `R` in the terminal.

# Take some control over your R packages
To take some control over where you R packages are installed, you can add a package path in a `.Renviron` configuration file. Simply run the following commands in the terminal to create a directry for your packages and a `.Renviron` file in your home directory and add the library path to it:

```bash
# Create directory for R your libraries
mkdir -p ~/.R/library

# Create .Renviron file in home directory
echo "R_LIBS_USER=~/.R/library" >> ~/.Renviron
```

# Take full control over your R packages
To take full control over your R packages and R versions, you can use a package manager like [**conda**](https://docs.conda.io/en/latest/) or [**renv**](https://rstudio.github.io/renv/).
