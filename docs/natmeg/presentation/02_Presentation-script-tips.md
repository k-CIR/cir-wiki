---
title: Presentation script tips
---

# Presentation script tips

## Code

The Presentation code is made up of SDL and PCL languages. Basically, in SDL you define objects that will be shown on the screen.

In PCL you do the workflow of your experiment. You can also change parameters of objects created in the SDL part.

## Python in Presentation

In PCL you can run separate Python (or other) scripts using the `run_process()` function. You can for example run a python-file for image processing. The first argument is the `python` command, second is the file to be run. The third option is whether to run the script in parallel in the background while continuing with the Presentation code, or wait for the Python code to complete before moving to the next line in Presentation. If `true`, note that if you want to use the outcome of the python-script in a subsequent part of your Presentation script you need enough time to finish it (or simply set it to `false`).

The final argument is whether to hide or show user interface.

```python
# Process will run and Presentation will pause until finished
run_process('python', 'process_image.py', false, true)
```

## Presentation in Python

>! NatMEG core team has not tried all functions so this is to be considered experimental for now.

Presentation has a python module called PresPy. With it you can program in python and execute Presentation commands.

```python
import sys
if sys.version_info.major < 3:
   sys.path.append( r"C:\Program Files (x86)\Neurobehavioral Systems\Presentation\Extensions\Python\2.7" )
else:
   sys.path.append( r"C:\Program Files (x86)\Neurobehavioral Systems\Presentation\Extensions\Python\3.7" )


import PresPy

pc = PresPy.Presentation_control()

pc.open_experiment(r"D:\NATMEG PROJECTS\<PATH TO YOUR EXP FILE>" )
pc.set_header_parameter( "active_buttons", 9 )
pc.set_header_parameter( "button_codes", "1,2,3,4,5,6,7,8,9" )

scen = pc.run( 0 )

bitmap = scen.bitmap() # Create a bitmap stim
text = scen.text() # Create a text stim
pic = scen.picture() # Create a picture stim
trial = scen.trial() # Create a trial

pic.add_part(bitmap, 0, 0)

trial.add_stimulus_event(pic)
trial.add_stimulus_event(text)

clock = scen.get_var('clock')

t = clock.time_double()
trial.present()
print(clock.time_double() - t)

```

More to come...

___
For an extended manual on Presentation software, see [Neurobs help page](https://www.neurobs.com/presentation/docs/index_html).
