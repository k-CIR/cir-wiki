---
title: Initial Setup
---

Follow these steps to set up Solena in MATLAB for the first time.

1. Download MATLAB 2014b and install it

    * You require a MATLAB licence first: sort this out with your PI.
    * You can find the file by Googling "Matlab 2014b installation windows"
    * Add only the necessary toolboxes:
    
        * MATLAB 8.4
        * Simulink 8.4
        * Curve Fitting Toolbox 3.5
        * Data Acquisition Toolbox 3.6
        * Image Acquisition Toolbox 4.8
        * Image Processing Toolbox 9.1
        * Parallel Computing Toolbox 6.5
        * Signal Processing Toolbox 6.22
        * Spreadsheet Link EX 3.2.2
        * Statistics Toolbox 9.1

2. Install MATLAB Runtime:
    * Navigate to the matlab network drive (henceforth `X:\`) folder and find `MATLAB_Runtime_R2022b_Update_5_win64` in the installers folder
    * Open and install

3. Configure MATLAB path:
    * Open MATLAB as administrator for the first time, by right clicking on MATLAB and clicking on "Run as administrator"
    * Run the following to set path to the relevant folders

```
addpath('X:\toolbox\m-files\solena')
```

  * Alternatively, if this does not work, you can use the full network address as follows:

```
addpath('\\130.229.41.50\toolbox\m-files\solena')
```

  * Close MATLAB again


4. Initialize Solena:

    * Open MATLAB normally (i.e. not as administrator). 
    * Run Solena in terminal with the command: `solena .` 
        * __Note 1__: You may need to run this command twice for Solena to boot correctly and aadd all necessary paths and files. 
        * __Note 2__: If it does not work type `clc; clear all` in the MATLAB terminal then run the `solena .`  command again. 
        * __Note 3__: If it still does not work restart MATLAB and try again. 

5. Set up Docker for Freesurfer:

    * Install Docker desktop for Windows
    * Instructions forthcoming...