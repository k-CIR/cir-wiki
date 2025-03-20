---
title: Digitization
---

# Digitization

**The digitization is the second part of the preparation. The first part is the [placement of electrodes](01_Electrodes-standard-setup.md).**

## Why

Head positioning should be monitored either continuously throughout the acquisition or at the start and end of the recording. The MEG acquisition is done only with respect to the MEG device, instead of the anatomy of the subject. Therefore, MEG devices include a subsystem to determine the position of the head with respect to the MEG sensors. As MEG (unlike MRI) cannot directly measure the position of the head, small coils known as Head Position Indicator coils (HPI) placed at known locations on the scalp of the subject, when energized, will generate a magnetic field that helps us to localize the position of head in a three-dimensional space, with respect to the MEG sensor array. If continuous head position tracking is enabled, generally small movements are acceptable with a maximum error of 5 mm.

Information about the patient's head position, orientation, and shape is obtained by digitizing (3D digitizer) the standard fiducial points, HPI coils, and the required additional points creating Cartesian co-ordinates in a 3D space. Digitization of four HPI coils, and landmarks, which include three bony fiducial points (Nasion, left, and right pre-auricular points), and additional points, is performed.

The HPI coil positions, and hence the head position, are estimated from the coil signals. This estimation is done several times per second, allowing the system to track also relatively fast movements. Once the head position is estimated, the MEG signals are transformed to a reference head position. This conversion is sequentially performed at each time point throughout the continuous (raw) data file.

## Equipment

TBA

## Before measurement
1. Check so that the correct HPI preparation is loaded
2. Remember to check  **cHPI**  in the Acquisition window

To monitor head position, open a terminal and type: 
```bash
mneHeadPos
```

![HPI tool](/resources/wiki_images/hpi-tool_small.jpg)

The head position is read from the latest HPI fit. Click" Reload HPI" to update the view.

> ! Be aware that the head position tool does not show the actual participants head. The head is a template head and should only be used as an approximation of the participant's real head position in the MEG helmet.

## During measurement

1. After each time you've stopped a measurement you need to check the  **cHPI** box again

You can rotate the head in the head position tool using the buttons on the GUI or by using the mouse wheel. You can change what is displayed (helmet, transparency, HPI on/off, head point fits, etc.) by pressing "Options...".

To view the head position from a previous file (e.g. for comparison) open a new terminal window and type:

> /data/MNE/mne_visualize_hpi_file *your_file_name*

The *your_file_name* is the filename of the file you want to read including the full path

## After measurement
Close head position tool


## Issues
### Acquisition does not ask about measuring HPI
[Acquisition](../squid-acquisition/02_Acquisition.md) will automatically ask if you want to do/redo HPI fit every time you click START or RESTART. If you pressed Skip but want to do the HPI fit anyway, you need to restart the recording.

<u>Problem</u>: If [Acquisition](../squid-acquisition/02_Acquisition.md) does not ask about measuring HPI, it might be because it has not registered the HPI digitization. You can check if HPI is digitized in the [Acquisition](../squid-acquisition/02_Acquisition.md) main window. It will either specify the time the HPI was digitized or say "HPI: not digitized!"

<u>Solution</u>: load the correct preparation with the digitized HPI coil locations

> ! Note that every time you click start in Acquisition, it saves a new preparation, so make sure that you note the time you saved the preparation with the digitized HPI on the digitization PC.

### HPI errors

![HPI results](/resources/wiki_images/hpi-results_small.jpg)
_(HPI results window showing successful HPI fit)_

<u>Problem</u>: Errors with HPI. It gives an error message or Suggestion in HPI results window (screenshot) is "redo HPI" as opposed to "Accept" (like in the screenshot).

<u>Solution</u>:
1. Make sure the correct preparation is loaded with the digitized HPI coil locations.
2. Check that the HPI cable is connected to the panel at the side of the scanner.
3. Click "Try again" to see if the fit has improved.
4. Make sure that all HPI coils on the participant's head is inside the helmet. If possible, reposition the participant, so at least three HPI coils are inside the helmet. Click "Try again" to see if the fit has improved. If not, proceed to step six.
5. Check for loose coils that might have come off. Do not try to re-attach them; go to step six.
6. Redo HPI/isotrak fit: Get the participant out of the scanner to the preparation area. Then reposition/re-attach HPI coils and redo the digitization.