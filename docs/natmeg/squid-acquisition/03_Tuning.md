---
title: Tuning
---

# Tuning
Tuning is not always needed, but recommend at least for the first measure of the day.

## Before measurement
1. Open Acquisition
2. Click the menu Tools -> Tuner. The tuning tool will appear.
3. Click file -> load tuning. A message will pop up asking if you want to read the default state tuning. Click ok.

> ! Optionally, you can click "measure noise" before loading the tuning and again after loading the tuning to see the noise level.
> The average noise level should be around 2.5-2.7.

4. When at a satisfactory noise level, stop and save tuning (overwrite default tuning).
5. Exit the Tuner (has to be done via the File menu)

## During measurement
No action required

## After measurement
No action required

## Issues

### The average noise level is too high (> 3) after loading the default tuning

<u>Solution</u>: Do the following:
    1. Check that there are no objects in the MSR that could be causing disturbances, e.g. non-tested metallic stimulus equipment, left items, etc. Remove those items
    2. Run new tuning: click "measure noise" and when it has measured the noise level, click "Tune". The tuning procedure with iterate through tuning parameters and try to minimize the noise in the system. Each iteration takes about 20 seconds. Click "stop tuning" when the average noise level is below 2.7.

> ! The tuning procedure takes up to 15 min. Make sure that you have enough time to run the tuning procedure and always check the tuning well in advance before your participant arrives.

> ! If sensors are missing, they are usually at a too high noise level. Ctrl-click on very noisy (or missing) sensors and heat via the menu. If many sensors are missing you can heat all sensors (this takes a couple of minutes). If problem remains, you might have to restart Acquisition (see this [Acquisition section](02_Acquisition.md)) before continuing with the tuning or call for assistance.
