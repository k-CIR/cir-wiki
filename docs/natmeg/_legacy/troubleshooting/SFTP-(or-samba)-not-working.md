---
title: SFTP (or samba) not working
tags: [SFTP, samba, connection, storage]
---

## Issues

??? failure "SFTP or samba is not working"
    This can happen when the bash console on storage returns a message that is too large for the protocol.

    !!! success ""
        Connect to `storage02` with SSH (`username@storage02.natmeg.se`), open the `.bashrc` file with a text editor such as `nano ~/.bashrc`, comment out any `echo` commands by adding a `#` in front of them, and save.
