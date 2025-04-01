---
title: File Conversion
---

The BIDS specification for PET can be found [here](https://bids-specification.readthedocs.io/en/stable/modality-specific-files/positron-emission-tomography.html). PET-BIDS data requires storage in NIfTI (`.nii.gz`) format with the appropriate JSON (`.json`) sidecar files, and tabular data as tab-separated values (`.tsv`).

As a general rule, BIDS filenames contain key-value pairings which look as follows: 

```
{key1}-{value1}_{key2}-{value2}_{suffix}.{extension}
```

Each key name (e.g. `sub` for subject, or `ses` for session) is followed by its value (e.g. `01`) after a hyphen. Underscores separate the different key-value pairings. Finally, the suffix describes what kind of data the file describes, e.g. .pet, .T1w etc.  So a PET file for subject 5 and session 2 would be called `sub-05_ses-02_pet.nii.gz` .

I recommend starting with converting the anatomical MR data first, because they are simpler than the PET data and establish the basic folder structure.  If you are converting data from a large number of subjects all at once, I recommend creating a table with the relevant details (i.e. folder locations, subject numbers, etc), and then stringing them together using a programming language of your choice to be run through the terminal.

## Raw MR data

For conversion of MR data, we use `dcm2niix`.  For each T1w MR measurement, the following command needs to be run, with the paths replaced so that they point to the BIDS folder and the raw DICOM folder respectively, and `XX` replaced with the subject name or number.

```
dcm2niix -b y -ba n -z y -o /path/to/bids/folder/sub-XX/anat -f sub-XX_T1w /path/to/dicom/data
```

The flags here refer to the following:

* `-b y`  : Produce a BIDS JSON sidecar along with the converted `.nii.gz` file
* `-ba n` : Do not anonymise the JSON sidecar
* `-z y`  : Use gz compression in the outputted files (this greatly reduces file sizes)
* `-o`    : output directory
* `-f`    : filename

The command above assumes that there is only one session (so it is not included in the filename). If there are two sessions, then this information should be added to the filename, e.g. `sub-01_ses-02_T1w`.

**Note:** within the main DICOM folder, there are typically many sub-directories, which may or may not be named. The command above should be run pointed to the directory containing the T1w MR image which will be used alongside the PET processing. There are many ways to figure out which subdirectory is the correct one. One way to check is simply to generate JSON sidecars for each of the image folders and read what is listed under "SeriesDescription" using the following command:

```
dcm2niix -b o -z n -o . /path/to/dicom/folder
```

## Raw PET Image Data

Raw PET imaging data at BMIC from the GE PET systems is stored as DICOM (`.dcm`), and older PET data from the HRRT system is stored as ecat7 (`.v`).  For conversion of PET data, we use `PET2BIDS`, which has commands for both DICOM and ECAT7.

### DICOM (`.dcm`)

For converting PET DICOM files, we use the following command:

```
dcm2niix4pet /path/to/dicom/folder --destination-path /path/to/bids/folder/sub-XX/pet/sub-XX_pet.nii.gz
```
If you have multiple PET images per subject, you can use these as different sessions. You could put both sessions in the PET folder (with `ses-YY` in the filename), or alternatively, if you would prefer that they are more separated, you can also place them in different folders as follows:

```
dcm2niix4pet /path/to/dicom/folder --destination-path /path/to/bids/folder/sub-XX/pet/ses-YY/sub-XX_ses-YY_pet.nii.gz
```


### ECAT7 (`.v`)

For converting ECAT7, we can use the following command:

```
ecatpet2bids /path/to/pet/filename.v --convert -n /path/to/bids/folder/sub-XX/pet/sub-XX_pet.nii.gz
```

If you have multiple PET images per subject, you can use these as different sessions. You could put both sessions in the PET folder (with `ses-YY` in the filename), or alternatively, if you would prefer that they are more separated, you can also place them in different folders as follows:

```
ecatpet2bids /path/to/pet/filename.v --convert -n /path/to/bids/folder/sub-XX/pet/ses-YY/sub-XX_ses-YY_pet.nii.gz
```

## Raw PET Blood Data

In recent years at BMIC, raw PET blood data are stored in `.anc` files, which contain all of the relevant information. For now there is no straightforward tool for converting these files to BIDS, but this is in the works.