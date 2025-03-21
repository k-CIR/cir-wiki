---
title: BIDS at MRC
---

To be able to co-register data from different imaging modalities in CIR, share data and analysis pipelines, it is important that data collected are saved in the standard Brain Imaging Data Structure ([BIDS](https://bids-specification.readthedocs.io/en/stable/)).

## MRC raw data
Data collected at MRC should be pushed to FOU1/Alvik after each completed session. A unique subject-ID is created for each session and data is stored under that ID and the time of scanning, in folders numbered according to MR-sequence.

**It is therefore important to note what ID gets created and assigned at each session.**

If a subject was scanned with three sequences at *2024-12-01*, *13:45:15* and given the ID: *12345*, their raw DICOM data would be located on Alvik in:

```markdown
/data/dicom/12345_20241201_134515/
├── 00000001
├── 00000002
└── 00000003
```
<br>

There are different tools available to make data collected at MRC compliant with BIDS, these are collected in the following repositories:

## [MRC-DICOM-to-BIDS](https://github.com/k-CIR/MRC-DICOM-to-BIDS)
Written to run on the MRC compute server nick-named Alvik. Gather DICOM data collected at MRC and convert to BIDS compliant naming and format. Designed to extract all sequences in the [CIR-protocol](https://github.com/k-CIR/CIR_wiki/wiki/CIR-MR%E2%80%90Protocol) for up to three sessions per subject and rename subjects to study specific ID.

Require [dcm2bids](https://unfmontreal.github.io/Dcm2Bids/3.2.0/) and [GNU parallel](https://www.gnu.org/software/parallel/) in your environment.

Note that ASL and SWI sequences are currently not defined in BIDS. See [BIDS extension proposal BEP004 & BEP005 for updates.](https://bids-specification.readthedocs.io/en/v1.2.1/06-extensions.html#bids-extension-proposals) For now, these are converted separately and copied to BIDS-derivatives.
