---
title: FreeSurfer
---

Freesurfer is not supported on Ubuntu 24, which is the OS on the SPICE. However, it is possible to run FreeSurfer using a Singularity container. The [fMRIPrep](../singularity_containers/01_fmriprep.md) container has all the needed dependencies. 

Run the following command from the terminal to start it. 
```
singularity shell --bind $(pwd):$(pwd) --cleanenv /scratch/singularityContainers/fmriprep.simg
```

You need a freesurfer license. If you don't have one, follow this [link](https://surfer.nmr.mgh.harvard.edu/registration.html). Upload it to SPICE and define the path to the FS_LICENSE in the singularity terminal.

```
export FS_LICENSE=<path_to_freesurfer_license>
```

Next step is to define the freesurfer SUBJECTS_DIR where the output will be saved to.
```
SUBJECTS_DIR="<path_to_SUBJECTS_DIR>"
```

Now you are ready to run freesurfer!
```
recon-all -subject <subject id> -i <path_to_t1> -all
```
