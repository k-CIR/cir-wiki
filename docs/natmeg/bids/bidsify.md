---
title: BIDS for MEG at NatMEG
---

# Bidsify
To promote the use of BIDS and simplify the implementation on the data collected at NatMEG this pipeline was created.

The source scripts are available on the cir server (TBA), but can also be downloaded from the [NatMEG-utils GitHub repository](https://github.com/k-CIR/NatMEG-utils)

This `bidsify.py` script converts data from NatMEG (MEG, EEG, OPM) to BIDS format and organizes the data into a BIDS-compliant folder structure. The script is designed to work with data collected at NatMEG and uses the MNE-BIDS library.

## Prerequisits
Ensure you have the following non-defualt libraries installed in your Python environment: `mne`, `mne_bids`, `numpy`, `pandas`

### Install requirements
1. Make sure python modules are installed in the environment. If not, install them using the following commands:

```bash
conda install mne mne-bids
```

## Process

### Components 

Generally there are three steps in the conversion process:

1. [**Create a configuration file**](#config-file): The script will prompt you to create a configuration file if it does not exist. This file contains paths to the raw data, BIDS folder, calibration and crosstalk files, and other parameters needed for the conversion.
2. [**Create a conversion table**](#the-conversion-table): The script creates a conversion table that estimates task names, processing, and other parameters to create the BIDS-compliant file name. Before running the conversion you should check task names and other parameters in the conversion table. 
3. **Convert the data**: The script converts the data to BIDS according the to the conversion table. The script will also create a `dataset_description.json` file and a `participants.tsv` file if they do not already exist.

### Usage

```bash
python bidsify.py [--help] [--config CONFIG] [--edit] [--conversion CONVERSION] [--overwrite]
```
### Options

- `--help`: Show help message and exit.
- `--config`: Path to the configuration file. If not provided, a you will be promted in the terminal to create a new or open an existing one.
- `--edit`: Open a dialog to edit the configuration file before running the script.
- `--conversion`: Path to the conversion file. If not provided, the latest conversion file will be used.
- `--overwrite`: Overwrite last conversion file and create a new one. This will not overwrite the conversion table but create a new one with the same name as the last one with a timestamp.

### Config file

A configuration file is needed and you will be prompted to create a defaul file if it does not exist. You will be promted to open an existing config file or create a new one. The default template will be created in the current working directory. You can also point to an existing config file the `--config` flag. Edits can be made to the config file by using the `--edit` flag or by opening the json-file in a text editor.

#### Default config file

```json
{   
    "Tasks": [""],
    "squidMEG": "/neuro/data/sinuhe/<project_on_sinuhe>",
    "opmMEG": "/neuro/data/kaptah/<project_on_kaptah>",
    "BIDS": "/neuro/data/local/<project_on_local>",
    "Calibration": "/neuro/databases/sss/sss_cal.dat",
    "Crosstalk": "/neuro/databases/ctc/ct_sparse.fif",
    "Dataset_description": "dataset_description.json",
    "Participants": "participants.tsv",
    "Participants mapping file": "/neuro/data/local/<project>/mapping.csv",
    "Original subjID name": "old_subject_id",
    "New subjID name": "new_subject_id",
    "Original session name": "old_session_id",
    "New session name": "new_session_id",
    "Overwrite": "off"
}
```

#### Description

- `Tasks`: List of tasks to be included in the conversion. This is used as a check to match the intended task names with the task names in the raw data. If a task is misspelled or missing it will be flagged in the conversion table and you will be prompted to edit the conversion table before continuing.
- `squidMEG`: Path to the raw data folder for SQUID MEG data
- `opmMEG`: Path to the raw data folder for OPM MEG data
- `BIDS`: Path to the BIDS folder where the data will be saved
- `Calibration`: Path to the calibration file
- `Crosstalk`: Path to the crosstalk file
- `Dataset_description`: Path to the dataset_description.json file in the BIDS folder
- `Participants`: Path to the participants.tsv file in the BIDS folder
- `Participants mapping file`: Path to the mapping file that contains the original and new subject IDs
- `Original subjID name`: Name of the column in the mapping file that contains the original subject ID
- `New subjID name`: Name of the column in the mapping file that contains the new subject ID
- `Original session name`: Name of the column in the mapping file that contains the original session ID
- `New session name`: Name of the column in the mapping file that contains the new session ID
- `Overwrite`: If set to "on", the script will overwrite existing files in the BIDS folder

### The conversion table
A conversion table will be created when running `bidsify.py`. This conversion file estimates task names, processing, and other parameters to create the bidsified file name. The conversion table is then looped through, skipping split-files and already converted files. By editing the lates file, you can change deviant task names, and decide to whether to run the conversion on a specific file or not. The conversion table is saved in the conversion_logs folder as `conversion_logs/<date_of_creation>_bids_conversion.tsv`. By default the latest file will be used but you can also select your own file by adding the `--conversion` flag to the command line.

#### Header description

- `time_stamp`: The timestamp when the original conversion file was created.
- `run_conversion`: Indicates whether the conversion should be executed (`yes` or `no`). Will automatically changed to `no` after file conversion.
- `task_flag`: Flag `ok` if task name matches expected task name, else `check`.
- `participant_from`: The original participant ID.
- `participant_to`: The new participant ID after mapping.
- `session_from`: The original session ID.
- `session_to`: The new session ID after mapping.
- `task`: The task name associated with the file.
- `split`: Indicates if the file is a split file.
- `run`: If more than one occurence of a task in the same session this should be set modifided manually.
- `datatype`: The type of data according to BIDS (e.g., `meg`, `eeg`).
- `acquisition`: Acquisition device.
- `processing`: Pre-processing details for the data, eg. MaxFilter.
- `raw_path`: The path to the raw data file.
- `raw_name`: The name of the raw data file.
- `bids_path`: The path where the BIDS-compliant file will be saved.
- `bids_name`: The name of the BIDS-compliant file. This will be adjusted after the conversion.

### Run script examples

/// tab | Example 1

**Run the script without flags**
```bash
python bidsify.py
```
You will get three options in the terminal
- `open`: Open an existing config file (default)
- `new`: Create a new config file from a default template using the dialog
- `cancel`: Cancel the operation


Given all tasks in the conversion passes the checks, the script will run and create a BIDS-compliant folder structure in the specified BIDS folder. The script will also create a `dataset_description.json` file and a `participants.tsv` file if they do not already exist.

If `task_flag` is `check`. You will be prompted to edit the conversion table before continuing. This is to ensure that the task name is correct and that the file is not a split file. If you are sure that the task name is correct, you can set the task_flag to `ok` and continue with the conversion.

Common changes to the conversion table are:

- `EmtpyRoom`. Noise recordings should include the word `empty` or `noise` in the filename. Correct spelling mistake and set task_flag to `ok`.
- `WorkingMemory1`. You probably needed to stop the recording in the middle of a paradigm. The first one might be named `WorkingMemory`. Change both task names to `WorkingMemory` and set `run` to `1` or `2` depending on the order of the recordings. Change the task_flag to `ok` and run the conversion.

///

/// tab | Example 2

**Run the script with config flag**

```bash
python bidsify.py --config=my_project/my_bids_config_file.json
```
This will run the script with the config file without further questions using the latest created conversion table or create a new.

Given all tasks in the conversion passes the checks, the script will run and create a BIDS-compliant folder structure in the specified BIDS folder.
///

/// tab | Example 3

**Edit config file before running the script**

```bash
python bidsify.py --config=path/to/name_of_config.json --edit
```
This will open a dialog for you to edit the config file before running the script.

Given all tasks in the conversion passes the checks, the script will run and create a BIDS-compliant folder structure in the specified BIDS folder.
///

/// tab | Example 4

**Run the script with a specific config and conversion file**

```bash
python bidsify.py --config=path/to/name_of_config.json --conversion=path/to/conversion_file.csv
```
Runs conversion without any further questions using a specific conversion file.

Given all tasks in the conversion passes the checks, the script will run and create a BIDS-compliant folder structure in the specified BIDS folder.

///

/// tab | Example 5

**Run the script with a specific config and conversion file and overwrite the conversion table**

```bash
python bidsify.py --config=path/to/name_of_config.json --conversion=path/to/conversion_file.csv --overwrite
```
Runs conversion without any further questions using a specific conversion file and overwrites the conversion table. This will not overwrite the conversion table but create a new one with the same name as the last one with a timestamp.

Given all tasks in the conversion passes the checks, the script will run and create a BIDS-compliant folder structure in the specified BIDS folder.

///

## Naming conventions
Although the script is written to handle various breaches of naming convensions, it is not yet water tight. The following naming conventions are recommended:

- Do not use numbers in your task name when saving your raw data.  
- Do not use `_` in the file-name. Tasks named `my_great_task` will be renamed to `MyGreatTask`.
- Empty room recordings should include the word `empty` or `noise` in the filename followed by `before` or `after` to indicate if it was recorded before or after the experiment.
- Resting state should be begin with `rest`, conversions for resting state names like `RS` is not yet implemented.

## Special features

- EEG data will be placed in an `eeg` folder in the BIDS root directory according to BIDS specifications. However, as EEG data is collected through the TRIUX system a `.fif` file will be created and the `.json` sidecare will be copied to the `meg` folder.
