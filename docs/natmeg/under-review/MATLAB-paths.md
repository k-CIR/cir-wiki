When adding paths to your MATLAB pathdef, you should save the pathdef in a local folder E.g., if you want to add a toolbox like FieldTrip permanently to your path.

When you install MATLAB, it should create a folder in your home directory called `~/matlab`. Save the pathdef as `pathdef.m` in this folder.

Using the Set Path tool from the menu in the MATLAB GUI might give an error if you add paths and try to save from the GUI tool. A popup will appear that asks if you want to save in another location. Click "yes" and save as `~/matlab/pathdef.m`.

The reason for the error is that MATLAB tries to save the pathdef in the shared MATLAB folder in `/opt`.