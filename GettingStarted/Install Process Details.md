detailed description of how jumpscale gets installed
====================================================

intro
-----

supported operating systems today.

- ubuntu 14+
- macosx yosimity+ (maybe earlier but not tested)
- slitaz (not very well tested, please report bugs)
- windows 7+ (SOON)

following env variables influence the install behaviour
---------

```
GITHUBUSER = ''
GITHUBPASSWD = ''
SANDBOX = 0
JSBASE = '/opt/jumpscale7'
JSGIT = 'https://github.com/jumpscale7/jumpscale_core7.git'
JSBRANCH = 'master'
AYSGIT = 'https://github.com/jumpscale7/ays_jumpscale7.git'
AYSBRANCH = 'master'
CODEDIR = '/opt/code'
```

- insystem means use system packaging system to deploy dependencies like python & python packages
- base is location of root of JumpScale
- JSGIT & AYSGIT allow us to chose other install sources for jumpscale as well as AtYourService repo

to sandbox or not
-----------

- ONLY on ubuntu we have a sandbox more where the python binaries & libraries get downloaded in a sandbox.
- a sanbox is like a chroot env, which means as much as possible all required files & libraries come from out of this sandbox directory and the OS does not get modified
- on Ubuntu 14+ the std behaviour is this sandboxing method, if your don't want to use it you will have to set SANDBOX = 0

jumpscale install process
-------------------------

- we install by means of downloading a bash (bat) file & executing in std env of OS
- goal is user does not need to manually download packages
- on macosx we use the fantastic package manager brew

the first install script to use is in our main git repo 
- [$github/jumpscale7/jumpscale_core7/install/install.sh](https://github.com/jumpscale7/jumpscale_core7/blob/master/install/install.sh)
- its very easy to create other install scripts which change your required behaviour e.g. set the env arguments differenty and use that as your own bootstrap file

this script will
- install the basic requirements to allow python to take over & from then onwards do all further install in python
    - curl python & git get installed
    - some basic env var's are set
- then the python bootscript file will be downloaded
    - default: [https://raw.githubusercontent.com/jumpscale7/jumpscale_core7/master/install/web/bootstrap.py](https://raw.githubusercontent.com/jumpscale7/jumpscale_core7/master/install/web/bootstrap.py)
    - ofcourse also this fileis really easy to change & get other install behaviour (please investigate the content of this file)

the python bootstrap file will
- download Install Tools
    - [https://github.com/jumpscale7/jumpscale_core7/blob/master/install/InstallTools.py](https://github.com/jumpscale7/jumpscale_core7/blob/master/install/InstallTools.py)
    - which is 1 python script with lots of helper functions in to help you bootstrap an install, please look at that file to understand
- read the environment variables and set python variables
- call the install method on InstallTools: 

```
def installJS(self,base="",clean=False,insystem=True,pythonversion=2,copybinary=True,\
        GITHUBUSER="",GITHUBPASSWD="",CODEDIR="\opt\code",\
        JSGIT="https://github.com/jumpscale7/jumpscale_core7.git",JSBRANCH="master",\
        AYSGIT="https://github.com/jumpscale7/ays_jumpscale7.git",AYSBRANCH="master"\
        ):
    """
    @param pythonversion is 2 or 3 (3 no longer tested and prob does not work)
    if 3 and base not specified then base becomes /opt/jumpscale73

    @param insystem means use system packaging system to deploy dependencies like python & python packages
    @param codedir is the location where the code will be installed, code which get's checked out from github
    @param base is location of root of JumpScale
    @copybinary means copy the binary files (in sandboxed mode) to the location, don't link

    JSGIT & AYSGIT allow us to chose other install sources for jumpscale as well as AtYourService repo

    IMPORTANT: if env var's are set they get priority

    """
```

at the end of this install jumpscale will be installed in minimal form & now you need to use @ys to further install jumpscale packages (@ys = AtYourService).



