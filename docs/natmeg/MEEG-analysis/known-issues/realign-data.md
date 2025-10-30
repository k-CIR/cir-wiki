---
title: Realignment of data from different MEG systems
---

## Data from different systems are not aligned

When combining data from different systems (e.g. matching EEG from MEGIN with OPM data from FieldLine), the data may not be aligned in time. This misalignment can lead to inaccuracies in analyses that rely on precise timing.

## Solution

Use [MNE-Python's realign_raw](https://mne.tools/stable/generated/mne.preprocessing.realign_raw.html) function to align the data.

```python
mne.processing.realign_raw(<raw_file>, <other_file>)
```