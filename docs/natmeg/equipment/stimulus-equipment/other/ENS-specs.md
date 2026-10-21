## Electric Nerve Stimulation

![Electric Nerve Stimulator]({{ picture_path }}/electric-nerve.png)

For  electrical nerve stimulation, we use two DeMeTec SCG30 stimulators, either with felt tips for median nerve stimulation, or with ring electrodes for single phalange stimulation.


The trigger to stimulation delay is about 3 msec.

* Further technical specifications are found [here](https://natmeg.se/onewebmedia/SCG30_TechnischeDaten.pdf).

### Ring electrodes
Wrap two disposable ring electrodes around the finger of interest. The silver conductive side is facing the skin, and the blue insulated side is facing outwards. To connect the ring electrodes to the stimulators, we use a custom-built connector:

![Custom connector](/resources/wiki_images/ring_electrode_connector.jpeg){ width="400" }
/// caption
Custom-built connector for connecting the ring electrodes to the DeMeTec stimulators.
///

 Make sure that the metal inside the connector is in contact with the silver conductive side of the ring electrodes and not the insulated blue side, otherwise the stimulation will not work.


### Controlling the DeMeTec stimulators using python
The stimulators can be controlled using python. Check out the [SCGcntrl GitHub repository](https://github.com/laurabpaulsen/SCGcntrl).


