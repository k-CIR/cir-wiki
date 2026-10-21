It is recommended to check out the [road map for projects at CIR](https://ki.se/en/research/research-areas-centres-and-networks/research-centres/centre-for-imaging-research-cir/road-map-for-projects-at-cir){target="_blank"} to get an overview of some important checkpoints common for most imaging projects.

Generally, data collected at CIR is gathered at the _Shared Platform for Imaging in the CIR Environment_ - SPICE. This is a high performance compute cluster that store data for active projects and offer compute resources for users to analyze their data remotely.

## Purpose

![CIR Pyramid]({{ picture_path }}/CIR-pyramid.png){ width="350" }
/// caption
    attrs: {class: float-right-box}
The added value of having data organized in a standard format for all projects and modalitites is that sharing data and pre-processing is easy and different research groups do not have to re-invent the wheel for every new project.
///

CIR want to increase availability to imaging research at KI and specifically make it easier to conduct multimodal imaging research. No time should be wasted for individual researchers for finding, organizing and transforming imaging data. As data is gathered within a project, it can easily be structured according to the [BIDS](https://bids.neuroimaging.io/index.html){target ="_blank"} standard which allow for common pre-processing tools (or [BIDS-apps](https://bids.neuroimaging.io/tools/bids-apps.html){target="_blank"}, like [fmriprep](https://fmriprep.org/en/stable/){target="_blank"}, [petprep](https://github.com/nipreps/petprep){target="_blank"}, [PyMVPA](https://github.com/bids-apps/PyMVPA){target="_blank"}, etc.) to process the data. The goal for CIR is to:

  1. Have data for all imaging facilities organized and available within 24 hours of collection.
  2. Offer support to store all data in BIDS with minimal researcher input.
  3. Offer quality control report of collected data within days of collection.
  4. Disseminate and share pre-processing pipelines between projects (e.g. via this wiki and public git repos)

## Project and access
Data must be collected within a project registered with CIR. Registering a project is done by the projects PI agreeing to the [user agreement](https://ki.se/en/research/research-areas-centres-and-networks/research-centres/centre-for-imaging-research-cir/user-agreement-details){target="_blank"}, and filling out and signing the [project registration webform](https://ki.se/en/research/research-areas-centres-and-networks/research-centres/centre-for-imaging-research-cir/register-new-project-at-cir){target="_blank"}.

A project folder that can only be accessed by the PI and specified researchers is then added to SPICE and data collected within your project is gathered here. Individual researchers that need a user account on SPICE should fill out [this form](https://ki.se/en/research/research-areas-centres-and-networks/research-centres/centre-for-imaging-research-cir/request-to-access-the-cir-server){target="_blank"} - project access is granted following confirmation from the projects PI.

## Gathering the data for your project
Different imaging facilities have different systems for labeling data - you should not have to worry about this. To simplify data tracking and handling, CIR offer to keep track of, and gather the data collected for all imaging modalities used in your project.

This is done through a simple [**Redcap**](https://medarbetare.ki.se/forskarstod/hantera-forskningsdata/skapa-samla-in-och-lagra-forskningsdata/redcap/introduktion-till-redcap){target="_blank"} form to fill out at data collection. In short, Redcap is an encrypted, backed-up, local to KI, 2FA secured, logged, service for collecting clinical and research data and approved for storing of personal data. Incorporate filling this form as part of your protocol for data collection. By registering who is collecting what data, at what facility, the resulting data is gathered in your projects folder on SPICE within 24 hours. The information you fill out is used to pseudonymize your data so that data can be gathered to your project without personal information and imaging data having to be stored together.

A fundamental principle within CIR is that all data on SPICE is pseudonymized. However, you have full control over your own project folder and can for example upload questionnaire responses or other auxiliary data you may need for your analysis. You, or someone in your group accidentally uploading personal information to your project is outside the control of CIR. The ultimate responsibility for data integrity lies with the PI of the project.

<p style="text-align: center; font-size: 36px; font-weight: bold;">
  Go to:
  <a href="https://redcap.link/cir-session" target="_blank">
    https://redcap.link/cir-session
  </a>
  to register your data collection.
</p>

<style>
.narrow-caption figcaption { max-width: 1000px; margin: 0 auto; }
</style>

Data you collect are gathered in your project folder, e.g: `data/projects/raw/modality`. The raw data is **read-only** by design. This is to 1) ensure the sync-process from the core facilities can keep track of what data has been made available to you, which is difficult if data is moved or renamed. 2) simplify for CIR to offer standardized pre-processing pipelines for all projects.

As soon as your data starts coming in, your next course of action should be to organize it according to the Brain Imaging Data Structure (BIDS) standard. This is the foundation for consistent and reproducible neuroimaging data analysis. You can read more about how CIR supports you in this process on the wiki-page [BIDS on SPICE](https://k-cir.github.io/cir-wiki/SPICE/05_spiceBIDS/).

![Data flow]({{ picture_path }}/data_structure.png){ width="1200" }
/// caption
    attrs: {class: narrow-caption}
Overview of how different facilities (in this example MRC and NatMEG) use different data structures when data is collected and how CIR gather it in a BIDS-inspired (subject/session/modality) format in your project folder.
///

!!! note "Do it yourself?"
    If you are used to organizing your raw data yourself, and do not want to register your data collection in Redcap, you can have whatever data is collected in your project syncronized to your project folder in the corresponding facilities data structure (i.e. what is to the left in the image above). In this case, CIR can not assist you with keeping track of the different subject-IDs used by the different facilities, provide the same level of support for organizing your data in BIDS or generate a report of what data is collected in your project.

Using the redcap form to register your data collection, as described above, a html-report is kept updated in your project folder on SPICE. This provide an overview of who collected what data when and where in your project, the key to the different IDs used by facilities and when data was collected and transferred to your project folder. This makes it easy to quickly gauge that everything gets collected as expected during your project.

![Project report]({{ picture_path }}/project_overview_table.png){ width="1200" }
/// caption
    attrs: {class: narrow-caption}
An example of the overview report rendered in your project folder. The table can be sorted, searched and filtered by you for quick checking that data is collected as expected.
///
