# Eye-tracker

For details on how to set-up Eye-tracker consult the [User manual](https://natmeg.se/onewebmedia/EL1000_UserManual_1.52.pdf) which is also available in the locker behind the MSR-cabinet.

## Equipment required
- The screen
- Eye-tracker

You will also need some lines of code in your Presentation scripts to initiate the eye-tracker, start calibration procedure and start recording.

## Before measurement
1. Put screen in correct position (see [Screen and projector](../stimulus-equipment/visual/Screen-and-projector.md))
2. Start eye-tracker software by pressing the letter  *t*  on the keyboard, then press enter

> ! If you do not see a terminal on the eye-tracking PC when you turn on the screen
> - Check that the screen setting of the Stimulation PC is not set in dual screen mode and that the correct input channel is selected
> - Check that the eye-tracking computer is turned on. The computer is found at the bottom of the stimulation cabinet

> ! To start eye-tracker in simulation mode type *t -x* and press enter

3. Make sure you have the right configuration for your needs and that the corneal reflection (CR) and pupil thresholds are set.
4. Adjust eye-tracker by moving the arm or by tilting the screen a bit.
5. Make sure MISC-channels 1-6 are activated in Acquisition settings. This is where ET-data is stored.

### Calibration and validation
When participant is seated in the MSR, calibrate the system then validate your calibration.

## During measurement
1. Monitor eye-positions

> ! As participants tend to sink down a bit during recordings eye-tracking may be lost if not chair is raised properly<br>
> ! If using the table, make sure pads or participant's hands are not blocking the eye-tracker

2. Check calibration

## After measurement
1. Turn off eye-tracking software
2. Remove eye-tracker and put back in box

Eye-tracking data is saved accordingly:
* MISC001 = X Left
* MISC002 = Y Left
* MISC003 = Pupil Left
* MISC004 = X Right
* MISC005 = Y Right
* MISC006 = Pupil Right

## Specifications
For  eye tracking we use  an EyeLink 1000 binocular tracker from SR Research.  The current installation runs at a maximum of 1000 Hz, tracking both eyes binocular.

The eye tracker is typically controlled via Neurobs Presentation,   
Via Presentation you can access the eye tracker output in realtime.

The X, Y  and pupil diameter of each eye is also output into the MEG system analog channels and sampled side by side with the MEG data.
The calibration space of the Eye-tracker is 1920x1080, with 0,0 in the top left corner.

The Eye tracker settings are aligned to the projector, so that the projector ini-file uses the pixel space (1920x1080), standard visual size (72x44 cm) and distance (100 cm) of the projector.

* Further technical specifications for the equipment is found in the manual [here](https://natmeg.se/onewebmedia/EL1000_UserManual_1.52.pdf).


## Issues

### The eye-tracking program is beeping and blinking
The eye-tracker has been disconnected from the cables in the MSR. Reconnect the eye-tracker or close the eye-tracking program.

### Eyes look blurry and the pupils are not detected.
Check that the participant's hands or paddings are not blocking the camera.
