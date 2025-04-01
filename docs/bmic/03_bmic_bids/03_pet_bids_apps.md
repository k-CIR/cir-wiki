---
title: BIDS Apps for PET
---

There are a growing number of BIDS apps for processing of PET data arranged according to the BIDS specification.  This guide will provide a brief guide for how to use several tools.


**Note:** these instructions are very preliminary, and subject to be updated.

## sMRIPrep: Structural MRI PREProcessing pipeline

While `sMRIPrep` is designed for T1w MR data, we typically collect this data alongside PET data for anatomical delineation. This tool performs some preprocessing following by the FreeSurfer pipeline.

The full documentation is [here](https://www.nipreps.org/smriprep/installation.html). What follows is a condensed version.

1. Activate your `PETBIDS` environment

    ```bash
    conda activate PETBIDS
    ```

2. Install the `sMRIPrep` docker wrapper.

    ```
    python -m pip install --user --upgrade smriprep-docker
    ```

3. `sMRIPrep` uses FreeSurfer, which requires a licence file. To obtain a FreeSurfer license, simply register for free at https://surfer.nmr.mgh.harvard.edu/registration.html and download the licence file to a known location. When running `sMRIPrep`, you will need to point it to your licence file location.

4. Run `sMRIPrep` on your data. Replace the relevant paths, and leave the participant command at the end.

    ```
    smriprep-docker --fs-license-file /path/to/freesurfer/license.txt \
    /path/to/bids/data/dir /path/to/output/dir participant
    ```

    For the output folder at the end, you can place the outputs into the derivatives folder of the BIDS data folder, i.e. /path/to/bids/data/dir/**derivatives**

5. This will generate derivative data folders including both freesurfer outputs in the `freesurfer` folder as well as diagnostic plots in the `smriprep` folder.  Go through the diagnostic plots and make sure that everything workout out as expected.


## petprep_hmc: PETPrep head motion correction workflow 

For PET data, it is important to perform head motion correction, for which `petprep_hmc` is designed. To use this package, you can use either the docker container or use it directly using Python. The full documentation is provided [here](https://petprep-hmc.readthedocs.io/en/latest/): what follows is a condensed version.

*Method 1: Using the docker container*

The docker container should work, but I believe that this syntax will soon be updated. Note that the output directory needs to be specified with the name of the pipeline too, i.e. /path/to/bids/data/dir/**derivatives/petprep_hmc**

```
docker run -it --rm \
    -v /path/to/bids/data/dir:/data/input \
    -v /path/to/output/dir:/data/output \
    -v /path/to/freesurfer/license.txt:/opt/freesurfer/license.txt \
    martinnoergaard/petprep_hmc:latest \
    --bids_dir /data/input \
    --output_dir /data/output \
    --analysis_level group
```

*Method 2: Using the bare-metal Python installation*

This method is usually more updated, but package installation can cause some annoyances. Remember to work in your conda PETBIDS environment.

1. Download the package. If you have git, you can git clone it

    ```
    git clone https://github.com/mnoergaard/petprep_hmc.git
    ```

Otherwise, download it from [here](https://github.com/mnoergaard/petprep_hmc), and unzip it to a folder called `petprep_hmc`


2. Install the package

    ```
    cd petprep_hmc
    pip install -e .
    ```

3. Run the pipeline through Python. Note that the output directory needs to be specified with the name of the pipeline too, i.e. /path/to/bids/data/dir/**derivatives/petprep_hmc**

    ```
    python3 path/to/petprep_hmc/run.py /path/to/bids/data/dir /path/to/output/dir group
    ```


## petprep_extract_tacs: PETPrep TAC extraction workflow 

The `petprep_extract_tacs` extracts time activity curves (TACs) using the FreeSurfer derivative output. To use this package, you can use either the docker container or use it directly using Python. The full documentation is provided [here](https://petprep-extract-tacs.readthedocs.io/en/latest/): what follows is a condensed version.

*Method 1: Using the docker container*

The docker container should work, but I believe that this syntax will soon be updated. Note that the output directory needs to be specified with the name of the pipeline too, i.e. /path/to/bids/data/dir/**derivatives/petprep_extract_tacs**

```
docker run -a stderr -a stdout --rm \ 
    -v /path/to/bids/data/dir:/bids_dir \
    -v /path/to/output/dir:/output_dir \
    -v $PWD:/workdir -v $PWD/petprep_extract_tacs:/petprep_extract_tacs \
    -v /path/to/freesurfer/license.txt:/opt/freesurfer/license.txt \
    --platform linux/amd64 \
    petprep_extract_tacs \
    /bids_dir /output_dir participant --n_procs 4  --petprep_hmc \
    system_platform=Darwin
```

*Method 2: Using the bare-metal Python installation*

This method is usually more updated, but package installation can cause some annoyances. Remember to work in your conda PETBIDS environment.

1. Install FreeSurfer, by following the instructions [here](https://surfer.nmr.mgh.harvard.edu/fswiki/FS7_linux).

2. Once FreeSurfer is installed, install the MATLAB Runtime

    ```
    sudo fs_install_mcr R2019b
    ```

3. Download the package. If you have git, you can git clone it

    ```
    git clone https://github.com/mnoergaard/petprep_extract_tacs.git
    ```

Otherwise, download it from [here](https://github.com/mnoergaard/petprep_extract_tacs), and unzip it to a folder called `petprep_extract_tacs`


4. Install the package

    ```
    cd petprep_extract_tacs
    pip install -e .
    ```

5. Run the pipeline through Python. Note that the output directory needs to be specified with the name of the pipeline too, i.e. /path/to/bids/data/dir/**derivatives/petprep_hmc**

    ```
    python path/to/petprep_extract_tacs/run.py /path/to/bids/data/dir /path/to/output/dir participant --n_procs 4 --gtm --petprep_hmc 
    ```
    Note: the petprep_hmc flag at the end directs the pipeline to use the output of the head-motion correction step.