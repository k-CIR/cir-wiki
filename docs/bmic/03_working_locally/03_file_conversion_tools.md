---
title: File Conversion Tools
---

## Installing Conversion Software

For converting anatomical MR files to BIDS, we will use `dcm2niix`, and for converting PET files to BIDS, we will use `PET2BIDS`.  To use `PET2BIDS`, we will first install Python and conda (although PET2BIDS can also be used with MATLAB - see the [full documentation](https://pet2bids.readthedocs.io/en/latest/index.html#) for details).

**Note:** For Windows users, many of these tools *can* be run with Windows directly, but with some difficulty. It is easier to run everything using Linux directly through the Windows Subsystem for Linux (WSL).

### WSL (Windows users)

I recommend using WSL with Ubuntu 22.04, because FreeSurfer has not yet been made available for Ubuntu 24.04 (which is the default WSL distribution).

1. Open PowerShell as Administrator
   - Search for PowerShell in the Start menu
   - Right-click and select "Run as administrator"

2. Install WSL with Ubuntu
   ```powershell
   wsl --install -d Ubuntu-22.04
   ```
   This command installs WSL with Ubuntu as the default distribution. The system will require a restart.

3. After restart, Ubuntu will finish setup
   - When prompted, create a username and password for your Linux distribution
   - This doesn't need to match your Windows credentials

4. To open Ubuntu, search for Ubuntu in the Start menu

**Note:** To understand where things are using WSL, your local drives are listed as mounted drives. You can find them in the `/mnt` folder.  So the contents of your C:\ are at `/mnt/c/`.  Note that for network drives, this can be a bit of a pain. I recommend doing processing locally and copying the files later to the network drive, but if you do wish to mount the network drive directly, you can follow the guide under BMIC > Getting Started > Mounting Network Drives (and follow the instructions for Linux).


### Python

/// tab | Windows

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

4. In Anaconda Prompt, create a new virtual environment for working with PET BIDS data
    ```
    conda create --name PETBIDS python=3.10
    conda activate PETBIDS
    ```

///

/// tab | Linux (Ubuntu/Debian)

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

3. Create a new virtual environment for working with PET BIDS data
    ```
    conda create --name PETBIDS python=3.10
    conda activate PETBIDS
    ```

///

### PET2BIDS

[PET2BIDS](https://github.com/openneuropet/PET2BIDS) is a well-validated tool for converting ecat7 (`.v`) and DICOM (`.dcm`) files to BIDS files.

Activate your PETBIDS environment. Remember that in Windows, you need to be using the "Anaconda Prompt".
```
conda activate PETBIDS
```

And then we can proceed to install the PET2BIDS software

```{bash}
pip install pypet2bids
```

The full package documentation can be found [here](https://pet2bids.readthedocs.io/en/latest/index.html#).

### dcm2niix

dcm2niix can also be installed using `conda` into your PETBIDS environment as follows:

```
conda activate PETBIDS
conda install -c conda-forge dcm2niix
```

To check if dcm2niix is installed correctly:

1. Open a terminal (Command Prompt, Terminal, etc.)
2. Type `dcm2niix -h` and press Enter
3. You should see the help message with usage instructions

### Docker

Docker is a tool for running software within a containerized environment. This means that all the dependencies are included within the docker container, and the software can be run without installing anything. BIDS Apps are often containerised within docker or singularity containers.

/// tab | Windows

Docker works best in Linux, and can be a bit of a pain in Windows. For running Docker in Windows, it's generally easier to run it within WSL (Windows Subsystem for Linux) to simulate a Linux environment.

1. Open PowerShell as Administrator
   - Search for PowerShell in the Start menu
   - Right-click and select "Run as administrator"

2. Install WSL with Ubuntu
   ```powershell
   wsl --install -d Ubuntu-22.04
   ```
   This command installs WSL with Ubuntu as the default distribution. The system will require a restart.

3. After restart, Ubuntu will finish setup
   - When prompted, create a username and password for your Linux distribution
   - This doesn't need to match your Windows credentials

4. Update your Ubuntu installation
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

Then follow the instructions for installing on Linux

///

/// tab | Linux (Ubuntu/Debian)

1. Install prerequisites

   ```bash
   sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
   ```

2. Follow the instructions [here](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) to:
    i. Set up Docker's apt repository.
    ii. Install the Docker packages.


3. Check that the installation was successful by running the  `hello-world` container

    ```
    sudo docker run hello-world
    ```

4. Follow the [post-install steps](https://docs.docker.com/engine/install/linux-postinstall/):

     ```
     sudo groupadd docker
     sudo usermod -aG docker $USER
     ```

5. Log out and log in again (or restart)

6. Test that you can now run docker commands without `sudo`

    ```
    docker run hello-world
    ```

///