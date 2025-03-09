# Acquisition

Acquisition is the main program you need for running the MEG-recording.

## Before measurement

Open: Menu -> Neuromag -> Acquisition
> ! Always check for error messages in the top and check that gantry position is automatically detected. If not, se [How to restart acquisition](#how-to-restart-acquisition)

1. Load project
2. Load settings
> If you use STI channels it is recommended that you add all STI channels, even if you only use some of them. This is because of how the composite channels (STI101, STI102) is configured.
3. Add participant (as Patient)

> Do [Digitisation](../preparation/02_Digitization-hpi.md) (save preparation)

1. Load preparation
2. Always load the settings again, after loading preparation. If the same settings are not applied on the digitisation computer settings are unloaded.

## During measurement

Use acquisition to handle the recording

1. Press  **GO!**  to start recording buffer

> ! Don't forget to [check channels](04_Check-channels.md)

1. Check  **cHPI**  to record continuous head position
2. Check  **Record raw**  to record raw file(s)
3. Check  **Average**  to record average evoked file(s)

## After measurement
1. Save data files

> ! If Average box was checked, the first file to save will be the average file, then the raw file<p>
> ! Make sure to have a structured way of naming the files

## Issues

### How to restart Acquisition?

<u>Problem</u>: Channels are not appearing when running Acquisition. Acquisition is giving errors about "lost connection" or "cannot connect to channels".

<u>Solution</u>: In order do the following, if your problem keeps appearing then proceed to the next step; otherwise do not proceed:

1. Check that the correct setting is loaded (File -> Load Settings). See if the missing channels are still missing.
2. Close and re-open Acquisition Programs (remember to save preparations if you have already begun).
3. Restart Acquisition Programs. You find this option under the Neuromag top menu, "Maintenance". (Menu -> Neruomag -> Maintenance -> Restart  Acquisition). A terminal will pop up—type y to confirm. The restart might take a couple of minutes. Once the restart has completed, you need to restart Acquisition and also launch the Tuner and reload the current tunings you are using.
4. If none of the above works, you will need to do a "hard reset". Open the text-file "hard reset" and follow the instructions. Wait a few minutes and then restart Acquisition according to 3.
