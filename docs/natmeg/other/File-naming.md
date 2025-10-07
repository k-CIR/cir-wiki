---
title: File naming
---

# File naming

Plan in advance how you want to name your files. You may have different conditions or times of measurement. Plan also for how you want to name the files if you have to stop recordings. For recording you do not have to consider the BIDS format as this is implemented at a later stage. However, it is good to have a consistent naming scheme from the start but make sure the name contains task/conditions.

## Recommendations

1. Keep filenames consistent across acquisition modalities.
2. Use comprehensible but short abbreviations for task names and conditions.
3. Avoid underscore (_) and hyphen (-) in the filename as these are used in BIDS format. Use instead camel case (e.g., `GoNoGo`).
4. Special characters and spaces are not allowed.

## Multiple recordings of same task/condition

### On SQUID acquisition computer
If you need to split a recording into multiple files, add a suffix (eg. `A`, `B` or `1`, `2`). Note that if using the [preprocessing pipelines](../preprocessing/pipeline.md), MaxFilter will be applied to each file separately, but continuous head movement estimation will be done across files if merge option is set. In the BIDS conversion, the files will be flagged for check and you have the option to add a run number.

### On OPM acquisition computer
As a timestamp added to each file, there is no need to add a suffix. If using the [preprocessing pipelines](../preprocessing/pipeline.md), the `copy_to_cerberos.py` script will add suffix `_dupX` to files with the same name after removing the timestamp. In the BIDS conversion, the files will be flagged for check and you have the option to add a run number.

If possible, check and rename files right after the recording session to avoid confusion later. There are several options to do this, see below.

## Issues
### Fixing wrong filenames of recordings

<u>Problem</u>: One or more recording is saved with a wrong filename

<u>Solution</u>: rename filenames (three ways)

1. Open a terminal
  > 1. cd to data folder (replace *text* with the text that applies your project):
  >> /neuro/data/sinhue/*your_project_name*/NatMEG_*number*/*YYMMDD*
  > 2. Rename the file:
  >> mv *old_filename.fif* *new_filename.fif*
  > 3. Press enter.

> ! Be aware that if a file with the new filename already exists, it will be overwritten with no option to recover the lost data. Rename any overlapping named file first.

2. Open folder window
  >1. Go to /neuro/data/sinhue/*your_project_name*
  >2. Right click and rename file

3. Open [BeyondCompare](Beyond-compare.md)
  >1. Open your project path
  >2. Right click and rename file
> ! Using BeyondCompare on DANA you can also rename files you have uploaded to Archive
