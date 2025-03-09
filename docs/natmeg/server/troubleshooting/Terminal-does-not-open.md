---
title: Terminal does not open
tags: [Terminal, troubleshooting]
---

# Terminal does not open

In your local putty (Win) or Terminal (MacOS, Linux) once connected to the server:

1. Check if gnome-terminal is in /usr/bin:
`which gnome-terminal`

2. Check version of gnome-terminal:
`rpm -q gnome-terminal`

3. Verify gnome-terminal installation
`rpm -V gnome-terminal`

4. If you are getting an error message that the environment variable LANG is not set, you may have mixed settings in the Language and Region section (for example, English and Sweden) in your local System Preferences. Try matching them (for example, English and United States).  

5. Update XQuartz on your Mac

6. Reset local environment variable 'export LIBGL_ALWAYS_INDIRECT=1'

If any error messages contact NatMEG core team.

Disclaimer: The steps above worked for one user, but not 100% sure this was the solution.