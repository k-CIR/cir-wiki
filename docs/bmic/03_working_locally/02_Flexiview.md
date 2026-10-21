---
title: Setting up Flexiview
---


Before Flexiview can be downloaded and installed, you need to have mounted the `fluor18` network drive (see `Mounting Network Drives`).

Raw PET data and participant details are stored on Flexiview. Follow the instructions below to get up and running with Flexiview.

1. Find `FlexiviewSetup.msi` in the  `fluor18/Temp/FlexiView` or in `fluor18/Ecat7_nfs/downloads/FlexiView/` and copy it to your local drive.

2. Install Flexiview from FlexiviewSetup.msi.  On Linux, this can be installed usine Wine and Winetricks. If Windows gives you a warning about installing it, click first on "More info" and then "Run anyway"
  
3. If you are not at BioClinicum, or not connected to the main Bioclinicum network, connect first to the KI VPN.

4. The IP address of FlexiView should be 193.10.17.91. This needs to be set the first time Flexiview is run.  To set this, navigate as follows:
   * Database (top left) -> Preferences
   * Set both fields (for the Database Server and File Server) to 193.10.17.91
  
  <br>
  
  ![Navigate to Preferences]({{ picture_path }}/BMIC_Flexiview1.png)
  
  <br>
  
  ![Set the new IP addresses]({{ picture_path }}/BMIC_Flexiview2.png)
  
  <br>
  
5. Log into Flexiview with the username and password you were assigned.
