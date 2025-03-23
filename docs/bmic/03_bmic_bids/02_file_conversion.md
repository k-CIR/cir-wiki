---
title: File Conversion
---

The BIDS specification for PET can be found [here](https://bids-specification.readthedocs.io/en/stable/modality-specific-files/positron-emission-tomography.html). PET-BIDS data requires storage in NIfTI (`.nii.gz`) format with the appropriate JSON (`.json`) sidecar files, and tabular data as tab-separated values (`.tsv`).

I recommend starting with converting the anatomical MR data first, because they are simpler than the PET data and establish the basic folder structure.

## Raw MR data

...

## Raw PET Data

Raw PET imaging data at BMIC from the GE PET systems is stored as DICOM (`.dcm`), and older PET data from the HRRT system is stored as ecat7 (`.v`).

### DICOM (`.dcm`)

...

### ecat7 (`.v`)

...