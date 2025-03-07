# Problem: Alt-key does not work on Mac-keyboard

# Solution:

> Disclaimer: this may only be a temporary fix, and a Mac-only problem

1. Identify the keycode of your alt-key: `xev -event keyboard` press Alt. This will probably show double events, including Shift_L (probably keycode 50), check the keycode for the other events.

![exv -event keyboard](https://github.com/natmegsweden/NatMEG_Wiki/raw/main/wiki_images/xev_print.png)

2. run `xmodmap -e "keycode your_keycode = Alt_L"`
3. to make it automatic when you start your vncserver add it to your .bashrc

Example:

For some reason I had to change it twice, thus adding the following lines to .bashrc

`xmodmap -e "keycode 64 = Alt_L"`

`xmodmap -e "keycode 205 = Alt_L"`

