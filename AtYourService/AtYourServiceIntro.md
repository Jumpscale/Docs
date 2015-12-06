## AtYourService Details

### Introduction

**AtYourService** is a self-healing application management framework for cloud infrastructure

its like a combination of
- Package manager like Ubuntu's ```apt-get```
- Service manager like Ubuntu's ```service```
- Configuration manager like [ansible](http://www.ansible.com)
- Build tool like [ant](http://ant.apache.org)
- Monitoring tool

<br/>**What is a service?**

A service, either local or remote, is an abstraction for almost anything:
- Simple package i.e ```mongodb```
- A server cluster i.e ```mongodb cluster```
- Data center infrastructure i.e ```Rack(s) or a cluster of machines```
- Abstraction for several other services

<br/>**One command to rule them all**

We use only one command ```ays``` to control everything:
- Configure a service and all its dependencies (if any): ```ays init -n service-name```
- Install service: ```ays apply```
- Start a service: ```ays start -n service-name```
- Stop a service: ```ays stop -n service-name```
- Check status for all installed services: ```ays status```
- Check status for only local services (on this machine) ```ays status --local ```
- Update metadata (like Ubuntu's ```apt-get update```) ```ays mdupdate```

<br/>**AtYourService structure**

- (1) Metadata Repos
 - Metadata repos contain all the metadata defining the life cycle of a service, from pre-installation to monitoring
 - An example is [ays_jumpscale7](https://github.com/Jumpscale/ays_jumpscale7), defining the full life cycle of the AYS JumpScale7 services
 - You can configure AtYourService to use one or more repos:
  - Edit the file ```/opt/jumpscale7/hrd/system/atyourservice.hrd```
  - Add new section for every metadata repo you want to add
    ```shell
        #here domain=jumpscale, change name for more domains
        metadata.jumpscale             =
            branch:'master',
            url:'https://github.com/Jumpscale/ays_jumpscale7',
        #add this domain
            metadata.openvcloud        =
            url:'https://git.aydo.com/0-complexity/openvcloud_ays',
```
 - AtYourService uses [git](http://git-scm.com) to manage its metadata
  - All metadata repos are cloned into ```/opt/code```
   - Repos from github are cloned into ```/opt/code/github```
   - Repos from other git repos are cloned into ```/opt/code/git/```
    - So ```https://github.com/Jumpscale/ays_jumpscale7``` is cloned into ```/opt/code/github/jumppscale/ays_jumpscale7```
  - Updating/cloning metadata repos:
   - Manually cloning individual repos is achieved with ```git pull```
   - Use ```ays mdupdate``` in order to update all existing repos and clone missing (not yet cloned) repos
 - You can configure a service by editing the recipe of the service, which is made of following files
  - **service.hrd** is the main metadata file which is valid for all service instances
  - **instance.hrd** is the metadata file relevant for 1 instance of a service
  - **actions_mgmgt.py** defines actions executed from the management location
  - **action_node.py** defines executed remotely on a node
  - **actions_tmpl.py** defines the "static" actions for the recipe itself, that do not require to first create a service instance in order to call them

- (2) Installation Directory
 -  For each locally and remotely installed service instance a sub directory under ```/opt/jumpscale7/hrd/apps``` will contain the configuration files, the recipe of the running service instance
 - The name of the sub directory reflects the name of the service and the name of the instance: ```{$service-name__$instance-name}```
 - For the AYS JumpScale services itself for example, as defined in the git clone ```/opt/code/github/jumpscale/ays_jumpscale7```, it will be as below, where the name of each instance is ```main``` which is the default instance name when no other name was specified in the recipe:

 ```shell
  root@ovc2:~# ls /opt/jumpscale7/hrd/apps/                    
  agentcontroller__main         osis__main
  agentcontroller_client__main  osis_client__jsagent
  base__main                    osis_client__main
  grafana__main                 osis_eve__main
  grafana_client__main          portal__main
  gridportal__main              portal_client__main
  influxdb__main                portal_lib__main
  influxdb_client__main         redis__system
  jsagent__main                 singlenode_grid__main
  mailclient__main              singlenode_portal__main
  mongodb__main                 statsd-collector__main
  mongodb_client__main          statsd-master__main
  nginx__main                   web__main
```


### AtYourService Basics

#### Recipes and instances

*AYS Recipe*
- Defines the full life cycle from pre-installation, over installation, to upgrades and monitoring of a service, all described in the above mentioned recipe files:
    - service.hrd
    - instance.hrd
    - action*.py
- In a recipe we describe
    - Parameters relevant for a service instance
    - How to start/stop the instance
    - How to monitor the instance
    - How to install the binary files for the instance
    - How to configure the instance
    - How to get stats from the instance
    - How to export/import the data


*Instances*

Example: Running several instances of MongoDB on the same machine on different ports.

```shell
#the following will init the MongoDB recipe as an instance
ays init -n MongoDB # Use default instance name (main)
ays init -n MongoDB -i mongo2 #instance name is (mongo2)
```


#### Each AtYourService instance has a unique key

Key in format $domain|$name!$instance@role ($version)

Different format examples
+ $domain|$name!$instance
+ $name
+ !$instance
+ $name!$instance
+ @role

Version is added with ()
+ e.g. node.ssh (1.0), where "node.ssh" is the name of the service, which in this case contains a "." where "node" is the role of the service and "ssh" the name of the instance

### AYS instances can be found using this key format

e.g.
```shell
#find 1 service instance with role MongoDB and then start (if not started yet), if more than 1 then this will fail
ays start -n @mongodb

#find all service instances with role node and print their status
ays status -n @node

#find a service instance which has instance name ovh4
ays status -n !ovh4

```

If more than 1 instance is found then there will be an error

### Each service has a role

If the role is not specified in the 'service.hrd' under parameter 'role' then the role will be auto filled from the first part of name, e.g. if the AYS service name is "node.ssh" the role will become node

Roles are used to define categories of AYS recipes e.g. AYS which define a node & how to execute commands on a node, another example of a role is e.g. ns

### Init redis local or remote (example)

local

```
ays init -n redis -i --data 'param.name:system param.port:7766 param.disk:0  param.mem:100 param.ip:127.0.0.1 param.unixsocket:0 param.passwd:'
```

remote

```
ays init -n node.ssh -i ovh4 --data "ip:94.13.18.89 ssh.port:22"

ays init -n redis -i system --parent '!ovh4' --data 'param.name:system param.port:7766 param.disk:0  param.mem:100 param.ip:127.0.0.1 param.unixsocket:0 param.passwd:'

```

Notice how we use as key !ovh4 this means any ays with instance name ovh4 will be used (only if found 1)
more complete way to specify would have been 'node.ssh!ovh4' or '!ovh4$node' #means instance ovh4 from role node

Remark: install will only happen after 'ays apply'

### Producers & Consumers

- Each service instance can consume a service delivered by a producer
- A producer is another service instance delivering a service
- When installing you can specify the consumption you are doing by e.g. '-c mongodb!main' construct
    - Easier is to specify by means of role e.g. '-c $mongodb' will only work if not more than 1 found per node or global

### Usage of dependencies

```
dependencies.global            = mongodb,influxdb
dependencies.node              = portal_lib,influxdb_client,mongodb_client
```

- Dependencies are specified with a role name (not based on AYS name)
- Global & node dependencies
  - Global dependencies are dependencies between AYS instance on level not specific to 1 node e.g. portal needs MongoDB
  - Node dependencies are specific for 1 node, they tell us which local(=node) AYS instance need to be locally installed
- If the local & global dependencies are properly defined then there is no need to specify the consumption flag
  - AYS will lookup a service with specified role on global or node level, if only 1 is found the the consumption will configured automatically

### Some special AtYourService recipe args

```
ns.enable = True
hrd.return = True
```

- ns.enable means we will be using the nameservice service, is not relevant for all services
- hrd.return means that after install the hrd needs to be copied back to the site from which we install (only relevant for remote working)
