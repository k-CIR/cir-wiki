---
title: Lab notebook
---


# Lab notebook

![Lab notebook](../../resources/wiki_images/lab-notebook_small.jpg)

The Lab notebook helps you to note important things for your project. You can add project specific details in the Project column, subject specific details in the Subject column or measurement specific details in the Date column. The Lab notebook is saved as json-files and txt-files in your project folder.

## Before measurement
1. Start a notebook server from the desktop (if one is not already running in the Terminal)
2. Start Lab notebook from the desktop
3. Choose Project, Subjects and Date (automatically todays date)

## During measurement
1. Note everything of interest for the experiment, preferably in the Date column
2. One thing to note may be subject's sleepiness during the measurement according to the Karolinska sleepiness scale (KSS) which should be on the desk or on the Stimulus computer's Desktop.

## After measurement
Make sure all notes have been added and close the Lab notebook

## Issues

### Lab Notebook does not start

<u>Problem</u>: If you cannot open Lab Notebook and get and error message saying Firefox is already running.
<u>Solution</u>: Open a new terminal and type:

> pkill -f firefox

This shuts down all Firefox processes. Then open the notebook server and the notebook from the desktop.
