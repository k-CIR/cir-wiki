---
title: Terminal does not open
tags: [Terminal, troubleshooting]
---

## Issues

??? failure "Terminal does not open"
    In your local PuTTY (Windows) or Terminal (macOS, Linux), once connected to the server, try the following.

    !!! success ""
        1. Check if `gnome-terminal` is in `/usr/bin`:
           `which gnome-terminal`
        2. Check the version of `gnome-terminal`:
           `rpm -q gnome-terminal`
        3. Verify the `gnome-terminal` installation:
           `rpm -V gnome-terminal`
        4. If you are getting an error message that the environment variable `LANG` is not set, you may have mixed settings in the Language and Region section in your local System Preferences. Try matching them, for example English and United States.
        5. Update XQuartz on your Mac.
        6. Reset the local environment variable `export LIBGL_ALWAYS_INDIRECT=1`.
        7. On macOS, open `.zshrc` on your local computer (`nano ~/.zshrc`), add the following lines, save, then close and reopen terminal:

           `export LC_ALL=en_US.UTF-8`

           `export LANG=en_US.UTF-8`

        If any error messages remain, contact the NatMEG core team.

    !!! note ""
        The steps above worked for one user, but it is not 100% certain that this was the solution.
