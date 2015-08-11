System Management Over SSH
==========================

Jumpscale has a lot of tools inside to manage remote systems over ssh.

SSH connection tools & BASIC SSH INFO (must read)
----------------------------------
How to deal with SSH on lower level & how to configure your system around it.

- [SSHBasics](SSHBasics)

SSH Remote System Tools
-----------------------

Some jumpscale functions to deal with a remote system over SSH
- [SSHRemoteSystem](SSHRemoteSystem)

cuisine
-------

A set of very nice tools to do basic system management to a node
This is all based on https://github.com/sebastien/cuisine 

Use this tool if you want basic management.
It does not support all platforms as well.

```
#in our example we will do all to localhost
c=j.remote.cuisine.connect("localhost",22)
```

for documentation see [Cuisine](Cuisine)

### how to make cuisine more silent

```
c=j.remote.cuisine.connect("localhost",22)

c.fabric.api.env['connection_attempts'] = 5
c.fabric.state.output["running"]=False
c.fabric.state.output["stdout"]=False
```

### how to get cuisine to use a specific key

```
c.fabric.key_filename="/home/despiegk/.ssh/id_rsa"
```

### hoe to get cuisine to use passwd

```
c.fabric.api.env.password = 'PASSWORD'
```

### More info about cuisine

* [Cuisine](Cuisine)
    * we have updated some documentation & made it easier to know what can be done



SSH SAL tools (j.ssh)
-----------------

SAL = System Abstraction Layer tools
The idea is we use SSH to remote manage certain systems (e.g. ubuntu, unix in general, openwrt, ...)
For that a thin abstraction layer is created called SAL and this makes it easy for the developer to interact with the remote system.

The original specs for this tool are on
https://github.com/Jumpscale/jumpscale_core7/blob/master/specs/ssh_enabled_SALs.md
Since then quite some modifcations are done.

Its build on top of cuisine

to get started

```
c=j.ssh.connect("localhost",verbose=True) #this returns a cuisine object (like above) which is verbose in output, if you don't want that put on False
ub=j.ssh.ubuntu.get(c) #use the ubuntu methods, feed it the cuisine connection

In [10]: ub=j.ssh.ubuntu.get(c)

In [11]: ub.
ub.connection                   ub.executeRemoteTmuxCmd         ub.executeRemoteTmuxJumpscript  ub.network                      

In [11]: ub.network.
ub.network.commit   ub.network.ipGet    ub.network.ipReset  ub.network.ipSet    ub.network.manager  ub.network.nics     ub.network.nsGet    ub.network.nsSet    

In [11]: ub.network.nics

Out[11]: ['eth0', 'lo', 'tun0']

```

like usual check the internal documentation using ipshell & ?


j.ssh specific functionality
------------------------

the docs for the specific salls are found below

- [SSHUbuntu](SSHUbuntu)
- [SSHUnix](SSHUnix)

