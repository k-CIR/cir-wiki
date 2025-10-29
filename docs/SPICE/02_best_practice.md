---
title: Best practices for using SPICE
---

## Data organization
Raw imaging data collected at CIR are generally gathered in the corresponding project folder under `/data/projects/<project_name>/raw/`. While every user manage their own home directory and may store exploratory results or experimental analysis here, it is recommended that processed data and analysis results are stored in the **project** folder. This ensures that all data related to a project are centralized and accessible to all project members and unnecessary duplication of data is avoided.

## Version control
Using [Git](https://git-scm.com/) for version control of analysis scripts is highly recommended. It allows you to keep track of changes, collaborate with others, and revert to previous versions if needed. It also makes your analysis, and research, traceable and reproducible.

!!! tip "Recommended read"
    [Coderefinery](https://coderefinery.github.io/git-intro/motivation/) offers some excellent motivation and use cases, highlighting the benefits of using Git for version control.

Use a remote repository hosting service like [GitHub](github.com) or [GitLab](gitlab.com) to enable collaboration and provide backup for your code.

Comment and document your code thoroughly to make it easier for your future self (and others) to understand its purpose and functionality. With the AI tools available today, there really is no excuse for not having well documented code!

## Code organization
Organize your code into modules or packages to improve readability and maintainability. This can help you and others navigate and modify the codebase more easily.

!!! tip "Recommended read"
    The paper [Seven quick tips for analysis scripts in neuroimaging](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007358) provides simple and effective guidelines for organizing analysis scripts.

Compartmentalize code for your different projects or pipelines in separate conda environments to avoid dependency conflicts and ensure reproducibility. Anaconda comes pre-installed on SPICE and is the recommended way to manage your environments and packages.

