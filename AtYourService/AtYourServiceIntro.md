## AtYourService Details

### Introduction

**AtYourService**: a self-healing application framework

AtYourService let you create so called 'service recipes' that can be used to represent nearly anything. From your datacenter infrastructure to a server cluster.
AtYourService will create a hierarchy of folders in which are contained all the metadata about your services (see [AtYourServiceRemote](AtYourServiceRemote.md) for examples)

AtYourService will make sure that applications get installed 

It's kind of like Ubuntu's ```apt-get & service``` and ```ant``` tools all together in one easy command line tool that can control a whole cloud.

Instead of the traditional (complicated) way of handling services data through databases or file system, AtYourService make use of [Revision Control Systems](http://en.wikipedia.org/wiki/Revision_control), especially [git](git-scm.com) in an elegant and modern way that suits A cloud architecture.

AtYourService preserves the installation/build state, so if for example an installation/build attempt fails, next time the process will continue from the last point, this behavior of course could be changed, but it's the default behavior and it's very handy.

AtYourService is able to install several instances of a service on the same machine.



### AtYourService system features

* Powerful Command line tool (One command to rule them all) : see [AtYourService CMD](AtYourServiceCmd.md)
* Install multiple instances of a service on the same node/machine : see [Service Instance](ServiceInstance.md)
* Multiple Operating systems support, virtualization backends, and containers
  - [Docker](http://www.docker.com)
  - [KVM](http://www.linux-kvm.org/)
  - [Ubuntu](http://www.ubuntu.com/)
  - Other Operating System (OS)
* Uses [git](http://git-scm.com) powered servers to hold data & metadata
* Powerful & easy full life cycle management Using only 3 metadata files
  - service.hrd : is the main metadata file which is valid for all service instances
  - instance.hrd : is the metadata file relevant for 1 instance of a service
  - actions.py or actions.lua : the livecycle management actions


### AtYourService Basics

#### AtYourService has a recipe and an instance

*ays template* or *ays recipe*
- are the definition of how a service needs to get deployed
- in such a recipe we describe
    - parameters relevant for the aysi (AtYouService instance)
    - how to startstop the aysi
    - how to monitor the aysi
    - how to install the binary files for the aysi
    - how to configure the aysi
    - how to get stats from the aysi
    - how to export/import the ays data


*Instances*

Example: Running several instances of mongodb on the same machine on different ports.

```shell
#the following will init mongodb template as an instance
ays init -n mongodb # Use default instance name (main)
ays init -n mongodb -i mongo2 #instance name is (mongo2)
```


#### Each AtYourService instance (aysi) has a unique key

key in format $domain|$name!$instance@role ($version)

different format examples
+ $domain|$name!$instance
+ $name
+ !$instance
+ $name!$instance
+ @role

version is added with ()
+ e.g. node.ssh (1.0)

### AYS instances can be found using this key format

e.g.
```shell
#find 1 atyourservice which role mongodb and then start (if not started yet), if more than 1 then this will fail
ays start -n @mongodb

#find all ays of role node and print status
ays status -n @node

#find an ays which has instance name: ovh4
ays status -n !ovh4

```

if more than 1 aysi found then there will be an error

### each AYS Recipe (aysr) has a role

if the role is not specified in the 'service.hrd' under parameter 'role'
the the role will be auto filled in with first part of name
e.g. if ays name is node.ssh the role will become node

these roles are used to define categories of aysr e.g. ays which define a node & how to execute cmds on a node
another example role is e.g. ns

### init redis local or remote (example)

local

```
ays init -n redis -i --data 'param.name:system param.port:7766 param.disk:0  param.mem:100 param.ip:127.0.0.1 param.unixsocket:0 param.passwd:'
```

remote

```
ays init -n node.ssh -i ovh4 --data "ip:94.13.18.89 ssh.port:22"

ays init -n redis -i system --parent '!ovh4' --data 'param.name:system param.port:7766 param.disk:0  param.mem:100 param.ip:127.0.0.1 param.unixsocket:0 param.passwd:'

```

notice how we use as key !ovh4 this means any ays with instance name ovh4 will be used (only if found 1)
more complete way to specify would have been 'node.ssh!ovh4' or '!ovh4$node' #means instance ovh4 from role node

remark: install will only happen after 'ays apply'

### producers & consumers

- Each aysi can consume a service delivered by a producer
- A producer is another aysi which delivers a service
- when installing you can specify the consumption you are doing by e.g. '-c mongodb!main' construct
    - easier is to specify by means of role e.g. '-c $mongodb' will only work if not more than 1 found per node or global 

### usage of dependencies

```
dependencies.global             = mongodb,influxdb
dependencies.node              = portal_lib,influxdb_client,mongodb_client
```

- dependencies are specified with a role name (not based on ays name)
- global & node dependencies
  - global dependencies are dependencies betweey aysi on level not specific to 1 node e.g. portal needs mongodb
  - node dependencies are specific for 1 node, they tell us which local(=node) aysi need to be locally installed 
- if the local & global deps. are properly defined then there is no need to specify the consumption flag
  - ays will lookup a service with specified role on global or node level, if only 1 is found the the consumption will configured automatically

### some special atyourserive recipe args

```
ns.enable = True
hrd.return = True
```

- ns.enable means we will be using the nameservice service, is not relevant for all services
- hrd.return means that after install the hrd needs to be copied back to the site from which we install (only relevant for remote working)

### Remarks (BAD)

@todo do better

- A service data is separated into 2 types
    - Metadata (configuration files to determine how to manage the whole life cycle)
    - Binary data (Actual service data)
- By default, Metadata are saved into [Metadata Repo](https://github.com/jumpscale/ays_jumpscale7) & binaries into [Binary Repo](http://git.aydo.com/binary)
- After a clean installation of jumpscale framework, both [Metadata Repo](https://github.com/jumpscale/ays_jumpscale7) & [Binary Repo](http://git.aydo.com/binary) will be cloned locally to paths:  ```/opt/code/github/jumpscale/ays_jumpscale7/``` & ```/opt/code/git/binary/``` respectively.
- When installing locally links will be made between local system & repo, when installing remotely rsync will be used over SSH to push the files to remote location.

- To install mongodb we do:
```
ays mdupdate #Update metadata locally
ays install -n mongodb #Install
```

- ```ays install -n mongodb``` will 1st search ```/opt/code/github/jumpscale/ays_jumpscale7/``` for a directory called mongodb which contain info on where to get mongodb binaries and how to install them.
- If directory found, installation process starts, otherwise aborts.
- This means we need frequently to do ```ays mdupdate``` to keep local metadata repo @```/opt/code/github/jumpscale/ays_jumpscale7/``` in sync with [Remote Metadata Repo](https://github.com/jumpscale/ays_jumpscale7)


