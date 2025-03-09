---
title: SFTP (or samba) not working
tags: [SFTP, samba, connection, storage]
---

This can happen when the bash console on storage returns a message that is too large for the protocol. To fix it connect to storage02 with ssh (`username@storage02.natmeg.se`), open the bashrc file with a text editor (e.g., `nano ~/.bashrc`), comment out any `echo` commands by adding a `#` in front of it and save. 