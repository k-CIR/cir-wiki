---
title: File Conversion Tools
---

## Installing Conversion Software

For converting anatomical MR files to BIDS, we will use `dcm2niix`, and for converting PET files to BIDS, we will use `PET2BIDS`.  To use `PET2BIDS`, we will first install Python and conda (although PET2BIDS can also be used with MATLAB - see the [full documentation](https://pet2bids.readthedocs.io/en/latest/index.html#) for details).

### Python

#### Windows

1. Install Python

    1. Download the latest Python installer from [python.org](https://www.python.org/downloads/windows/)
    2. Run the installer
    3. **Important**: Check "Add Python to PATH"
    4. Select "Install Now"

2. Install Miniconda

    1. Download Miniconda from [conda.io](https://docs.conda.io/en/latest/miniconda.html)
    2. Run the installer
    3. Accept the license agreement
    4. Select "Just Me" when asked who to install for
    5. Choose a destination folder (the default is fine)
    6. For Advanced Options, you can leave them as they are
    7. Click "Install"

3. For future steps, when using the terminal, use the "Anaconda Prompt". You will find it in your start menu.

#### Linux (Ubuntu/Debian)

1. Install Python (if not already installed)

    1. Open Terminal
    2. Update package lists and install Python:
   ```
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

2. Install Miniconda

    1. Download Miniconda:
       ```
       wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
       ```
    2. Make the installer executable:
       ```
       chmod +x Miniconda3-latest-Linux-x86_64.sh
       ```
    3. Run the installer:
       ```
       ./Miniconda3-latest-Linux-x86_64.sh
       ```
    4. Follow the prompts, accept the license agreement
    5. Allow the installer to initialize Miniconda

### PET2BIDS

[PET2BIDS](https://github.com/openneuropet/PET2BIDS) is a well-validated tool for converting ecat7 (`.v`) and DICOM (`.dcm`) files to BIDS files.

Assuming Python and conda (or miniconda) are already installed, we start by creating and activating a PETBIDS environment. Remember that in Windows, you need to be using the "Anaconda Prompt".

```
conda create --name PETBIDS python=3.10
conda activate PETBIDS
```

And then we can proceed to install the PET2BIDS software

```{bash}
pip install pypet2bids
```

The full package documentation can be found [here](https://pet2bids.readthedocs.io/en/latest/index.html#).

### dcm2niix

dcm2niix can also be installed using `conda` as follows:

```
conda install -c conda-forge dcm2niix
```

To check if dcm2niix is installed correctly:

1. Open a terminal (Command Prompt, Terminal, etc.)
2. Type `dcm2niix -h` and press Enter
3. You should see the help message with usage instructions

