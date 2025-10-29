---
title: fMRIPrep
---

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