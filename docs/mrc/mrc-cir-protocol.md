---
title: 3T CIR Protocol
---

## Introduction 
The brain imaging protocol for CIR was developed in synergy between the UK Biobank, ADNI-4  and HumanConnectom-Aging projects. CIR will establish a standard protocol at Karolinska CIR to enable multi-modality and cross-subject, cross-disease research of human brain. Hereby, we provide details of the acquisition protocols and suggestions for minimal image pre-processing.

## MRI scanner
The protocol was developed on the General Electric (GE) 3 Tesla scanner, Signa-PremierXT installed 202301, 70 cm bore, 80 mT/m max gradient strength, 200 T/m/s slew rate, and a 48 channels RF receive head-neck coil. 

## MRI acquisition protocol
The total experimental time is ca. 34 min. The protocol contains the following 7 MR contrasts (details below)
* **T1-weighted** (4:46 min)
* **T2-weighted FLAIR** (4:15 min)
* **Scout** (0:09 min)
* **Arterial Spin Labeling** (5:02 min)
* **FieldMap fmri** (0:05 min)
* **Functional MRI** (Resting-state, eyes open, 6:02 min)
* **FieldMap DTI** (0:39 min)
* **Diffusion Tensor Imaging** (8:27 min)
* **Susceptibility-weighted imaging** (1:41 min)
* **T2-weighted structural imaging** (2:26 min)

## T1-weighted (4:46 min)
3D structural imaging provides T1- relaxation time contrast between grey and white matter while CSF is nulled. It is used for (i) medical assessment, (ii) inter-subject, cross-modality alignments, and (iii) brain segmentation.

3D MPRAGE Sagittal, resolution 1 mm3, 180 slices, TR=2.237, FA=9, BW=244.1 Hz/pix, Parallel Imaging: ARC R=2, Coil Intensity Corrections and Gradwarp applied. Prospective motion correction - PROMO™ is used.

## T2-weighted FLAIR (4:15 min)
3D structural imaging provides a transverse-relaxation time contrast between GM, WM, while CSF is nulled. It is used for (i) medical assessment (ii) inter-subject, cross-modality alignments, and (iii) brain segmentation.

3D IR - Fast Spin Echo (CUBE), sagittal, resolution 1 mm3, 180 slices, TE=130 ms, TI=1894 ms, Tr=6800, Parallel Imaging: ARC R=2x2, CS  R=1.2, B1, Coil Intensity Corrections and Gradwarp applied. 

## Scout (0:09 min)
Refine head position, patient may slide down while the following imaging requires accurate slice positioning.

## Arterial Spin Labeling (5:02 min)
3D quantitative imaging of blood perfusion weighted contrast that uses arterial blood water as an endogenous tracer to measure blood flow through brain parenchyma.

3D Fast Spin Echo-Spiral, axial, eff.resolution 3.5 mm3, 46 slices 3.5 mm thick, Labeling duration 1450 ms, Post-labeling delay 2525 ms, vascular crushers: none, Gradwarp applied. Dataset contains: M0, PW (difference image tag-control) images zero-filled to 128x128 matrix. 

## FieldMap fmri (0:05 min)
The same setting as for FMRI but reverse phase view order. 

Type-in psd: epiRTrs, CV blips =1, distortion A>P, phase enc. dir. “j-”

## Functional MRI (Resting-state, eyes open, 6:02 min)
Time series data provides contrast sensitive to blood oxygenation associated with intrinsic brain activity of GM. It is used for functional connectivity mapping as well as other derivative metrics of tissue oxygenation are produced.

2D Gradient Echo EPI, axial (no tilt), resolution 3 mm3, 44 slices, 3 mm thick,  TR=720 ms, FA=60°, TE=28 ms, Parallel Imaging: ARC R=1, MultiBand R=4 (11 bands), Eff.echo.spacing= 516µs, Tot.readout=0.037668 s, Fat Sat – classic.
Dataset: number of volumes=500, num.dummy scans =3 excluded from dataset, image ACQ matrix: 74x74 , Recon matrix: 128x128.  
(type-in psd: epiRTrs, CV blips =0, distortion P>A, phase enc. dir. “j”  ).

## FieldMap DTI  (0:39 min)
The same setting as for DTI but reverse phase view order (blips polarity)
Type-in psd: epi2as, distortion A>P, phase enc. dir. “j-”

## Diffusion Tensor Imaging (8:27 min)
Provides contrast based on diffusion properties of intra and extra cellular water. Local diffusivity metrics are sensitive to the integrity of tissue compartments (multiple b-values required). Anisotropic diffusion probed along multiple directions is sensitive to structural connectivity between brain regions.

2D Spin Echo EPI, axial (no tilt), resolution 2 mm3, 72 slices 2 mm thick, two diffusion shells b1=1300 s/mm2 50 dir’s and b2=2600 s/mm2 50 dir’s, # b0=6, TE=75 ms, gradient directions adopted from UK Biobank project,  Parallel Imaging: ARC R=2, MultiBand R=2,  Eff.echo.spacing =337µs, Totl.readout=0.03634s,  FatSat: classic and Slice-Selective  Gradient Reversal,  image ACQ matrix = Recon matrix= 110x110 
(type-in psd: epi2asaltoff, distortion P>A, phase enc. dir. “j”  ).

## Susceptibility-weighted imaging (1:41 min)
Provides contrast sensitive to magnetic susceptibility differences between tissue constituents (e.g., iron, calcium and myelin). It is used for (i) medical assessment (ii) for characterization of iron, myelin, micro-bleeds, etc.

3D EPI Gradient Echo, axial, resolution 0.5x0.5x2 mm, single echo, TE=27 ms, TR=56 ms, FA=20°, number of multi-shots 20, matrix 448x448, 80 slices 2 mm thick, Fat Sat: SpSp rf-pulse. Two datasets is produced: SWI and local tissue phase map. Raw data is not returned, processed data is returned with some delay.

## T2-weighted structural imaging (2:26 min)
Provides a T2-relaxation time contrast between GM, WM, while CSF is not nulled. It is used for (i) medical assessment (ii) tissue segmentation.

3D Fast Spin Echo (CUBE™), sagittal, resolution 1 mm3, 180 slices, TE=90 ms,  Parallel Imaging: ARC R=2x2, CS R=1.2, B1, Coil Intensity Corrections and Gradwarp. 