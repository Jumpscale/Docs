watchdog
========

server = watchdog manager
-------------------------

to install

```shell
ays configure -n grid_node
ays install -n webdis
ays install -n watchdogmanager
```

to use client
-------------

this will make sure the following HRD params are added:

```cfg
grid.watchdog.secret=
grid.watchdog.addr=
```

make sure they are filled in properly where you want to use watchdog
functionality secret is a long key, providing security for your grid the
secret needs to be the same for the FULL grid.

the addr is a comma separated list for addr to use to send watchdogs too

```python
import JumpScale.baselib.watchdogclient
j.tools.watchdogclient.send("cpu.core","OK",90)
```

types of watchdogs
------------------
