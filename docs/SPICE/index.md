---
title: SPICE
---
!!! note "SPICE is being made accessible to external users"
    During Q4 2026, the SPICE server is being updated to provide access to external users. That is, research partners and collaborators not neccesarily located at KI.

    Access to SPICE require users to be connected to the KI network, either physically or via VPN. Soon, SPICE will be made accessible to its users from any location, provided they have the necessary credentials - a registered user account, password and a two-factor authentication (2FA) or SSH key.

    **Until further notice, during the transition period, being connected to the KI network is still required.**

    Remote desktop access to SPICE will be provided via a secure web portal. Terminal access and data download via SFTP is available as usual with the addition of 2FA or SSH key authentication.

    Users with an existing account will be contacted to have their account uppdated to the new authentication system. Projects, environments and data is left untouched.

## The Shared Platform for Imaging in the CIR Environment (SPICE)

If you collect data at CIR, you are provided with access to the CIR high performace cluster nicknamed **SPICE** (Shared Platform for Imaging in the CIR Environment). With 256 CPU cores, 2.3 Terrabyte of RAM and 1 Petabyte of fast storage SPICE is designed with neuroimaging and data analysis in mind, providing a powerful and flexible environment for processing large datasets. Standard software such as Matlab, Python, FSL, SPM, FreeSurfer and AFNI are installed and ready to use. You can also install your own software if needed.

## Get user access
To get access to SPICE you need to be a member of a research group that has an active project at CIR. Fill out the [the webform on the KI web page](https://ki.se/en/research/research-areas-centres-and-networks/research-centres/centre-for-imaging-research-cir/request-to-access-the-cir-server)  to request a new user account. Access is granted after approval by the projects PI.

Users get access to a home folder located in 

    /data/users/yourusername

.. and access to any project folders they are a member of, located in 

    /data/projects/projectname

Data collected at CIR (e.g. MRI, PET, MEG, EEG)  land as read only in `raw/` in the projects folder.

How your project and its data are managed is up to you and your projects PI. The general recommendation is to save processed data and results to the specific project folder so it can be accessed by all project members.

The home folder is intended for personal scripts and code in development, and should not be used for storing data.
