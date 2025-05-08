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

Example to run fmriPrep:
```bash
singularity run --bind $(pwd):$(pwd) --cleanenv ./scratch/singularityContainers/singularity/fmriprep.simg \
        path/to/data/dir path/to/output/dir \
        participant \
        --nthreads 20 \
        --omp-nthreads 10 \
        --fs-license-file path/to/freesurfer_licence \
        --output-spaces MNI152NLin2009cAsym \
        --fs-no-reconall \
        --work-dir  path/to/work/dir
```

### heudiconv
[heudiconv](https://github.com/nipy/heudiconv) is a flexible DICOM converter for organizing brain imaging data into structured directory layouts, such as in BIDS.

Location: `/scratch/singularityContainers/heudiconv.sif`

### halfpipe
[ENIGMA Halfpipe](https://github.com/HALFpipe/HALFpipe) is an intuitive tool designed to streamline reproducible fMRI analysis, covering preprocessing, individual, and group-level analyses. It leverages fMRIPrep for advanced preprocessing without requiring BIDS data conversion, and allows for real-time computation of common resting-state and task-based fMRI metrics.

Location: `/scratch/singularityContainers/halfpipe.sif`

### mriqc
[mriqc](https://mriqc.readthedocs.io/en/latest/) is an open-source tool that automatically extracts image quality metrics (IQMs) from structural, functional, and diffusion MRI data, without needing a reference image. It is designed for minimal preprocessing and is built using modular Nipype workflows that integrate tools like ANTs and AFNI. MRIQC adheres to BIDS and BIDS-App standards for compatibility and follows strong software engineering practices to ensure robustness and reliability, with continuous testing on diverse datasets.

Location: `/scratch/singularityContainers/mriqc.sif`

## Running a Singularity Image
If the data to be preprocessed is already on the server, you are ready to run a Singularity image. E:
```bash
$ singularity run --cleanenv fmriprep.simg \
    path/to/data/dir path/to/output/dir \
    participant \
    --participant-label label
```
## Further documentation
For more information on how to use Singularity check [here](https://docs.sylabs.io/guides/3.5/user-guide/index.html#).
