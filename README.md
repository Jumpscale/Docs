About JumpScale
===================

[JumpScale](http://www.jumpscale.com/) is **A cloud automation product** and a branch from what used to be Pylabs. About 5 years ago Pylabs was the basis of a cloud automation product which was acquired by
[SUN Microsystems](http://www.oracle.com/us/sun/index.html) from a company called [Q-Layer](http://incubaid.com/successes/Q-Layer/). In the mean time we are 3 versions further and we rebranded to [JumpScale](http://www.jumpscale.com/).

License
========

[JumpScale](http://www.jumpscale.com/) is a [BSD 2-Clause License](JumpScale-License)

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
* **In progress**: [python3](https://www.python.org/download/releases/3.0/) support, [AtYourService](AtYourServiceIntro) drivers for [[KVM](http://www.linux-kvm.org/page/Main_Page), [Docker](https://www.docker.com/), [Ubuntu](www.ubuntu.com), [OpenWRT](https://openwrt.org/), [Windows](http://windows.microsoft.com/en-us/windows/home), ..]

Known Issues
=============
* See bug list on this wiki.

Help us improve JumpScale
=============================
* for feedbacks, or to get access to this repo, contact us on info@incubaid.com
* Help us [improve documentation](ContributeToDocs)
* Check out other repos related to [JumpScale](https://github.com/Jumpscale/jumpscale_core7):
 * [Jumpscale Prototypes](https://github.com/jumpscale/jumpscale_prototypes)
 * [AtYourService metadata](https://github.com/Jumpscale/ays_jumpscale7) & [AtYourService binaries / Aydo](http://git.aydo.com/org/binary) repos

How To Get Started
------------------
-   [Architecture and General Overview](Architecture)
-   [Installation](Install)
-   [Getting Started: The Basics](GettingStartedBasic)
-   [How to work with AtYourService](AtYourServiceIntro)
-   [Tricks in IPython with JumpScale](IPythonTricks)

Concepts
--------

-   [Human Readable Data Format](Human%20Readable%20Data%20Format)

Extensions
----------

-   [Code Management](CodeManagement)