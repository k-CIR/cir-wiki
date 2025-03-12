


## Structure of the wiki
In the docs directory each facility is added as top level and an index.md is included to describe the facility. Subdirectories can be added and markdown-files in each subdirectory is included in the navigation automatically if parent directory is included in the mkdocs.yml file.

```bash
docs
│   ├── natmeg
│   │   ├── index.md
│   │   ├── stimulus-equipment
│   │   │   ├── audio
│   │   │   │   ├── Audio-mixer.md
│   │   │   │   ├── ...
│   ├── resources
│   │   └── wiki_images
│   │       ├── ADA8200_P0ATL_Front_XL.png
│   │       ├── ...
└── mkdocs.yml
```

To make the navigation look nicer add title in the header parameters of the markdown file.

```markdown
---
title: Audio mixer specifiations
---
```


Navigation of the mkdocs.yml
```yml
nav:
  - Home: index.md
  - NatMEG: 
    - natmeg/index.md
    - Stimulus Equipment:
      - Audio: natmeg/stimulus-equipment/audio
```

See [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) for more options on navigation and theme


## Install locally

Clone the repository then you need a few python packages

Using pip:
```bash
pip install mkdocs mkdocs-material pymdown-extensions mkdocs-include-dir-to-nav
```

Using conda
```bash
conda create -n mkdocs_env mkdocs mkdocs-material pymdown-extensions mkdocs-include-dir-to-nav

conda activate mkdocs_env

```

`mkdocs serve` to run locally
