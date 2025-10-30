---
title: Consistent filenames in loops
---

Consistent filenames are key to data management. If you name your output files manually every time you save a file, you risk making errors. Do not rename files each time you run the analysis. Use a consistent way to read what subject, session, and processing step the data belongs to.

In the top of a script (or better in a separate `config` script that you run at the beginning of every other script), you specify the base string of the filename. E.g.:

/// tab | FieldTrip
```matlab
%% Base file names
raw_fstring = '-proc-tsss-raw.fif';          % The raw data
ds_fstring  = '-proc-ds200-raw.mat';   % Downsampled and cleaned raw data
epo_fstring = '-epochs.mat';            % Epoched data
```
///

/// tab | MNE-Python
```python
# Base file names
raw_fstring = '-proc-tsss-raw.fif'          # The raw data
ds_fstring  = '-proc-ds200-raw.fif'         # Downsampled and cleaned raw data
epo_fstring = '-epo.fif'                   # Epoched data
```
///


Then in the loop/function where you run the data processing, you specify the subject-specific input- and output filenames. 

/// tab | FieldTrip

This is an example of how to do in a Matlab loop:

```matlab
%% Run loop...
for ss = 1:length(all_subjects)
   subj = all_subjects{ss};

   % Define filenames
   infname  = fullfile(my_data_path, subject_folder_path, [subj, ds_fstring]);    % Read '-raw-downsampled.mat'
   outfname = fullfile(my_data_path, subject_folder_path, [subj, epo_fstring]);   % Save '-epochs.mat'

   % Load data
   load(infname)

   % Run your process
   ...

   % Save
   save(outfname, mydata)
end
```
///

/// tab | MNE-Python

This is an example of how to do in a Python loop:

```python

# Run loop...
for ss in all_subjects:
   subj = ss

   # Define filenames
   infname  = os.path.join(my_data_path, subject_folder_path, subj + ds_fstring)    # Read '-proc-ds200-raw.fif'
   outfname = os.path.join(my_data_path, subject_folder_path, subj + epo_fstring)   # Save '-epo.fif'

   # Load data
   raw = mne.io.read_raw_fif(infname) # Read data

   # Run your process
   epochs = mne.Epochs(raw)

   # Save
   epochs.save(outfname) # Save epochs

```
///

Example with multiple sessions and subjects:

/// tab | FieldTrip

```matlab
%% Run loop...
for ss = 1:length(all_subjects)
   for jj = 1:length(all_sessions)

      subj = all_subjects{ss};
      session = all_sessions{jj}

      % Define filenames
      infname  = fullfile(my_data_path, subject_folder_path, [subj,'-',session, ds_fstring]);    % Read '-raw-downsampled.mat'
      outfname = fullfile(my_data_path, subject_folder_path, [subj,'-',session, epo_fstring]);   % Save '-epochs.mat'

      % Load data
      load(infname)

      % Run your process
      ...

      % Save
      save(outfname, mydata)
   end
end
```
///

/// tab | MNE-Python

```python
# Run loop...
for ss in all_subjects:
   for jj in all_sessions:

      subj = ss
      session = jj

      # Define filenames
      infname  = os.path.join(my_data_path, subject_folder_path, subj + '-' + session + ds_fstring)    # Raw name '-proc-ds200-raw.fif'
      outfname = os.path.join(my_data_path, subject_folder_path, subj + '-' + session + epo_fstring)   # Save '-epo.fif'

      # Load data
      raw = mne.io.read_raw_fif(infname) # Read data

      # Run your process
      epochs = mne.Epochs(raw)

      # Save
      epochs.save(outfname) # Save epochs

```
///