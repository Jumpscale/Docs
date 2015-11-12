## AtYourService Details

### Introduction

**AtYourService**: a self-healing application framework meant for the cloud and can be used remotely

- Package manager like Ubuntu's ```apt-get```
- Service manager like Ubuntu's ```service```
- Configuration manager like [ansible](http://www.ansible.com)
- Build tool like [ant](http://ant.apache.org)
- Monitoring tool.

**What is a Service?**

- A service either local or remote is an abstraction for almost anything:
 - Simple package i.e ```mongodb```
 - A Server cluster i.e ```mongodb cluster```
 - Data center Infrastructure i.e ```Rack(s) or a cluster of machines```
 - Abstraction for several other services

**One command to rule them all**

- We use only one command ```ays``` to control everything
 - Configure a service and all its dependencies (if there):
 ```ays init -n service-name```
 - Install service:
 ```ays apply```
 - Start a service:
 ```ays start -n service-name```
 - Stop a service:
 ```ays stop -n service-name```
 - Check status for all installed services:
 ```ays status```
 - Check status for only local services (on this machine)
 ```ays status --local ```
 - Update metadata (like Ubuntu's ```apt-get update```)
 ```ays mdupdate``` 


**Atyourservice structure**

-  (1) Metadata Repos
 - Metadata repos contain metada required to install services
 - Metadata for a service defines the life cycle of a service starting from pre-installation to monitoring
  - An example is [ays_jumpscale7](https://github.com/Jumpscale/ays_jumpscale7)
  - you can configure atyourservice to use one or more repo(s)
    - Edit the file ```/opt/jumpscale7/hrd/system/atyourservice.hrd ```
    - Add new section for every metadata repo you want to add
    ```sh
        #here domain=jumpscale, change name for more domains
        metadata.jumpscale             =
            branch:'master',
            url:'https://github.com/Jumpscale/ays_jumpscale7',
        # add this domain
            metadata.openvcloud            =
            url:'https://git.aydo.com/0-complexity/openvcloud_ays',
```
   - atyourservice uses [git](http://git-scm.com) to manage its medata data
     - all metadata repos are cloned into ```/opt/code```
      - repos from github are cloned into ```/opt/code/github```
      - repps from other git repos are cloned into ```/opt/code/git/```
      - ```https://github.com/Jumpscale/ays_jumpscale7``` is cloned into ```/opt/code/github/jumppscale/ays_jumpscale7```
     - Updating/cloning metadata repos:
        - Do it manually for individual repos using ```git pull```
        - Use ```ays mdupdate``` which will update existing repos and clone missing ones
        - Non cloned repos defined in ```/opt/jumpscale7/hrd/system/atyourservice.hrd ```  cloned automatically when you do ```ays apply```
  - You can configure a service using only 3 files
    - service.hrd : is the main metadata file which is valid for all service instances
    - instance.hrd : is the metadata file relevant for 1 instance of a service
    - actions.py or actions.lua : the livecycle management actions

- (2) Installation directory
 - contains the final configuration files for each installed service either locally or remotely
 - Installation directory is in ```/opt/jumpscale7/hrd/apps ```
 - by default the default isntance name of a service is called ```main```
 - if service is located in ```/opt/code/jumpscale/ays_jumpscale7``` then the domain name is called ```jumpscale```

 - Installed services have their config files installed by default into ```/opt/jumpscale7/hrd/apps/{$domain_$name_$instance}```

 - ```sh
  root@ovc2:~# ls /opt/jumpscale7/hrd/apps/                    
  jumpscale__agentcontroller__main         jumpscale__osis__main
  jumpscale__agentcontroller_client__main  jumpscale__osis_client__jsagent
  jumpscale__base__main                    jumpscale__osis_client__main
  jumpscale__grafana__main                 jumpscale__osis_eve__main
  jumpscale__grafana_client__main          jumpscale__portal__main 
  jumpscale__gridportal__main              jumpscale__portal_client__main 
  jumpscale__influxdb__main                jumpscale__portal_lib__main
  jumpscale__influxdb_client__main         jumpscale__redis__system
  jumpscale__jsagent__main                 jumpscale__singlenode_grid__main
  jumpscale__mailclient__main              jumpscale__singlenode_portal__main
  jumpscale__mongodb__main                 jumpscale__statsd-collector__main
  jumpscale__mongodb_client__main          jumpscale__statsd-master__main
  jumpscale__nginx__main                   jumpscale__web__main```
  

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
