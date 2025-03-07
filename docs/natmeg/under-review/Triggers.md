
## Issues

### Errors with trigger channel STI016 in Neuromag data

<u>Problem</u>: Triggers in the main trigger channel (STI101) are wrong. Some have negative values.

There is a know issue when using TTL triggers with bit 16 during recordings of Neuromag MEG data. For some reason  STI016 in the Neuromag acquisition setups is stored with a negative value -32768 and subsequently subtracted rather than added to the total trigger value when read offline.

Note that this problem does not appear in the Acquisition software or databrowser when recording data. The problem first appears when the data is written to disk and then loaded with MNE Python or FieldTrip for further off-line processing.

<u>Solution(s)</u>:

If you use **MNE Python**, this can be fixed with adding the argument unit_cast=True in mne.read_event. Like this:
> eve = mne.find_events(mydata, unit_cast=True).

Then you should get the correct trigger values in STI101 and can proceed as normal.

If you use **FieldTrip**, download the custom trial function ft_trialfun_neuromagSTI016fix from NatMEG's Github page (link). Copy/paste it into your FieldTrip directory in the folder ./fieldtrip/trialfun. Then when you read trials into FieldTrip, you must specify to use this trial function when reading data with ft_define_trial and ft_preprocessing.  The trial function will reconstruct STI101 from the split trigger channels and trigger values should be correct and you can proceed with your analysis as normal. For example, like this:

> \# Read data with reconstructed STI101 triggers
>
> cfg = [];
>
> cfg.dataset             = fname;
>
> cfg.trialdef.prestim    = 1;            # Time before trigger
>
> cfg.trialdef.poststim   = 1;            # Time after trigger
>
> cfg.trialdef.eventtype  = 'STI101';
>
> cfg.trialfun            = 'ft_trialfun_neuromagSTI016fix';
>
> cfg                     = ft_definetrial(cfg);
>
> data                    = ft_preprocessing(cfg);