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
export GITHUBUSER=''
export GITHUBPASSWD=''
export JSBASE='/opt/jumpscale7'
export SANDBOX=0
export JSBRANCH='ays_unstable'
export AYSBRANCH='ays_unstable'
export JSGIT='https://github.com/Jumpscale/jumpscale_core7.git'
export AYSGIT='https://github.com/Jumpscale/ays_jumpscale7.git'
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

## Offline mode

To do an offline installation you can install JumpScale in offline mode.

1. Make sure that the required packages are installed which are:

  * curl
  * git
  * ssh
  * python2.7
  * python


2. Make sure that the required repos are cloned in the right direcctory

  ```
  http://git.aydo.com/binary/base_python.git -> /opt/code/git/binary/base_python
  http://git.aydo.com/binary/grafana.git -> /opt/code/git/binary/grafana
  http://git.aydo.com/binary/mongodb.git -> /opt/code/git/binary/mongodb
  https://git.aydo.com/binary/nginx.git -> /opt/code/git/binary/nginx
  https://git.aydo.com/binary/nodejs.git -> /opt/code/git/binary/nodejs
  https://git.aydo.com/binary/openvcloud.git -> /opt/code/git/binary/openvcloud
  http://git.aydo.com/binary/openvstorage.git -> /opt/code/git/binary/openvstorage
  http://git.aydo.com/binary/openwrt.git -> /opt/code/git/binary/openwrt
  http://git.aydo.com/binary/ovs_branding.git -> /opt/code/git/binary/ovs_branding
  http://git.aydo.com/binary/python-cloudlibs.git -> /opt/code/git/binary/python-cloudlibs
  http://git.aydo.com/binary/redis.git -> /opt/code/git/binary/redis
  http://git.aydo.com/binary/routeros.git -> /opt/code/git/binary/routeros
  http://git.aydo.com/binary/statsd.git -> /opt/code/git/binary/statsd
  http://git.aydo.com/binary/web_python.git -> /opt/code/git/binary/web_python
  https://github.com/Jumpscale/ays_jumpscale7.git -> /opt/code/github/jumpscale/ays_jumpscale7
  https://github.com/Jumpscale/jumpscale_core7.git -> /opt/code/github/jumpscale/jumpscale_core7
  https://github.com/Jumpscale/jumpscale_portal.git -> /opt/code/github/jumpscale/jumpscale_portal
  ```
3. Execute [the installation script](https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/7.0/install/InstallTools.py) using `--offline` argument

`curl https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/7.0/install/InstallTools.py | python - --offline`


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

