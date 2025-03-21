---
title: How to edit this wiki
---

From the most famous wiki of them all, [Wikipedia](https://en.wikipedia.org/wiki/Wiki):

*A wiki is a form of hypertext publication on the internet which is **collaboratively** edited and managed by its audience directly through a web browser. A typical wiki contains multiple pages that can either be edited by the public or limited to use within an organization for maintaining its internal knowledge base.*

To maintain this wiki as a useful resource, each user share the responsibility of keeping it comprehensive, relevant and up to date. If you think something is missing or unclear - please make an addition or suggest a change. 

## Structure
This wiki is really just a collection of text documents written in [markdown](https://en.wikipedia.org/wiki/Markdown) - a very simple format for creating formatted text. You can check out this [cheat sheet](https://www.markdown-cheatsheet.com/) for some of the syntax used in markdown documents.

These documents are tracked via the version control system [git](https://git-scm.com/), so that changes made are reviewed, tracked and restorable. Git can run locally to track changes of projects, but it is even more useful when a project (or repository) is shared between many editors via a remote repository hosted on [github](https://github.com/).

Each markdown document collected in the repository for this wiki represent one page of the wiki. [MkDocs](https://www.mkdocs.org/) runs in the background to build a site from the documents in the main branch of that repository based on the settings specified in its configuration file `mkdocs.yml`

## How to edit
You can find detailed instructions on how to edit and add pages to the wiki in the README of the repository [here.](https://github.com/k-CIR/cir-wiki/tree/main)