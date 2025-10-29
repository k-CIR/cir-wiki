---
title: Singularity containers
---

SPICE supports the use of [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html) containers for running software in isolated environments.

Singularity is a container platform designed for high-performance computing environments. It enables users to create and run containers that encapsulate software and its dependencies in a portable, reproducible, and secure manner.

We maintain several pre-built Singularity images to support the execution of various neuroimaging software tools, ensuring consistency across analyses and simplifying software management.

Singularity images ara available in: `/scratch/singularityContainers`

## Running a Singularity Image
If the data to be preprocessed is already on the server, you are ready to run a Singularity image. E:
```bash
$ singularity run --cleanenv fmriprep.simg \
    path/to/data/dir path/to/output/dir \
    participant \
    --participant-label label
```
## Further documentation
For more information on how to use Singularity check [here](https://docs.sylabs.io/guides/3.5/user-guide/index.html#).