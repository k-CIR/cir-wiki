---
title: Set-up and record headshape
---

# Acquisition

Acquisition is the main program you need for running the MEG-recording.

## Before measurement

**1. Open: Menu -> Neuromag -> Acquisition**

!!! warning "Check for error messages"
    Always check for error messages in the top and check that gantry position is automatically detected. If not, se [How to restart acquisition](#how-to-restart-acquisition)

**2. Load project**

**3. Load settings**

1. If you only need the headshape: Turn off all channels except one EEG channel and potentially any bio-channels or STI channels you want to record in parallel with the OPM-system.

!!! warning "For parallel recordings **Internal active shielding** MUST be un-checked"

!!! note "STI channels"
    If you use STI channels it is recommended that you add all STI channels, even if you only use some of them. This is because of how the composite channels (STI101, STI102) is configured.

**4. Add participant (as Patient)**

!!! tip "Save preparation before digitisation to transfer settings to digitisation computer"

> Do [Digitisation](../../preparation/02_Digitization-hpi.md) (save preparation)

**5. Load preparation**

!!! warning "Double check the settings"
    Always double check that the correct settings are loaded, especially if you have multiple projects or participants or did not save the preparation before digitisation.

## Headshape measurement

1. Press  **GO!**  to start recording buffer
2. Check  **Record raw**  to record raw file(s)
3. wait ~10 seconds **Stop**
4. Save file as `headshape`, `coreg` or any [reasonable own choice](../../other/File-naming.md) but be consistent across recordings


## Issues

### How to restart Acquisition?

<u>Problem</u>: Channels are not appearing when running Acquisition. Acquisition is giving errors about "lost connection" or "cannot connect to channels".

<u>Solution</u>: In order do the following, if your problem keeps appearing then proceed to the next step; otherwise do not proceed:

1. Check that the correct setting is loaded (File -> Load Settings). See if the missing channels are still missing.
2. Close and re-open Acquisition Programs (remember to save preparations if you have already begun).
3. Restart Acquisition Programs. You find this option under the Neuromag top menu, "Maintenance". (Menu -> Neruomag -> Maintenance -> Restart  Acquisition). A terminal will pop up—type y to confirm. The restart might take a couple of minutes. Once the restart has completed, you need to restart Acquisition and also launch the Tuner and reload the current tunings you are using.
4. If none of the above works, you will need to do a "hard reset". Open the text-file "hard reset" and follow the instructions. Wait a few minutes and then restart Acquisition according to 3.
