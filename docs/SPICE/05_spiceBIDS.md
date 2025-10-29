---
title: BIDS on SPICE
---

## MEG and EEG data
NatMEG provide a complete pipeline for pre-processing MEG and EEG data including conversion to BIDS format. See details on the [NatMEG pipeline page](../natmeg/preprocessing/pipeline.md).

## MRI data
MRC provide a pipeline for the standard [CIR-protocol](../mrc/mrc-cir-protocol.md) that you can find [here](../mrc/mrc-bids.md) and a singularity container for running [heudiconv](../SPICE/singularity_containers/02_heudiconv.md) to convert DICOM data to BIDS format.

## PET
BMIC provide tools for file conversion and BIDS organization of PET data. See details [here](../bmic/03_bmic_bids/01_file_conversion_tools.md). In addition, there are several [Bids-apps](../bmic/03_bmic_bids/03_pet_bids_apps.md) available for PET data processing and analysis.