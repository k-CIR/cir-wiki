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

## How to edit a page
Editing the content of the wiki is simple. To do it correctly you need to know a bit about git and github to so that edits are tracked properly.

**Step one:** Get an account on [github](https://github.com/).

Now, if you click the button for "Edit this page" on any page on the wiki, you'll be taken to the corresponding markdown file in the repository on github.

<figure style="text-align: center;">
    <img src="{{ picture_path }}/edit_page_screen.png" alt="Edit this page screenshot" width="500">
    <figcaption>The "Edit this page" button - top right of every page on this wiki.</figcaption>
</figure>

Here, you can click the pen to "Edit this file on github", assuming you are logged in.

<figure style="text-align: center;">
    <img src="{{ picture_path }}/edit_githubmd_screen.png" alt="Edit this page" width="500">
    <figcaption>Edit this file on github.</figcaption>
</figure>

You can now make your changes. When you are done, to avoid conflicts from people modifying the same document, you can not save your changes and have them published directly. Instead, you propose the change and create a ticket for an admin of the wiki to review and approve. In git-nomencalture you will **commit** your changes to a new version of the repository (called a **branch**) and create a request to have your changes pulled in to repository by an admin of the wiki.

<figure style="text-align: center;">
    <img src="{{ picture_path }}/commit_screenshot.png" alt="Screenshot commit" width="500">
    <figcaption><b>1.</b> Commit your changes and <b>2.</b> Write a commit message and propose changes in new branch.</figcaption>
</figure>

To be continued..