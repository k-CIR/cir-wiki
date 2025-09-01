---
title: Contribute to wiki
---

# Contribute to this wiki
The simplest way to make substantial contributions to the wiki, like adding a section or page, is to clone the wiki to your local machine and make changes there. This way you can continously monitor how your changes will look once they are published, making sure the structure and pages looks like you expect them to.

This page will guide you through the process of cloning the wiki, running it locally, and making changes to it. If the technical side of things seem daunting or you run in to problems, you can [post and issue on the Github repository](https://github.com/k-CIR/cir-wiki/issues) and we will help you out.

## Clone the wiki
Step one is to clone the wiki to your local machine. To do this, go to its [Github repository](https://github.com/k-CIR/cir-wiki) and clone the default `dev` branch.

![Copy SSH adress]({{ picture_path }}/sshadress_screenshot.png){ width="500" }
/// caption
Copy the SSH address of the repository from the repository page.
///

This assumes that you already set up an SSH key on your computer that is connected to your github account. Having an SSH key on your computer, paired with your github account is how github knows who you are and allows you to suggest tracked changes to the repository. If you have not set up an SSH key, you can follow [the instructions here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) to do so. While this takes a few minutes to set up, it is a one-time task that is well worth the effort.

Then, use `git clone <SSH adress>` to clone the repository to your local machine. This will create a folder called **cir-wiki** in your current directory.

## Install and run MkDocs
To run the wiki locally, you need to have [MkDocs](https://www.mkdocs.org/) installed. If you have Python installed, you can install MkDocs using pip (package installer for Python). Running the command below will install MkDocs and companion packages used by this wiki.

`pip install mkdocs mkdocs-material pymdown-extensions mkdocs-include-dir-to-nav mkdocs-macros-plugin`

If you want to set up an new conda environment for this, you can do so with the following commands:

`conda create -n mkdocs_env --channel=conda-forge mkdocs mkdocs-material pymdown-extensions mkdocs-macros-plugin`

Then, activate the environment with:

`conda activate mkdocs_env`

The `mkdocs-include-dir-to-nav` package is not available in conda, you need to install it with pip after activating the environment by running:

`pip install mkdocs-include-dir-to-nav`

You are now ready to run the wiki locally. To do so, navigate to the **cir-wiki** folder and run: `mkdocs serve`

![MkDocs in terminal]({{ picture_path }}/mkdocs_terminal.png){ width="750" }
/// caption
Running MkDocs in the terminal. Note the address where the wiki is running locally.
///

If you use your favourite browser to now go to the address shown in the terminal (usually `http://127.0.0.1:8000/`), you will see your local version of the wiki, running on your computer.

## Make your life easier
To make your life easier, use a purpose built text editor to work with the wiki. For example, using [Visual Studio Code](https://code.visualstudio.com/), you get syntax highlighting, source control integration (git) and can easily navigate between different documents. Open the **cir-wiki** folder in VS Code and you will see all the files and folders that make up the wiki.

## The config file - mkdocs.yml
The wiki is configured using a file called `mkdocs.yml` in the root of the repository. This file contains the configuration for the wiki, such as the title, theme, and navigation structure. You should only have to consider yourself with the navigation structure, which is defined under the `nav` key in the config file. The navigation structure is a list of pages and sections that will be displayed in the sidebar of the wiki.

![Navigation structure]({{ picture_path }}/nav_screenshot.png){ width="600" }
/// caption
The navigation structure in the `mkdocs.yml` file. Found below specifiations for the theme and plugins.
///

## Add a page

TBA

## Add an image

TBA

## Add a section

TBA