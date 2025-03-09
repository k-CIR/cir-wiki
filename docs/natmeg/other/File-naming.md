---
title: File naming
---

# File naming

Plan in advance how you want to name your files. You may have different conditions or times of measurement. Plan also for how you want to name the files if you have to stop recordings.

> ! Acquisition does not allow special characters or spaces in the filename

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
