---
title: Using Solena
---

## Selecting and setting up the study layout 

__Note__: The following tutorial-guide assumes that you use a default version of `study_layout.txt` file. An example verison can be copied from: [path forthcoming]. Paste this version or your own version of the `study_layout.txt` into a empty folder. This folder will become the parent folder for your study and its solena-processing (from here on called "parent" or "parent directory").  

1. Launch Solena:

    * Open MATLAB terminal and type: `solena .`
   
2. Navigate to your study:

    * Click on the "Study"-bottom (symbol: paper-check list) 
    * Change file filter from "Solena study database" to "TextFiles *.txt"
    * Navigate to the folder where your  `study_layout.txt` file is located, select it 
    * Click OK
    * Solena will now create necessary files in the same directory as the study_layout file

## Setting Up Subjects

1. Create subject folders:

  * In file explorer, manually create empty folders named after your subjects in the parent directory

2. Add subjects to the study:
    
  * In the Solena GUI, click on "Add" (Add subject to study; symbol: [Insert symbol description] ) 
  * Click on the relevant subject folder and click OK
  * Respond to prompts about creating folder structure and study part assignment (choose "default" unless otherwise specified)
  * Solena should now create all necessary files and folders inside the subject specific folder. 
  * Navigate to the subject folder in file explorer and make sure it's been populated properly with new files and folders [INSERT example names of files and folders, or image].  

## Data Transfer

Transfer your raw MR and PET files/folders to the newly created Solena structure.

  * PET ECAT7 files go to `\raw\pet_ecat7`
  * PET DICOM folders or files go to `\raw\pet_dicom`
  * MR DICOM folders go to `\raw\mr_dicom`
  * __Note__: raw PET files can often be located on Flexiview. Raw MR data can often be located on the MR-server. 

## Configuring Subject Data

1. Click on the subject column that appeared in the Solena command window (to the left there should now have appeared a column with greyed out "I" "O" and "Q" symbols - click on this column). 
2. Click on the "Edit" bottom (Edit constants for subjects, symbol: [INSERT symbol desc])
3. Configure the following:

  * **SubjectName**: Manually type in the folder name of the subject (e.g., "fabl")
  * **pet1**: If using ECAT7 files, manually type in the full name of the PET-ECAT7 file including suffix

   
## Running the Pipeline

1. Run the first pipeline step Block 1: [INSERT NAME OF BLOCK]

  * Click on the first row of the subject column ("I", "O", "Q" symbols)
  * Click on the "Execute" button (symbol: [INSERT symbol desc])
  * Status should change to "pending"
  * Wait 2-3 minutes for conversion to complete

    **Obtaining MR Sequence Name**
    
    _Method 1: Using the Inspector Tool_
    
      * Click on "Inspect" button (the owl symbol)
      * Copy the MR SeriesDescription tag displayed
      * Click on "Edit" button again (opens the subject's studyconstant.txt in MNATLAB text editor): 
          * **mrSeqName:** paste in the MR SeriesDescription tag at the appropriate row that says mrSeqName (e.g.  ASx BRAVO 1337) 
    
    _Method 2: If Inspector Tool Doesn't Work_
    
      * Open the MAT file created inside `raw\mr_dicom` (dcmCatalog.mat)
      * Double-click on dcmCatalog in the Workspace window
      * Find the correct MR name, double-click the 1x1 struct element in the second column
      * Double-click on "headers"
      * Double-click first 1x1 struct
      * Copy the SeriesDescription from here into studyconstant.txt by using the "Edit"" button (see above)
    
    _Method 3: Using Vinci-viewer_
    
      * Load the relevant DICOM files into Vinci-viewer (http://www.nf.mpg.de/vinci3/doc/vinci-about.html)
      * Click on the "i" symbol in the toolbar below the image panels
      * Copy the series description from the popup window into studyconstant.txt by using the "Edit"" button (see above)
    
2. Run the second pipeline step Block 1: [INSERT NAME OF BLOCK - file conversion]
    
  * Click on the second row of the relevant subject column
  * Click on "Execute"
  * Wait a few minutes. 
  * When finished (both "I" and "O" symbol are green) check the `raw\mr_ana` folder and see if its been populated by `*.nii` file/files.
  * Click on the "Inspect tool" (symbol: cute owl with big glasses) and choose SPM or Slicer3D for viewing the MR. 

3. Run the third pipeline step Block 1: [Reorient and Crop MR]

  * Click on the second row of the relevant subject column
  * Click on "Execute"
  * There should now appear some SPM pop-up windows in MATLAB. 
  * ...
  * When finished (both "I" and "O" symbol are green), click on the "Inspect tool" and choose SPM or Slicer3D for viewing the MR. 

4. Run the fourth step of the pipeline Block 2: [INSERT NAME OF BLOCK]
  * Click on the third row of the relevant subject column
  * Click on "Execute"
  * ...
   
... etc
