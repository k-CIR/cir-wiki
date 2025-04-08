---
title: VideoMEG
---

# Instructions for using the VideoMEG system at NatMEG

The video camera used by the VideoMEG system is not always in use. Make sure one (or several) "MSR camera" is connected to the fiber optic connector inside the MSR. You will find the labeled cables for this in the right corner, relative to the door entrance of the MSR. 

## Connect the BNC cable
Connect the BNC cable marked "VideoMEG" to one of the BCI ports of the PCI port 9-16 (usually response buttons). If you will be using response buttons, make sure not to connect the BNC cable to the same port as the response button.

![BNC connection VideoMEG]({{ picture_path }}/videomeg-bnc.png){ width="500" }
/// caption
The BNC connection for the VideoMEG system.
///

**Make sure to reset the connections once you are done with the measurements.**

## Log in to the computer
Start the computer and and press F2 on the computer to get to the boot menu. Select P2-SATA (not Windows).

## Preparing equipment 
Make sure the camera is aligned and focused on the (part of the) subject of interest.
> If you would unplug or switch camera make sure to restart the vido recording software.

## Preparing measurements

### File structure
The videomeg computer sends timestamps to the MEG acquisition computer on bit 16. These timestamps are also stored in the *.vid en *.aud files that are recorded on this computer. Upon conversion of the vid and aud files to an *.avi file, they are also burned into the avi video stream.

### Synchonization with Acquisition
Start the synchronization daemon by clicking the stopwatch icon on the taskbar. A terminal will open with some information. It will take about a minute before the timecodes start showing up on the MEG acquisition system. 


## Doing measurements
1. Start the video recording software by clicking the camera icon on the taskbar. Select the "Pike F032B fiber" camera, adjust the shutter and gain, and start acquisition. This will automatically assign a name for the audio and video files (*.aud and *.vid) with the date and time of the acquisition.
2. Start MEG data acquisition, check the presence of the timecodes in the trigger channel, run your experiment.
3. Stop MEG acquisition
4. Stop the video recording.

## After measurements

Convert the audio and video (*.aud and *.vid) files to an avi file. The avi file has the timestamps in a human readable format burned in the video stream. The avi file does NOT have the timestamps in a machine readable format.

## Batch convert
First make sure the only the files of your latest recording are in the recording folder. Move any other files to `old files`. The script is set up to loop through the files of all tasks from one subject during one recording session so make sure only these files are in the folder.

Open the terminal and navigate to the VideoMEG folder:
```bash
cd VideoMEG/Utils
```

Batch convert all files in folder by:

```bash
  python batch_export.py <SUBJECT_ID> <TASK-1> ... <TASK-n>
```

Where SUBJECT_ID is the NatMEG subject ID number.
Where TASK-n is the task description in the same order as the video was recorded.

For example 
```bash
  python batch_export.py '0916' 'RestingState_EyesClosed' 'WorkingMemory'
```
would take the first audio and video files (according to the timestamp and convert to a file named *'Video_NatMEG_20230313151245_sub-0916_task-RestingState_EyesClosed.avi'*. Then take the second audio and video files (according to the timestamp and convert to a file named *'Video_NatMEG_20230313151245_sub-0916_task-WorkingMemory.avi'*

If no subject or task is defined, file willl be saved with timestamp and run#.
e.g *Video_NatMEG_20230313151245_sub-XX_run-01.avi*