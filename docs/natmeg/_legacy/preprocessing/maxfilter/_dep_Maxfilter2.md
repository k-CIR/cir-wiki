---
title: Maxfilter script for NatMEG
tags: [natmeg, cerberos, maxfilter]
---
# Maxfilter script for NatMEG

This is the process describing how to use the maxfilter script for NatMEG. The script is designed to run on a computer with a MaxFilter™ installation. The head position averagers are written in Python and use functions from [MNE-Python](https://martinos.org/mne/stable/index.html). The pipeline has been tested to work on Cerberos at NatMEG, but no guarrantee is provided that it will work elsewhere!

You can find the necessary python scripts [here](https://github.com/natmegsweden/natmeg_utils)

## Prerequisits
Ensure you have the following non-default libraries installed in your Python environment: `mne`, `matplotlib`

## Process

### Install requirements

1. Make sure python modules are installed in the environment. If not, install them using the following commands:

```bash
conda install mne matplotlib
```

### Run script

Option 1. Run the script by executing the following command:

```bash
python maxfilter.py --config=path/to/maxfilter_settings.json
```
This will run the script with the config file wihout further questions.

Option 2. Edit config file before running the script:

```bash
python maxfilter.py --config=path/to/maxfilter_settings.json --edit
```
This will open a dialog for you to edit the config file before running the script.

Option 3. Run the script without a config flag
```bash
python maxfilter.py # (add --edit to also edit an existing file)
```
You will get three options in the terminal
- `open`: Open an existing config file (default)
- `new`: Create a new config file from a default template using the dialog
- `cancel`: Cancel the operation

### Config file

```json
{
"standard_settings": {
    "project_name": "",
    "trans_conditions": ["task1", "task2"],
    "trans_option": "mne_continous",
    "merge_runs": "on",
    "empty_room_files": ["empty_room_before.fif", "empty_room_after.fif"],
    "sss_files": ["empty_room_before.fif", "empty_room_after.fif"],
    "autobad": "on",
    "badlimit": 7,
    "bad_channels":[""],
    "tsss_default": "on",
    "correlation": 0.98,
    "movecomp_default": "on",
    "data_path": "."
    },

"advanced_settings": {
    "force": "off",
    "downsample": "off",
    "downsample_factor": 4,
    "apply_linefreq": "off",
    "linefreq_Hz": 50,
    "scripts_path": "/home/natmeg/Scripts",
    "cal": "/neuro/databases/sss/sss_cal.dat",
    "ctc": "/neuro/databases/ctc/ct_sparse.fif",
    "dst_path": "neuro/data/local",
    "trans_folder": "headtrans",
    "log_folder": "log",
    "maxfilter_version": "/neuro/bin/util/mfilter",
    "MaxFilter_commands": "",
    }
}
```

Standard_settings:

- `project_name`: Name of the project
- `trans_conditions`: List of conditions to be transformed
- `trans_option`: Type of transformation (continous or initial)
- `merge_runs`: Estimate head position average over all runs if multiple
- `empty_room_files`: List of empty room files
- `sss_files`: List of SSS files
- `autobad`: Turn on or off autobad
- `badlimit`: Bad limit
- `bad_channels`: List of bad channels
- `tsss_default`: Turn on or off tSSS
- `correlation`: Correlation limit
- `movecomp_default`: Turn on or off movecomp
- `data_path`: Path to the data

Advanced_settings:

- `force`: Force maxfilter to run
- `downsample`: Downsample data
- `downsample_factor`: Downsample factor
- `apply_linefreq`: Apply line frequency filter
- `linefreq_Hz`: Line frequency in Hz
- `scripts_path`: Path to the script
- `cal`: Path to the calibration file
- `ctc`: Path to the crosstalk file
- `dst_path`: Path to the destination folder (not active yet)
- `trans_folder`: Name of the transformation folder
- `log_folder`: Name of the log folder
- `maxfilter_version`: Path to the maxfilter version
- `MaxFilter_commands`: Additional commands for maxfilter (see MaxFilter manual)