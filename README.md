About JumpScale
===================

[JumpScale](http://www.jumpscale.com/) is **A cloud automation product** and a branch from what used to be Pylabs. About 5 years ago Pylabs was the basis of a cloud automation product which was acquired by
[SUN Microsystems](http://www.oracle.com/us/sun/index.html) from a company called [Q-Layer](http://incubaid.com/successes/Q-Layer/). In the mean time we are 3 versions further and we rebranded to [JumpScale](http://www.jumpscale.com/).

Main Features
-------------
- a large library of convencience functions for mainly system automation
- portal framework (markdown & confluence format, very easy to create macro's)
- osis = object storage & indexing system (db layer on top of mongogb, mysql, postgreswl, ...)
- a system abstraction layer to manage many applications, services & clouds
- a ssh management layer (use ssh to manage large amounts of apps, os'es, ...)
- a package management system (called at your service (AYS))
- a full life cycle management system for apps (called at your service (AYS))
- a agent & agentcontroller (1 in python, 1 in golang) for managing thousands of nodes
- a framework to manage a grid of nodes like 1 with lots of macro's created for the portal
- a rest based application server (as part of the portal)
- lots of best practicices how to do things
- a portforwarding system to allow secure access to all your services even if behind firewalls (part of agentcontroller 2)

    Jumpscale is the result of 15 years of developing cloud products & tools to support us.
    Its being used in most of our products in the incubaid group.
    We are 100% committed to make this an even more mature framework with community backing (which is today not the case mainly because of the poor documentation)

roadmap
--------
- 8.0
    - we are porting certain area's to golang
        - our agent/agentcontroller (done but still need to integrate in our portal)
    - lots better documentation, looking for help, over the years this documentation came together but its not consistent enough & not clear enough, we need lots of improvements. 
    - new version of osis (based on even) and fully integrated in our portal
    - safekeeper (an exciting system to securely remotely manage an environment)
    - reactivate our cloudrobot (is message based robot for automating your daily sysadmin life)
- 8.1
    - we are porting certain area's to golang
        - portal framework (planned but not for 8.0)
        - ays (planned but not for 8.0)

How To Get Started
------------------
-   [Installation](GettingStarted/Install.md)
-   [Getting Started](GettingStarted/Home.md)
-   [How to work with AtYourService](AtYourService/AtYourServiceIntro.md)
-   [Tricks in IPython with JumpScale](GettingStarted/IPythonTricks.md)

More Info
--------

- [API Documentation](http://despiegk.gitbooks.io/jumpscaleapi/content/)
- Main gitgub repo's
    - [JumpScale Core Repo](https://github.com/Jumpscale/jumpscale_core7):
    - [Jumpscale Prototypes](https://github.com/jumpscale/jumpscale_prototypes)
    - [AtYourService metadata](https://github.com/Jumpscale/ays_jumpscale7) 
    - [AtYourService binary repo's](http://git.aydo.com/binary)
- Docs in other format
    - [Jumpscale Docs In PDF](https://www.gitbook.com/download/pdf/book/despiegk/jumpscale)
    - [Jumpscale Docs In EBook (epub)](https://www.gitbook.com/download/epub/book/despiegk/jumpscale)
    - [Jumpscale API Docs In PDF](https://www.gitbook.com/download/pdf/book/despiegk/jumpscaleapi)
    - [Jumpscale API Docs In EBook (epub)](https://www.gitbook.com/download/epub/book/despiegk/jumpscaleapi)

Known Issues
=============
* See bug list on github: https://github.com/Jumpscale/jumpscale_core7/issues

Help us improve JumpScale
=============================
* for feedbacks, or to get access to this repo, contact us on info@incubaid.com

License
========

[JumpScale](http://www.jumpscale.com/) is a BSD 2-Clause License

Changes From JumpScale 6
========================

* **main**: Lots of simplifications in core.
* **installer**: much cleaner installer 
* **HRD**: now the main and only configuration format *(some ideas from [toml](https://github.com/toml-lang/toml))*
* **AtYourService**: 100% reworked  system based on *([git](http://git-scm.com/) only)*
* **process management**: now part of AtYourService *(no separate module)*
* **j.do**: more powerful and a good way to create bootstrap scripts *(look at [installer] (Install))*
* **Removed**: blobstor !!! and replaced by git based repositories for binary files
* **In progress**: a new agent written in golang
* **In progress**: [python3](https://www.python.org/download/releases/3.0/) support, [AtYourService](/AtYourService/AtYourServiceIntro.md) drivers for [[KVM](http://www.linux-kvm.org/page/Main_Page), [Docker](https://www.docker.com/), [Ubuntu](http://www.ubuntu.com), [OpenWRT](https://openwrt.org/), [Windows](http://windows.microsoft.com/en-us/windows/home), ..]

