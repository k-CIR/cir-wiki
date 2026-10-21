---
title: FreeSurfer
---

FreeSurfer is not currently supported natively on Ubuntu 24 (the operating system used on SPICE). To use FreeSurfer, run it through the [FreeSurfer and MNE-Python container](../singularity_containers/05_freesurfer_mne.md).

This container includes:

- FreeSurfer
- MNE-Python


## FreeSurfer license

You need a freesurfer license. If you don't have one, follow this [link](https://surfer.nmr.mgh.harvard.edu/registration.html). Upload it to SPICE and note the path to the license file for use in the next section.


## Start the container
Run the following commands from a terminal.

```bash
PROJECT_DIR=/data/projects/<project_name>
FS_LICENSE=<path_to_freesurfer_license>
SUBJECTS_DIR=<path_to_SUBJECTS_DIR>

singularity shell \
    --bind $PROJECT_DIR \
    --cleanenv \
    --env FS_LICENSE=$FS_LICENSE \
    --env SUBJECTS_DIR=$SUBJECTS_DIR \
    /scratch/singularityContainers/mne_freesurfer.sif
```

This mounts your PROJECT_DIR into the container, making all files in that directory available inside the container. You can also specify paths to other directories if needed using the --bind option.

Now you are ready to run freesurfer!
```
recon-all -subject <subject id> -i <path_to_t1> -all
```

## FreeSurfer and MNE-Python
If you are performing MEG/EEG source localisation, you will also need MNE-Python to generate the Boundary Element Model (BEM) surfaces required for forward modelling. The container includes MNE-Python for this purpose.

Create the BEM surfaces using:

```bash
mne watershed_bem --subject <subject_id> --subjects-dir <path_to_SUBJECTS_DIR> 
```

Optionally, you can create a [dense scalp surface](https://mne.tools/stable/auto_tutorials/forward/30_forward.html#visualizing-the-coregistration). This is useful for visual coregistration, alignment of digitised head points, and marking fiducials.
```
mne make_scalp_surfaces \
  --subject <subject_id> \
  --subjects-dir <path_to_SUBJECTS_DIR> \
  --mri <path_to_MRI> \
  --no-decimate
```

The path supplied to --mri is relative to:
```
$SUBJECTS_DIR/<subject_id>/
```
For example, if the MRI file is located at:
```
$SUBJECTS_DIR/<subject_id>/orig/001.mgz
```

then use:
```
--mri orig/001.mgz
```
