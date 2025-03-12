---
title: The CIR data template
---

The **main directory** of the **CIR data template** contains all **important directories** and **singularity containers** for running the programs necessary for transfer, conversion to BIDS and preprocessing of data.

![]({{ picture_path }}/wiki_images/cirtemplate.png)

### Scripts&#x20;

* **`run_dicomtransfer.sh`**: handles file transfers. The script assumes data has been organized according to the MRC standard.
* **`create_heuristic_heudiconv.sh`**: extracts the metadata from DICOM files located in the `/dicom` directory. It generates a `.tsv` file for each DICOM file, storing the results in a hidden folder (`.heudiconv`) within the `/bids` directory. For example, metadata from a subject with ID "1001" will be stored at `/bids/.heudiconv/1001/info/dicominfo.tsv`
* **`run_heudiconv.sh`**: creates a basic BIDS structure from DICOM files and stores the output in the `/bids` folder. It reads the heuristics from the file `/heudiconv/heuristic.py`
* **`run_fmriprep.sh`**: Preprocesses BIDS-formatted data located in the **`/bids`** folder using _fmriprep_. The preprocessed output is stored in the **`/bids/derivatives/fmriprep`** directory.
