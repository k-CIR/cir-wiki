---
title: Undefined function 'fiff_read_epochs'
tags: [FieldTrip, MNE, fif, read, epochs]
---

## Issues

??? failure "FieldTrip cannot read raw FIF files"
    FieldTrip will not read raw FIF files and gives an error like this:

    ```matlab
    Undefined function 'fiff_read_epochs' for input arguments of type 'char'.

    Error in ft_read_header (line 1911)
            epochs = fiff_read_epochs(filename);

    Error in ft_read_header (line 134)
        hdr{i} = ft_read_header(filename{i}, varargin{:});
    ```

    !!! note ""
        FieldTrip uses low-level MNE-Matlab functions to read FIF data files. By default, these are not in any folder that FieldTrip adds to your path when running `ft_defaults`.

    !!! success ""
        Add the MNE functions to your path. Add the following line of code to your scripts at the stage where you would call `ft_defaults`:

        ```matlab
        addpath('~/fieldtrip/fieldtrip/external/mne')
        ```

        This assumes that you have FieldTrip in the folder `/home/your_username/fieldtrip/fieldtrip`. If not, change it to wherever you have FieldTrip.
