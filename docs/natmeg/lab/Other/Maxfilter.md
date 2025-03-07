---
title: Maxfilter
---

# Maxfilter

It is convenient to use a script to loop through your raw fif-files with MaxFilter. MaxFilter is installed on DANA.

## Before measurement
1. Copy the master **/home/master/data_scripts/avg_headpos/maxfilter_avgHead.sh** to your own directory.
2. Change the settings in the headers to match your desired processing pipeline.
3. Make executable
  
`chmod u+x <your_file_name.sh>`

> ! To check if the file is executable type `ls -l <your_file_name.sh`

## During measurement
No action required

## After measurement
1. Run your personalized maxfilter script (cd into correct folder)

`./<your_file_name.sh>`

2. When analysis is done, upload to server

### Maxfilter names guide

- *sss*: processed with Signal Space Separation.
- *tsss*: processed with Temporal Signal Space Separation.
- *mc*: applied movement correction.
- *ds*: data is downsampled.
- *quat*: quaternion; it has estimated the head movement but not done movement correction (this is represented in quaternion format).
- *avghead*: TBA

### Note

This pipeline is a wrapper for running Neuromag MaxFilter inside the NatMEG infrastructure at Karolinska Insitutet, Sweden (www.natmeg.se). Neuromag MaxFilter is a commercial software licenses by Electra Neuromag. The head position averagers are written in Python and use functions from MNE-Python (https://martinos.org/mne/stable/index.html). The pipeline has been tested to work on DANA, but no guarrantee is provided that it will work elsewhere!
