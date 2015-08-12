Install of jumpscale
=====================

Ubuntu
------
use these install scripts to make your life easy

```shell
sudo -s
#if ubuntu is in recent state & apt get update was done recently
cd /tmp;rm -f install.sh;curl -k https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/master/install/install.sh > install.sh;bash install.sh
```

above will copy a boostrap.py file in your temp folder e.g. /tmp, you can manually execute from there

MacOSX
------
go to shell in MacOSX
```shell
cd $TMPDIR;rm -f install.sh;curl -k https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/master/install/install.sh > install.sh;bash install.sh
```

ENV ARGUMENTS which can be set to change behaviour of install
------------------------------

```
export GITHUBUSER = ''
export GITHUBPASSWD = ''
export SANDBOX = 0
export JSBASE = '/opt/jumpscale7'
export JSGIT = 'https://github.com/Jumpscale/jumpscale_core7.git'
export JSBRANCH = 'master'
export AYSGIT = 'https://github.com/Jumpscale/ays_jumpscale7.git'
export AYSBRANCH = 'master'
```

* insystem means use system packaging system to deploy dependencies like python & python packages
* base is location of root of JumpScale
* JSGIT & AYSGIT allow us to chose other install sources for jumpscale as well as AtYourService repo

if you want to use other branch set an environment variable
e.g.
```shell
export JSBRANCH=@ys
```
the standard branch = master

More Information About Installation Process
=======================

- [Install Process Details](Install%20Process%20Details.md)

Install Needed Packages
=======================

```shell

# To get a portal running and install its required services, use:
ays install -n singlenode_portal

# Or To install a single node grid locally:
ays install -n singlenode_grid
```

You can read more about AtYourService [here](../AtYourService/AtYourServiceIntro.md)

to use in sandbox
-----------------

only in the case you installed a sandbox then you need to set your env before using jumpscale

To use sandbox load env variables. (Not requires for ays or js commands)

```shell
source /opt/jumpscale7/env.sh 
#or any other location of jumpscale
```

test jumpscale
--------------

to get shell
```shell
js
```

example through ipython
```shell
ipython
from JumpScale import j
```

