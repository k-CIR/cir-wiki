---
title: NatMEG Processing Pipeline Utility Scripts
---

# NatMEG Processing Pipeline

Comprehensive MEG/EEG preprocessing pipeline for NatMEG data including copying of data, MaxFilter processing, HPI coregistration, BIDS conversion, and data synchronization utilities.

Scripts and further information can be found at the [NatMEG-utils GitHub repository](https://github.com/k-CIR/NatMEG-utils)

## Overview

This pipeline provides end-to-end processing for:
- **TRIUX/SQUID MEG** data from Elekta systems
- **OPM MEG** data from Kaptah/OPM systems  
- **EEG** data collected through TRIUX

## Key Features

- **Interactive HTML Dashboard**: Generate comprehensive project reports with hierarchical file trees, local/remote comparison, and interactive filtering
- **Server Synchronization**: Automated sync to CIR server with rsync, supporting include/exclude patterns and dry-run mode
- **Enhanced CLI Interface**: Modular subcommands for individual pipeline steps (run, copy, hpi, maxfilter, bidsify, sync, report)
- **Flexible Installation**: Improved install.sh script with conda/venv options and cross-platform support
- **Automated Configuration**: Generate default config files with `natmeg create-config`


## The config file by section

### RUN
The steps to include in `natmeg run --config <config_file.yml>`, toggle between true/false to include/exclude steps.
```yml
RUN:
  Copy to Cerberos: true
  Add HPI coregistration: true
  Run Maxfilter: true
  Run BIDS conversion: true
  Sync to CIR: true
```
### Project
General project paths and information. Make sure to set the correct paths for your data storage locations. 

- If using GUI project Name and Root will update Raw and BIDS paths if not manually set.
- Calibration and Crosstalk paths refer to in Project copies of these files, original locations are set in `copy_to_cerberos.py` script.
- Since project names can differ between Sinuhe/Kaptah and local storage, set the correct paths for your project on both systems by replacing the place holders.
```yml
Project:
  Name: ''
  CIR-ID: ''
  InstitutionName: Karolinska Institutet
  InstitutionAddress: Nobels vag 9, 171 77, Stockholm, Sweden
  InstitutionDepartmentName: Department of Clinical Neuroscience (CNS)
  Description: project for MEG data
  Tasks:
  - ''
  Sinuhe raw: /neuro/data/sinuhe/<project_path_on_sinuhe> 
  Kaptah raw: /neuro/data/kaptah/<project_path_on_kaptah>
  Root: /neuro/data/local/
  Raw: /neuro/data/local/<project>/raw
  BIDS: /neuro/data/local/<project>/BIDS
  Calibration: /neuro/data/local/<project>/databases/sss/sss_cal.dat
  Crosstalk: /neuro/data/local/<project>/databases/ctc/ct_sparse.fif
  Logfile: pipeline_log.log
```
### OPM
```yml
OPM:
  polhemus:
  - ''
  hpi_names:
  - HPIpre
  - HPIpost
  - HPIbefore
  - HPIafter
  frequency: 33
  downsample_to_hz: 1000
  overwrite: false
  plot: false
```
### MaxFilter
Default settings. 

- Add all files for which you want continous head positioning estimation in `trans_conditions`
- If you do not have empty room files, leave the list empty `- ''`
- Add project bad channels in `bad_channels` list, one per line, or leave empty `- ''`
```yml
MaxFilter:
  standard_settings:
    trans_conditions:
    - ''
    trans_option: continous
    merge_runs: true
    empty_room_files:
    - empty_room_before.fif
    - empty_room_after.fif
    sss_files:
    - ''
    autobad: true
    badlimit: '7'
    bad_channels:
    - ''
    tsss_default: true
    correlation: '0.98'
    movecomp_default: true
    subjects_to_skip:
    - ''
  advanced_settings:
    force: false
    downsample: false
    downsample_factor: '4'
    apply_linefreq: false
    linefreq_Hz: '50'
    maxfilter_version: /neuro/bin/util/maxfilter
    MaxFilter_commands: ''
    debug: false
```
### BIDS
BIDS conversion settings. Make sure to set the correct paths for your files and project information. Example `participant_mapping_example.csv`.

- The `bids_conversion.tsv` is generated if not already existing and controls the conversion. Edit task names and runs, and set status to `ok`. BIDS conversion will not be done if there are any file has status `check`.

```yml
BIDS:
  Dataset_description: dataset_description.json
  Participants: participants.tsv
  Participants_mapping_file: participant_mapping_example.csv
  Conversion_file: bids_conversion.tsv
  Overwrite_conversion: false
  Original_subjID_name: old_subject_id
  New_subjID_name: new_subject_id
  Original_session_name: old_session_id
  New_session_name: new_session_id
  overwrite: false
  dataset_type: raw
  data_license: ''
  authors: ''
  acknowledgements: ''
  how_to_acknowledge: ''
  funding: ''
  ethics_approvals: ''
  references_and_links: ''
  doi: doi:<insert_doi>
```

## Pipeline Components

### 1. Data Synchronization (`copy_to_cerberos.py`)
Synchronizes raw data between storage systems (Sinuhe/Kaptah → Cerberos).

### 2. HPI Coregistration (`add_hpi.py`)
Performs head localization for OPM-MEG using HPI coils and Polhemus digitization.


### 3. MaxFilter Processing (`maxfilter.py`)
Applies Elekta MaxFilter with Signal Space Separation (SSS) and temporal extension (tSSS).


### 4. BIDS Conversion (`bidsify.py`)
Converts NatMEG data to BIDS format and organizes it into a BIDS-compliant folder structure.

### 5. Server Synchronization (`sync_to_cir.py`)
Synchronizes processed data to CIR server using `rsync` with include/exclude patterns and dry-run mode.

## Installation

### Automated Installation (Recommended)

The NatMEG pipeline includes an automated installation script that sets up everything you need:

#### Default Installation (Conda Environment)
```bash
# Clone the repository
git clone https://github.com/NatMEG/NatMEG-utils.git
cd NatMEG-utils

# Run the installer (uses conda by default)
bash install.sh

# View all installer options
bash install.sh --help
```

#### Alternative Installation (Python Virtual Environment)

Note: Does not work on all Linux distributions (e.g. Rocky/RHEL/CentOS) due to PyQt compatibility issues. Use default conda installation instead.

```bash
# Clone the repository
git clone https://github.com/NatMEG/NatMEG-utils.git
cd NatMEG-utils

# Run the installer with venv flag
bash install.sh --venv
```**Benefits of conda installation (now default):**
- **Better PyQt Compatibility**: Provides isolated Python environment that avoids system conflicts
- **Linux Compatibility**: Works well on enterprise Linux distributions (Rocky/RHEL/CentOS)
- **Dependency Isolation**: Prevents conflicts with system-installed Python packages
- **Reliability**: More consistent installation experience across different systems

The installer will:
- Detect your operating system (macOS/Linux) and conda installation  
- Create a `natmeg` executable in `~/.local/bin/`
- Add `~/.local/bin` to your PATH if needed
- Set up either Python venv or conda environment based on your choice
- Provide clear troubleshooting instructions

After installation, you can use the pipeline from anywhere:
```bash
natmeg gui                     # Launch GUI
natmeg run --config config.yml # Run pipeline
natmeg --help                  # Show all options
```

### Manual Installation

If you prefer manual setup:

#### Option 1: Conda Environment (Recommended for Linux Rocky)
```bash
# Create basic conda environment
conda create -n natmeg_utils python>=3.12 pip uv -y
conda activate natmeg_utils

# Install dependencies via pip (same as venv approach)
pip install -r requirements.txt
```

#### Option 2: Python Virtual Environment
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

#### 3. Add to PATH (Optional)
```bash
# Add repository to PATH for global access
echo 'export PATH="$HOME/Sites/NatMEG-utils:$PATH"' >> ~/.zshrc  # or ~/.bashrc
source ~/.zshrc
```

### Prerequisites

- **Python 3.12+**: Required for all pipeline components
- **Conda/Miniconda**: Recommended for environment management
- **Git**: For cloning the repository
- **Operating System**: macOS or Linux (Windows support coming soon)

## Quick Start

> **Note**: Install the pipeline first using `bash install.sh` (see [Installation](#installation) section above)

### Using the natmeg Command

After installation, you can use the `natmeg` command from anywhere:

```bash

# Launch GUI configuration interface
natmeg gui # Loads a default configuration file if none specified

# Create configuration file
natmeg create-config --output my_config.yml  # Generate default config

# Run complete pipeline with options
natmeg run --config config.yml               # Complete pipeline
natmeg run --config config.yml --dry-run     # Preview without execution
natmeg run --config config.yml --no-report   # Skip final HTML report
natmeg run --config config.yml --delete      # Delete remote files not in source

# Run individual components
natmeg copy --config config.yml              # Data synchronization only
natmeg hpi --config config.yml               # HPI coregistration only  
natmeg maxfilter --config config.yml         # MaxFilter processing only
natmeg maxfilter --config config.yml --dry-run  # Show commands without execution
natmeg bidsify --config config.yml           # BIDS conversion only

# Server synchronization with advanced options
natmeg sync --create-config                  # Generate example server config
natmeg sync --server-config servers.yml --test      # Test server connection
natmeg sync --directory /data/project        # Sync directory (default 'cir' server)  
natmeg sync --config project_config.yml --dry-run   # Preview sync from project config
natmeg sync --directory /data/project --delete      # Delete remote files not in source
natmeg sync --directory /data/project --exclude "*.tmp" --include "*.fif"  # Pattern filtering

# Generate project reports
natmeg report --config config.yml            # Generate HTML dashboard

# Show help for all commands
natmeg --help
natmeg run --help      # Detailed help for specific subcommand
```

## Troubleshooting

### Installation Issues

**PyQt Issues on Linux Rocky/RHEL:**
```bash
# Default conda installation should work out of the box
bash install.sh

# If you previously used venv and had issues, conda is now default
# Creates isolated Python environment avoiding system conflicts
```

**Conda not found:**
```bash
# Install conda first
# macOS:
brew install miniconda
# or download from: https://docs.conda.io/en/latest/miniconda.html

# Linux:
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

**natmeg command not found:**
```bash
# Check if ~/.local/bin is in PATH
echo $PATH

# If not, add it to your shell config
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc  # or ~/.bashrc
source ~/.zshrc
```

**Environment activation fails:**
```bash
# For conda environments (default)
conda env list
conda env remove -n natmeg_utils -y  # Remove corrupted environment
bash install.sh  # Recreate with conda (default)

# For virtual environments  
rm -rf .venv  # Remove corrupted environment
bash install.sh --venv  # Recreate with venv
```

### Platform-Specific Issues

**Linux Rocky/RHEL/CentOS - PyQt GUI Issues:**

The GUI may fail to start on enterprise Linux distributions due to PyQt compatibility issues with system libraries. **Solution: Use conda installation**

```bash
# Recommended approach
bash install.sh --conda

# If already installed with pip/venv, switch to conda:
cd ~/Sites/NatMEG-utils
bash install.sh --conda  # This will replace the existing installation
```

**Why conda is now the default:**
- Provides isolated Python environment separate from system Python
- No conflicts with system-installed Python packages
- Better compatibility across different operating systems and distributions
- Same requirements.txt installation but in isolated conda environment
- Resolves PyQt issues commonly seen with system Python installations

### Runtime Issues

**Module import errors:**
```bash
# For conda environments
conda activate natmeg_utils
conda list  # Check installed packages

# For virtual environments
source .venv/bin/activate
pip list  # Check installed packages

# Install missing dependencies
pip install mne mne-bids pyyaml
```

**Permission errors:**
```bash
# Make natmeg executable
chmod +x ~/.local/bin/natmeg

# Check file permissions
ls -la ~/.local/bin/natmeg
```

**Terminal crashes:**
The natmeg script includes safety checks to prevent terminal crashes. If issues persist:
```bash
# View the generated script
cat ~/.local/bin/natmeg

# Regenerate with latest safety checks
cd ~/Sites/NatMEG-utils
bash install.sh
```

---

## Contributions

Improvements are welcomed! The pipeline includes robust installation and execution scripts that work across different environments.

**Development Guidelines:**
- Do not change scripts locally for personal use
- Follow GitHub conventions: create branches or fork the repository
- Make pull requests for any modifications
- Test installation script on both macOS and Linux before submitting changes
- Ensure compatibility with different conda installations and shell environments

**Testing the Installation:**
```bash
# Test on clean environment
bash install.sh

# Verify functionality
natmeg --help
natmeg gui
```
