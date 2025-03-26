---
title: Mounting Network Drives
---

## Windows

1. Open the Windows File Explorer

2. Navigate to "This PC"

3. Right click in some empty space in the right hand window

4. Click on "Add a network location"

5. Select "Choose a custom network location"

6. Add the relevant network locations as follows:
    
    * **alfred:** Map \\\\130.229.41.50\\alfred to one drive name (typically Z:)
      * This is the file server for working directories
    
    * **fluor18:** Map \\\\130.229.41.50\\fluor18 to another drive name (typically Y:)
      * This is the file server for software
    
    * **matlab:** Map \\\\193.10.16.204\\matlab to another drive name (typically X:)
      * This is the file server for MATLAB scripts
      
7. When prompted for username and password, enter your full KI email adddress and password respectively
    
## Linux (Debian/Ubuntu)

1. Create empty folders in `/mnt` for alfred, fluor18 and matlab by pasting these commands into the terminal.

 ```
 mkdir /mnt/alfred
 mkdir /mnt/fluor18
 mkdir /mnt/matlab
 ```

2. Download the relevant utilities for interacting with network drives: 

```
sudo apt-get install cifs-utils
```

3. Mount the folders in the designated locations, replacing ZZZ and XXX below with your KI username (e.g. grmath) and KI password (i.e. which you use for your email). It can be easiest to just paste these into a notepad tool to replace the ZZZ and XXX with the relevant details.

```
sudo mount -t cifs -o username=ZZZ,password=XXX,vers=2.0,uid=$(id -u),gid=$(id -g),forceuid,forcegid //130.229.41.50/alfred /mnt/alfred
sudo mount -t cifs -o username=ZZZ,password=XXX,vers=2.0,uid=$(id -u),gid=$(id -g),forceuid,forcegid //130.229.41.50/fluor18 /mnt/fluor18
sudo mount -t cifs -o username=ZZZ,password=XX,vers=2.0,uid=$(id -u),gid=$(id -g),forceuid,forcegid //193.10.16.204/matlab /mnt/matlab
```

4. *If* you ever need to un-mount, use e.g. `sudo umount -f /mnt/alfred` (and similarly for the other mounted file servers)

5. And if you un-mount and need to re-mount, use `sudo mount -a`
