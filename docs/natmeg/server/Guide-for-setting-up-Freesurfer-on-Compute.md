Freesurfer for doing surface-based segmentation and parcellation (e.g. used to create cortical sheets for MNE) is already installed in NatMEG's Compute server. To use Freesurfer, you need to configure your user account and set up the correct paths for your project.


## Setup Freesurfer

Freesurfer is found in `/opt/freesurfer/7.2.0-1`. To configure Freesufer run the following code (or add it to your `.bashrc` configuration to run every time you start a terminal):

````{bash}
export FREESURFER_HOME=/opt/freesurfer/7.2.0-1
source $FREESURFER_HOME/SetUpFreeSurfer.sh
````
Now you are ready to use Freesurfer.

## Setup project folder (`$SUBJECTS_DIR`)

Freesufer will as a default try to put output files in the folder "/home/your_username/freesurfer". Before you use Freesurfer, you should configure the SUBJECTS_DIR where the output files are put by Freesurfer. It is recommended to create a folder in your home directory for your project, e.g. "home/your_username/my_project" (but with an actual informative project name and your actual username). In that folder, you then create a folder called "fs_subjects_dir" for the Freesurfer data.

You then configure the SUBJECTS_DIR by running the following code:

````{bash}
export SUBJECTS_DIR=/home/your_username/my_project/fs_subjects_dir
echo "SUBJECTS_DIR = $SUBJECTS_DIR"
````
It can be an advantage to add the code snippet above to a setup script that your source every time you will work on "my_project".

You are now ready to call `recon-all`.

## Further documentation
For more information on how to use Freesurfer, yous should read the Freesurfer documentation: http://freesurfer.net/fswiki/Tutorials.
