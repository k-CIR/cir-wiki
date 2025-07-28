---
title: Preprocessing Pipeline
---

## NatMEG Preprocessing Utils

Comprehensive MEG/EEG preprocessing pipeline for NatMEG data including BIDS conversion, MaxFilter processing, HPI coregistration, and data synchronization utilities. For detailed preprocessing instructions and utilities, see the [NatMEG-utils repository](https://github.com/k-CIR/NatMEG-utils).

## Components

### 1. Data Synchronization

Synchronizes raw data between storage systems (Sinuhe/Kaptah → Cerberos).

Features:

- Intelligent file comparison (size, timestamp, content)
- FIF-specific handling for MEG/EEG data to split large files into 2GB chunks
- Parallel processing for large datasets
- Comprehensive logging and error handling

### 2. OPM HPI Coregistration

Performs head localization for OPM-MEG using HPI coils and Polhemus digitization.

Features:

- Sequential HPI coil activation and localization
- Magnetic dipole fitting in device coordinates
- Coordinate transformation using fiducial points
- Quality control with goodness-of-fit metrics
- 3D visualization of sensor arrays and coil positions
- Parallel processing of multiple files

### 3. MaxFilter Processing

Applies Elekta MaxFilter with Signal Space Separation (SSS) and temporal extension (tSSS) on squidMEG data.

Features:

- Continous head position averaging and movement compensation
- Temporal SSS for interference suppression
- Bad channel detection and correction
- Empty room processing for noise estimation
- Task-specific parameter configuration
- Parallel processing across subjects/sessions

### 4. BIDS Conversion

Converts NatMEG data to BIDS format and organizes it into a BIDS-compliant folder structure.

Features:

- Automatic conversion of MEG, EEG, and OPM data to BIDS
- Generation of BIDS metadata files (e.g., dataset_description.json, participants.tsv)
- Flexible configuration for file mapping and naming
- Integration with MNE-BIDS for robust BIDS compliance
- Conversion table for tracking and managing file conversions define comprehensive task names and identify runs
