---
title: Best practices for using SPICE
---

## Data organization
Raw imaging data collected at CIR are generally gathered in the corresponding project folder under `/data/projects/<project_name>/raw/`. While every user manage their own home directory (i.e. `/data/users/<username>`) and may store exploratory results or experimental analysis here, it is recommended that processed data and analysis results are stored in the **project** folder. This ensures that all data related to a project are centralized and accessible to all project members and unnecessary duplication of data is avoided.

CIR support all projects in using [BIDS](https://bids.neuroimaging.io/), and provide assistance and resources to make your data BIDS-compliant.

See [BIDS on SPICE](05_spiceBIDS.md) for details on how different imaging modalities are organized in BIDS.

BIDS provides a consistent and structured way to organize and describe neuroimaging data, making it easier to share, analyze, and reproduce research findings. Many neuroimaging analysis tools support BIDS data, which will streamline your analysis workflow.

## Version control with Git
Using [Git](https://git-scm.com/) for version control and structure of analysis scripts is highly recommended. It allows you to keep track of changes, collaborate with others, and revert to previous versions if needed. It also makes your analysis, and research, traceable and reproducible.

!!! tip "Recommended read"
    [Coderefinery](https://coderefinery.github.io/git-intro/motivation/) offers some excellent motivation and use cases, highlighting the benefits of using Git for version control.

Comment and document your code thoroughly to make it easier for your future self (and others) to understand its purpose and functionality. With the AI tools available today, there really is no excuse for not having well documented code!

## Use Github to share and collaborate
Using git makes it easy to share and collaborate on code with others. Use a remote repository hosting service like [GitHub](https://www.github.com) or [GitLab](https://www.gitlab.com) to enable collaboration and provide backup for your code. After registering a github account you can set up an SSH key pair to push and pull changes to your remote repository without having to type your password. This is the same principle as for using a [SSH key pair to connect remotely in VScode](03_Vscode_tips.md#login-without-password).

To do this, you need to generate an SSH key pair (one private and one public key) on your local machine and add the public key to your github account. It's called a key-pair, but really you can think of it as a lock (public key) and a key (private key). You generate a key pair, put the lock (public key) on the service you want to access and keep the key (private key) on your local machine. When you connect, the server checks if you have the right key to unlock the lock.

!!! note "Different machines - different keys"
    Even if you are working on SPICE from your laptop - SPICE is a different machine than your local computer. If you edit code on your laptop _and_ SPICE, you will need to set up a separate SSH key pairs on SPICE and on your local machine.

Github has excellent [documentation on how to set up SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). But in a nutshell, to create a new SSH key pair on SPICE, and add its public part to your github account, do the following:

1. Connect to SPICE in terminal or VScode.
2. Generate a new SSH key pair by running: `ssh-keygen -t ed25519 -C "your_email@example.com"` You can press enter to accept the default location and continue without a passphrase.
3. Start the ssh-agent in the background by running: `eval "$(ssh-agent -s)"`
4. Add your SSH private key to the ssh-agent by running: `ssh-add ~/.ssh/id_ed25519`
5. Copy the public part of your SSH key to your clipboard by running: `cat ~/.ssh/id_ed25519.pub` and copying the output.
6. Go to your github account settings, navigate to "SSH and GPG keys" and click "New SSH key". Paste the contents of your clipboard into the "Key" field and give it a descriptive title.

The first time you push or pull changes to/from github from SPICE, you may be prompted to confirm the authenticity of github's server and your identity. Type `yes` to continue when prompted.

To set your git username and email on SPICE, run:

    git config --global user.name "Your Name"
    git config --global user.email "your_email@example.com"

## Code organization
Organize your code into modules or packages to improve readability and maintainability. This can help you and others navigate and modify the codebase more easily.

!!! tip "Recommended read"
    The paper [Seven quick tips for analysis scripts in neuroimaging](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007358) provides simple and effective guidelines for organizing analysis scripts.

Compartmentalize code for your different projects or pipelines in separate conda environments to avoid dependency conflicts and ensure reproducibility. Anaconda comes pre-installed on SPICE and is the recommended way to manage your environments and packages.

