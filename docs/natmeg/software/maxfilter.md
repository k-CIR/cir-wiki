---
title: MaxFilter
---

MaxFilter™ is a software package developed by MEGIN for removing environmental noise and correcting for head movement in MEG data. It is widely used in the field of magnetoencephalography (MEG) research to enhance data quality and reliability.

You can learn more about MaxFilter [here](https://natmeg.se/learnaboutmeg/meg%20topics/data%20maxfiltering.html)

## See also

- [Software](./index.md) - overview of NatMEG software and preprocessing routes.
- [SESHAT](./seshat.md) - the main NatMEG preprocessing workflow.


### MaxFilter (CLI only)
Default settings. 

- Add all files for which you want continous head positioning estimation in `trans_conditions`
- If you do not have empty room files, leave the list empty `- ''`
- Add project bad channels in `bad_channels` list, one per line, or leave empty `- ''`

Maxfilter settings are defined in a config.yml

seshat maxfilter --config config.yml         # MaxFilter processing only
seshat maxfilter --config config.yml --dry-run  # Show commands without execution

```yml
MaxFilter:
  standard_settings:
    trans_conditions:
    - ''
    trans_option: continous
    merge_runs: true
    empty_room_files:
    - empty_room_before.fif
    - empty_room_after.fif
    sss_files:
    - ''
    autobad: true
    badlimit: '7'
    bad_channels:
    - ''
    tsss_default: true
    correlation: '0.98'
    movecomp_default: true
    subjects_to_skip:
    - ''
  advanced_settings:
    force: false
    downsample: false
    downsample_factor: '4'
    apply_linefreq: false
    linefreq_Hz: '50'
    maxfilter_version: /neuro/bin/util/maxfilter
    MaxFilter_commands: ''
    debug: false
```