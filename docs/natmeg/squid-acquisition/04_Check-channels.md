---
title: Check channels
---

# Check channels

After [tuning](03_Tuning.md) and before each measurement you should check the channels.

## Before measurement
1. Click  *GO!*  in the [Acquisition](02_Acquisition.md) control window
2. Browse through channels to see if everything looks alright
3. If everything looks good you are ready to start recording, if not see [below](#fixing-bad-channels-before-recording)

## During measurement
If door is opened or between condition when recording has been stopped redo the steps above

## After measurement
No action required

## Issues

### Fixing bad channels before recording

<u>Problem</u>: Jumpy or noisy channels

<u>Solution</u>: Use Squiddler to heat bad channels

Open: Menu -> Neuromag -> Squiddler

![Squiddler](../../resources/wiki_images/squiddler_small.jpg)


In Squiddler:

1. Select channel with slider
2. Open Commands, click Heat Channel. Wait until the channels settle then inspect if the channel looks fine. Inspect if other channels have been affected by the heating.
3. Repeat 1-2 for all bad channels.
