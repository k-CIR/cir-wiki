---
title: FreeSurfer and MNE-Python
---

This container holds FreeSurfer and MNE-Python, which are commonly used for structural MRI processing and MEG/EEG data analysis. Both these requirements are needed to create the BEM surfaces for source localisation. 

Location: `/scratch/singularityContainers/mne_freesurfer.sif`

## Dev notes
For future reference, if the container needs updating, the command and Dockerfile used to create it is provided below.

### Dockerfile
```
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV FREESURFER_HOME=/opt/freesurfer
ENV SUBJECTS_DIR=/data/subjects
ENV FS_LICENSE=/opt/freesurfer/license.txt
ENV PATH=/opt/freesurfer/bin:$PATH

RUN apt-get update && apt-get install -y \
    wget curl git tcsh bc perl tar gzip \
    python3 python3-pip python3-dev \
    libxext6 libxmu6 libxt6 libglu1-mesa \
    libgomp1 libx11-6 \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
    mne \
    numpy \
    scipy \
    pandas \
    matplotlib \
    nibabel \
    pyvista \
    pyvistaqt \
    mne-bids \
    autoreject \
    scikit-learn \
    jupyterlab

RUN wget -O /tmp/fs.tar.gz \
 https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.1/freesurfer-linux-ubuntu22_amd64-7.4.1.tar.gz && \
 mkdir -p /opt && \
 tar -xzf /tmp/fs.tar.gz -C /opt && \
 rm /tmp/fs.tar.gz


RUN echo "source \$FREESURFER_HOME/SetUpFreeSurfer.sh" >> /etc/bash.bashrc

CMD ["/bin/bash"]
```


### Command to build the container
```bash
docker buildx build \
--platform linux/amd64 \
-t <docker_username>/mne-freesurfer:latest \
--push .
```
