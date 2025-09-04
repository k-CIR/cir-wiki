---
title: NatMEG Processing Pipeline Utility Scripts
---

# NatMEG Processing Pipeline

Comprehensive MEG/EEG preprocessing pipeline for NatMEG data including BIDS conversion, MaxFilter processing, HPI coregistration, and data synchronization utilities.

Note: The last step, to push project to the CIR-server, is not yet included. Also everything is in devlopment mode so feedback and improvements are welcome.

Read full documentation on how to use the pipeline [here](https://k-cir.github.io/cir-wiki/natmeg/preprocessing)

## Overview

This pipeline provides end-to-end processing for:
- **TRIUX/SQUID MEG** data from Elekta systems
- **OPM MEG** data from Kaptah/OPM systems  
- **EEG** data collected through TRIUX

## Installation

### Automated Installation (Recommended)

The NatMEG pipeline includes an automated installation script that sets up everything you need:

```bash
# Clone the repository
git clone git@github.com:k-CIR/NatMEG-utils.git
cd NatMEG-utils

# Run the installer
bash install.sh
```

The installer will:
- Detect your operating system (macOS/Linux) and conda installation
- Create the conda environment `natmeg_utils`
- Create a `natmeg` executable in `~/.local/bin/`
- Add `~/.local/bin` to your PATH if needed
- Guide you through conda environment setup 
- Provide clear troubleshooting instructions

After installation, you can use the pipeline from anywhere:
```bash
natmeg gui                     # Launch GUI
natmeg run --config config.yml # Run pipeline
natmeg --help                  # Show all options
```

### Manual Installation

If you prefer manual setup:

#### 1. Create Conda Environment
```bash
conda create -n natmeg_utils python=3.9 -y
conda activate natmeg_utils
```

#### 2. Install Dependencies
```bash
# Core dependencies
conda install mne mne-bids numpy pandas matplotlib pyyaml

# Optional dependencies for advanced features
pip install json5  # For JSON files with comments

# Install pipeline in development mode
pip install -e .
```

#### 3. Add to PATH (Optional)
```bash
# Add repository to PATH for global access
echo 'export PATH="$HOME/Sites/NatMEG-utils:$PATH"' >> ~/.zshrc  # or ~/.bashrc
source ~/.zshrc
```

### Prerequisites

- **Python 3.9+**: Required for all pipeline components
- **Conda/Miniconda**: Recommended for environment management
- **Git**: For cloning the repository
- **Operating System**: macOS or Linux (Windows support coming soon)

## Quick Start

> **Note**: Install the pipeline first using `bash install.sh` (see [Installation](#installation) section above)

### Using the natmeg Command

After installation, you can use the `natmeg` command from anywhere:

```bash
# Launch GUI configuration interface
natmeg gui

# Run complete pipeline
natmeg run --config config.yml

# Run specific components
natmeg copy --config config.yml      # Data synchronization only
natmeg hpi --config config.yml       # HPI coregistration only  
natmeg maxfilter --config config.yml # MaxFilter processing only
natmeg bidsify --config config.yml   # BIDS conversion only

# Show help
natmeg --help
```

### Legacy Direct Script Usage

You can still run scripts directly if needed:

#### 1. GUI Configuration Interface
Launch the unified configuration interface:
```bash
python run_config.py
```
This opens a tabbed GUI for setting up all pipeline components with integrated execution.

#### 2. Complete Pipeline
Run the entire pipeline programmatically:
```bash
python natmeg_pipeline.py --config config.yml
```
Or use the GUI to first edit the configuration and then execute the pipeline.
```bash
python natmeg_pipeline.py
```

#### 3. Individual Components
Run specific processing steps:
```bash
# Data synchronization
python copy_to_cerberos.py --config config.yml

# HPI coregistration (OPM only)
python add_hpi.py --config config.yml

# MaxFilter processing
python maxfilter.py --config config.yml

# BIDS conversion
python bidsify.py --config config.yml
```

---

## Configuration

### Unified YAML Configuration
All pipeline components use a single YAML configuration file:

```yaml
# Project and data paths
project:
  squidMEG: /neuro/data/sinuhe/project_name
  opmMEG: /neuro/data/kaptah/project_name
  BIDS: /neuro/data/local/project_name/bids
  Calibration: /neuro/databases/sss/sss_cal.dat
  Crosstalk: /neuro/databases/ctc/ct_sparse.fif
  tasks: ["Noise", "RSEO", "RSEC", "AudOdd", "Phalanges"]

# BIDS conversion settings
bids:
  Dataset_description: dataset_description.json
  Participants: participants.tsv
  Participants_mapping_file: participant_mapping.csv
  Conversion_file: bids_conversion.tsv
  Overwrite_conversion: false
  Original_subjID_name: old_subject_id
  New_subjID_name: new_subject_id
  Original_session_name: old_session_id
  New_session_name: new_session_id
  dataset_type: raw
  overwrite: false

# MaxFilter processing
maxfilter:
  standard_settings:
    project_name: project_name
    trans_conditions: ["AudOdd", "Phalanges", "RSEO", "RSEC"]
    trans_option: continous
    merge_runs: true
    empty_room_files: ["empty_room_before.fif", "empty_room_after.fif"]
    autobad: true
    badlimit: 7
    tsss_default: true
    correlation: 0.98
    movecomp_default: true
    data_path: /neuro/data/sinuhe
  advanced_settings:
    force: false
    downsample: false
    downsample_factor: 4
    cal: /neuro/databases/sss/sss_cal.dat
    ctc: /neuro/databases/ctc/ct_sparse.fif

# OPM HPI coregistration
opm:
  polhemus: ["RestinState.fif"]
  hpi_names: ["HPI01", "HPI02", "HPI03", "HPI04", "HPI05"]
  hpifreq: 33.0
  downsample_freq: 1000
  overwrite: false
  plot: true

# Pipeline execution control
RUN:
  Copy to Cerberos: false
  Add HPI coregistration: false
  Run Maxfilter: false
  Bidsify: true
```

### Legacy JSON Support
Individual components still support legacy JSON configuration files for backward compatibility.

---

## Pipeline Components

### 1. Data Synchronization (`copy_to_cerberos.py`)

Synchronizes raw data between storage systems (Sinuhe/Kaptah → Cerberos).

**Features:**
- Intelligent file comparison (size, timestamp, content)
- FIF-specific handling for MEG/EEG data to split large files into 2GB chunks
- Parallel processing for large datasets
- Comprehensive logging and error handling

**Usage:**
```bash
python copy_to_cerberos.py --config config.yml
```

### 2. HPI Coregistration (`add_hpi.py`)

Performs head localization for OPM-MEG using HPI coils and Polhemus digitization.

**Features:**
- Sequential HPI coil activation and localization
- Magnetic dipole fitting in device coordinates
- Coordinate transformation using fiducial points
- Quality control with goodness-of-fit metrics
- 3D visualization of sensor arrays and coil positions
- Parallel processing of multiple files

**Key Functions:**
- `find_hpi_fit()`: Localizes HPI coils using sequential activation
- `process_single_file()`: Applies transformations to individual files
- Quality threshold: Goodness of fit >0.9 for reliable localization

**Usage:**
```bash
python add_hpi.py --config config.yml
```

### 3. MaxFilter Processing (`maxfilter.py`)

Applies Elekta MaxFilter with Signal Space Separation (SSS) and temporal extension (tSSS).

**Features:**
- Continous head position averaging and movement compensation
- Temporal SSS for interference suppression
- Bad channel detection and correction
- Empty room processing for noise estimation
- Task-specific parameter configuration
- Parallel processing across subjects/sessions

**Key Processing Steps:**
1. **Head Position Averaging**: Continuous HPI-based localization
2. **Movement Compensation**: Correction of head movement artifacts
3. **Temporal SSS**: Removal of external interference
4. **Bad Channel Handling**: Detection and interpolation of bad channels
5. **Empty Room Correction**: Estimation and subtraction of environmental noise

**Usage:**
```bash
python maxfilter.py --config config.yml
```

### 4. BIDS Conversion (`bidsify.py`)

Converts NatMEG data to BIDS format and organizes it into a BIDS-compliant folder structure.

**Features:**
- Automatic conversion of MEG, EEG, and OPM data to BIDS
- Generation of BIDS metadata files (e.g., `dataset_description.json`, `participants.tsv`)
- Flexible configuration for file mapping and naming
- Integration with MNE-BIDS for robust BIDS compliance
- Conversion table for tracking and managing file conversions define comprehensive task names and identify runs

**Usage:**
```bash
python bidsify.py --config config.yml
```

---

## Special Features

- EEG data will be placed in an `eeg` folder in the BIDS root directory according to BIDS specifications. However, as EEG data is collected through the TRIUX system a `.fif` file will be created and the `.json` sidecare will be copied to the `meg` folder.

---

## Troubleshooting

### Installation Issues

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
# Check conda environments
conda env list

# Recreate environment if needed
conda remove -n natmeg_utils --all -y
conda create -n natmeg_utils python=3.9 -y
conda activate natmeg_utils
cd ~/Sites/NatMEG-utils
pip install -e .
```

### Runtime Issues

**Module import errors:**
```bash
# Ensure you're in the correct environment
conda activate natmeg_utils

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
