---
title: Working Locally
---

In order to work with PET data locally, you might need to mount the file servers for access to files and scripts, and download and install Flexiview for access to PET data records. 

# Locate your data

If you have started a project more recently, data should be primarily stored on [SPICE](https://k-cir.github.io/cir-wiki/SPICE/) and can be downloaded [using the provided instructions](https://k-cir.github.io/cir-wiki/SPICE/04_download_your_data/). Data from older projects is either stored in Flexiview, or can be found on Alfred. Instructions on how to [mount drives like Alfred]() and how to [use Flexiview]() can be found on these pages. 

# Mount necessary network drives
Some tools, like Solena, require the user to map the correct network drives containing custom matlab scripts. Information on the different network drives can be foud [here]()

# Pick your analysis and preprocessing tools
## PETPrep
[PETPrep](https://petprep.readthedocs.io/en/latest/) is a BIDS App that can automatically preprocess PET data. PETPrep can be run locally as a Docker container, provided you have a BIDS dataset with at least one T1-weighted MRI image per subject. To start running PETPrep, you will first have to convert your data to BIDS format. Instructions on [which software to use](https://k-cir.github.io/cir-wiki/bmic/03_file_conversion_tools) and how to [run BIDS conversion locally](https://k-cir.github.io/cir-wiki/bmic/04_file_conversion) can be found on the Wiki pages. 

If you want to run an old version of PETPrep (petprep_hmc and petprep_extract_tacs), documentation can be found [here](https://k-cir.github.io/cir-wiki/bmic/05_pet_bids_apps)

## Solena 
If you do not want to use BIDS Apps, BMIC also provides access to a matlab based software called Solena. Instructions for how to [set up Solena](https://k-cir.github.io/cir-wiki/bmic/06_Solena_setup) and [run Solena](https://k-cir.github.io/cir-wiki/bmic/07_Using_solena) can be found on the respective wikipages. 

