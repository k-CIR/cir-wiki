# The CIR wiki (for contributors)

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

To make the navigation look nicer add title in the header parameters of the markdown file. This will be used in the menu instead of the filename. Files are sorted alphabetically so for a specific order add a number in the beginning of the filename.

```markdown
---
title: Audio mixer specifications
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
pip install mkdocs mkdocs-material pymdown-extensions mkdocs-include-dir-to-nav mkdocs-macros-plugin
```

Using conda
```bash
conda create -n mkdocs_env mkdocs mkdocs-material pymdown-extensions mkdocs-include-dir-to-nav mkdocs-macros-plugin

conda activate mkdocs_env

```

`mkdocs serve` to run locally

## How to contribute to the wiki
You can contribute in two ways:  

**Through Pull Requests**

If you have edits or new content to add, fork the repository, make your changes, and submit a pull request for review. It’s good practice to:  
- Request at least one reviewer from the main collaborators of the CIR repository.  
- Assign the pull request to yourself and/or others who need to work on it.  

**Through Issues**

If you have suggestions, corrections, or requests but can't make the changes yourself, open an issue to bring it to our attention.  

