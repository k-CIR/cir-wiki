---
title: Morphing, normalization, and transforming source spaces and coordinate systems (MNE)
tags: [MNE-Python, source analysis, normalization]
---


This page is various quick guides to normalization of source estimates with MNE-Python and working with group level data. 

## Read labels from standard atlas
In MNE you transform atlas from fsaverage to subject anatomy. The advantage is that Freesurfer comes with several standard atlases that is already transformed to individual anatomy as part of the standard Freesurfer pipeline. Just read the labels:

/// tab | MNE-Python
```Python
labels = mne.read_labels_from_annot(subj,
                                    parc=atlas,
                                    subjects_dir=subjects_dir,
                                    hemi=hemi)
```

If you want to use atlases that are not part of Freesurfer as a default, you need to add them to Freesurfer first: see this [example script](https://github.com/natmegsweden/NatMEG_Wiki/blob/main/example_scripts/add_annot.sh).

## Transform source space to common space.
With MNE you usually transform to the Freesurfer template "fsaverage" for group analysis. To transform from subject source space to common space, MNE make use of a "morph" class that once constructed is applied to the source estmates in downstream processing steps. For more information on the "morph" class, see the [MNE documentation](https://mne.tools/stable/generated/mne.SourceMorph.html#mne.SourceMorph).

Follow the MNE tutorials to see how to create and apply morphing in MNE:

* [Morph surface source space](https://mne.tools/stable/auto_examples/inverse/morph_surface_stc.html) (the most common in MNE)
* [Morph volume source space](https://mne.tools/stable/auto_examples/inverse/morph_volume_stc.html?highlight=morph)

///