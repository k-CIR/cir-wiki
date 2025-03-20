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

## How to contribute to the wiki
You can contribute in two ways:  

**Through Pull Requests**

If you have edits or new content to add, follow these steps:

1. **Fork** the repository on GitHub.
2. **Create a new branch** for your edits.
3. **Make your changes** and **commit** them.
4. **Push your branch** to your forked repository.
5. **Open a pull request** against the dev branch of this repository.
6. **Request at least one reviewer** from the main contributors of the CIR repository.
7. **Assign the pull request** to yourself and/or others who need to work on it.  

**Through Issues**

If you have suggestions, corrections, or requests but can't make the changes yourself, open an issue to bring it to our attention.  

## Install locally

Clone the repository then you need a few python packages

Using pip:
```bash
pip install mkdocs mkdocs-material pymdown-extensions mkdocs-include-dir-to-nav mkdocs-macros-plugin
```

Using conda
```bash
conda create -n mkdocs_env --channel=conda-forge mkdocs mkdocs-material pymdown-extensions mkdocs-macros-plugin

conda activate mkdocs_env

pip install mkdocs-include-dir-to-nav # not available in conda

```

`mkdocs serve` to run locally

