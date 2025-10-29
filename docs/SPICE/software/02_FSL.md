---
title: FSL
---

FSL is a comprehensive library of analysis tools for FMRI, MRI and diffusion brain imaging data.

FSL is installed in `/usr/local/fsl` and activated for all users by default.

## Setup FSL
To get started, you need to set the FSLDIR environment variable to point to the FSL installation directory:

````{bash}
# FSL Setup
FSLDIR=/usr/local/fsl
PATH=${FSLDIR}/share/fsl/bin:${PATH}
export FSLDIR PATH
. ${FSLDIR}/etc/fslconf/fsl.sh
````

## Further documentation
For more information on how to use FSL, see the [FSL documentation](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/).
