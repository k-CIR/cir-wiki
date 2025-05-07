---
title: Singularity images
---

Singularity is a container platform designed for high-performance computing environments. It enables users to create and run containers that encapsulate software and its dependencies in a portable, reproducible, and secure manner.

At the CIR server, we maintain several pre-built Singularity images to support the execution of various neuroimaging software tools, ensuring consistency across analyses and simplifying software management.

## Location of Singularity images
Singularity images ara available at the following location: `/scratch/singularityContainers`

## Available images
### fmriPrep
[fMRIPrep](https://fmriprep.org/en/latest/index.html) is a robust and user-friendly fMRI preprocessing pipeline that handles variations in scan acquisition protocols and that requires minimal user input, while providing easily interpretable and comprehensive error and output reporting.

Location: `/scratch/singularityContainers/fmriprep.simg`
### heudiconv
[heudiconv](https://github.com/nipy/heudiconv) is a flexible DICOM converter for organizing brain imaging data into structured directory layouts, such as in BIDS.

Location: `/scratch/singularityContainers/heudiconv.sif`

### halfpipe
[ENIGMA Halfpipe](https://github.com/HALFpipe/HALFpipe)

Location: `/scratch/singularityContainers/halfpipe.sif`

### mriqc
[mriqc](https://mriqc.readthedocs.io/en/latest/)

Location: `/scratch/singularityContainers/mriqc.sif`

## Further documentation
For more information on how to use Singularity check [here](https://docs.sylabs.io/guides/3.5/user-guide/index.html#).
