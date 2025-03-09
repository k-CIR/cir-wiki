---
title: Presentation
---

# Presentation

For an extended manual on Presentation software, see [Neurobs help page](https://www.neurobs.com/presentation/docs/index_html), this page is only for NatMEG specific configurations.

Some tips and tricks are available in [Presentation-script-tips](02_Presentation-script-tips.md)

Example scripts: 
* [Resting state paradigm](Examples/Presentation‐code‐example‐Resting‐state‐paradigm.md)
* [Auditory oddball paradigm](Examples/Presentation-code-example-Auditory-oddball-paradigm.md)

## Setting up the response buttons

1. Add the input ports you want to your experiment.

> You need an input port which is **port6** for the fORP-buttons response pads. Select the Response Device and configure the port settings.

![Port settings](../../resources/wiki_images/pres_port_in_settings_small.jpg)

1. Add output ports

> Here **port0** is Button pad 1 and **port4** is Button pad 2

![Port input settings](../../resources/wiki_images/pres_port_out_settings_small.jpg)

3. Add response buttons

> Here you need to add active buttons to the experiment, both from  the Button pads and from the keyboard, should you need it.

![Port button settings](../../resources/wiki_images/pres_response_settings_small.jpg)

\blandscape
\small

## Ports overview
|DIGITAL LINES|Port num|Port name|Port function|Comment|Bit line 1 |Bit line 2 |Bit line 3|Bit line 4|Bit line 5|Bit line 6|Bit line 7|Bit line 8|
| -------- | --- | ------- | ----------- | -------------- |:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|PCIe-6509|0|MEG (1-8) |Transmit: Event triggers to MEG acquisition system |Connects to STI101, lines 1-8 (STI001-008)|STI001|STI002|STI003|STI004|STI005|STI006|STI007|STI008|
||
|PCIe-6509|1|AudioFile|Transmit|AudioFile sound stimulator|Valve 1 ch1|Valve 1 ch2|Valve 1 ch3|Valve 1 ch4|Valve 2 ch6|Valve 2 ch7|Valve 2 ch8|Valve 2 ch9|
||
|PCIe-6509|2|CCS trig + AF trig|Transmit|Triggers CCS stimulators 1 and 2, Triggers AudioFile|BNC 1 Aux 3|BNC 2 Aux 4|BNC 3 Line 1|
||
|PCIe-6509|3|PAM|Transmit|Pneumatic valves; PAM, membranes, brush robot|Valve 1 ch1|Valve 1 ch2|Valve 1 ch3|Valve 1 ch4|Valve 2 ch6|Valve 2 ch7|Valve 2 ch8|Valve 2 ch9|
||
|PCIe-6509|4|MEG (9-16)|Transmit: Event triggers to MEG acquisition system|Connects to STI101, lines 9-16 (STI009-016)|STI009|STI010|STI011|STI012|STI013|STI014|STI015|STI016|
||
|PCIe-6509|5|RealTime|Receive|Connected to LPT5 for MatLab > Presentation interaction|Bit 1|Bit 2|Bit 3|Bit 4|Bit 5|Bit 6|Bit 7|Bit 8|
||
|PCIe-6509|6|fORP|Receive|2x4 response pads Connects to STI102, ch 9-16|Left Blue STI102 Ch 9|Left Yellow STI102 Ch 10|Left Green STI102 Ch 11|Left Red STI102 Ch 12|Right Blue STI102 Ch 13|Right Yellow STI102 Ch 14|Right Green STI102 Ch 15|Right Red STI102 Ch 16|
||
|PCIe-6509|7|FIB OPT|Receive|Ch 1-5 Fiber-optic gadgets Connects to STI102, ch 1-5|STI102 Ch 1|STI102 Ch 2|STI102 Ch 3|STI102 Ch 4|STI102 Ch 5|STI102 Ch 6 (not used)
||
|PCIe-6509|7|FIB OPT|Receive|Ch 7-8 CCS stimulation, Connects to STI102, ch 7-8|||||||CCS1 STI102 Ch 7|CCS2 STI102 Ch 8|
||
|LPT|1|EyeLink|Transmit: Event triggers to EyeLink acquisition system|Bit 1-8|Bit 1|Bit 2|Bit 3|Bit 4|Bit 5|Bit 6 |Bit 7 |Bit 8|
||
|LPT|5|MatLab/ Realtime|Transmit|Connected to PCIe-5 for MatLab > Presentation interaction|Bit 1|Bit 2|Bit 3|Bit 4|Bit 5|Bit 6 |Bit 7 |Bit 8|
||
|AUX/ MISC|1|AUX/ MISC|Transmit/ Receive|BNC link btw Stimulation and MSR cabinet| Aux 3| Aux 4| Aux 5| Aux 6| Aux 7| Aux 8|Aux 9|Aux 10|

\elandscape