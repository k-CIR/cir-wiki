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

## Using Solena

### Opening a Study

1. Launch Solena:
   * Open terminal and type: `solena .`
   
2. Navigate to your study:
   * Click on "Study"
   * Change file filter from "Solena study database" to "TextFiles *.txt"
   * Navigate and select the `study_layout.txt` file
   * Click OK
   * Solena will create necessary files in the same directory as the study_layout file

### Setting Up Subjects
1. Create subject folders:
   * In file explorer, manually create empty folders named after your subjects in the same parent directory

2. Add subjects to the study:
   * In the Solena GUI, click on "Add" (Add subject to study)
   * Click on the relevant folder and click OK
   * Respond to prompts about creating folder structure and study part assignment
   * Solena will create all necessary files and folders inside

### Data Transfer
Transfer your raw MR and PET files/folders to the newly created Solena structure:
* PET ECAT7 files go to `\raw\pet_ecat7`
* PET DICOM files go to `\raw\pet_dicom`
* MR DICOM folders go to `\raw\mr_dicom`

### Configuring Subject Data
1. Click on the subject column that appeared in the Solena command window
2. Click on "Edit" (Edit constants for subjects)
3. Configure the following:
   * **SubjectName**: Manually type in the folder name of the subject (e.g., "fabl")
   
   * **pet1**: If using ECAT7 files, manually type in the full name of the PET-ECAT7 file including suffix
   
   * **mrSeqName**: Copy the MR sequence name (see below for how to obtain this)

#### Obtaining MR Sequence Name
**Method 1: Using the Inspector Tool**

* Click on "Inspect" (the owl symbol)
* Copy the MR sequence name displayed
* Click on "Edit" again, and paste in the MR sequence name

**Method 2: If Inspector Tool Doesn't Work**

* Open the MAT file created inside `raw\mr_dicom` (dcmCatalog.mat)
* Double-click on dcmCatalog in the Workspace window
* Find the correct MR name, double-click the 1x1 struct element in the second column
* Double-click on "headers"
* Double-click first 1x1 struct
* Copy the seriesDescription from here

**Method 3: Using Vinci-viewer**

* Load the relevant DICOM files into Vinci-viewer
* Click on the "i" symbol in the toolbar below the image panels
* Copy the series description from the popup window

### Running the Pipeline
1. Run the first pipeline step:
   * Click on the first row of the subject column
   * Click on the "Execute" button
   * Status should change to "pending"
   * Wait 2-3 minutes for conversion to complete

2. Run the second pipeline step:
   * Click on the second row of the relevant subject column
   * Click on "Execute"
   * Click on the "Inspect tool" and choose SPM or Slicer3D for viewing the MR

3. Run the third step of the pipeline:
   * Click on the third row of the relevant subject column
   * Click on "Execute"
   
... etc
