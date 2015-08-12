## AtYourService Details

### Introduction

**AtYourService** An hybrid between a modelisation tool and a package manager

**Modelisation tool**:
AtYourService let you create so called 'service templates' that can be used to represent nearly anything. From your datacenter infrastructure to a server cluster.
AtYourService will create a hierarchy of folder in which are contained all the metadata about your services (see [AtYourServiceRemote](AtYourServiceRemote.md) for examples)

**Package manager**
It's kind of like Ubuntu's ```apt-get & service``` and ```ant``` tools all together in one easy command line tool that can control a whole cloud.
Instead of the traditional (complicated) way of handling services data through databases or file system, AtYourService make use of [Revision Control Systems](http://en.wikipedia.org/wiki/Revision_control), especially [git](git-scm.com) in an elegant and modern way that suits A cloud architecture.
AtYourService preserves the installation/build state, so if for example an installation/build attempt fails, next time the process will continue from the last point, this behavior of course could be changed, but it's the default behavior and it's very handy.
AtYourService is able to install several instances of a service on the same machine.



### AtYourService system features

* Powerful Command line tool (One command to rule them all) : see [AtYourServiceCmd]
* Install multiple instances of a service on the same node/machine : see [ServiceInstance]
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

#### Instances
Example: Running several instances of mongodb on the same machine on different ports.

@todo

```
ays install -n mongodb #Use default instance name (main)
ays install -n mongodb -i mongo2 #instance name is (mongo2)
```

#### templates

@todo

### Remarks

@todo do better

- A service data is separated into 2 types
    - Metadata (configuration files to determine how to manage the whole life cycle)
    - Binary data (Actual service data)
- By default, Metadata are saved into [Metadata Repo](https://github.com/jumpscale/ays_jumpscale7) & binaries into [Binary Repo](http://git.aydo.com/org/binary)
- After a clean installation of jumpscale framework, both [Metadata Repo](https://github.com/jumpscale/ays_jumpscale7) & [Binary Repo](http://git.aydo.com/org/binary) will be cloned locally to paths:  ```/opt/code/github/jumpscale/ays_jumpscale7/``` & ```/opt/code/git/binary/``` respectively.
- When installing locally links will be made between local system & repo, when installing remotely rsync will be used over SSH to push the files to remote location.

- To install mongodb we do:
```
ays mdupdate #Update metadata locally
ays install -n mongodb #Install
```

- ```ays install -n mongodb``` will 1st search ```/opt/code/github/jumpscale/ays_jumpscale7/``` for a directory called mongodb which contain info on where to get mongodb binaries and how to install them.
- If directory found, installation process starts, otherwise aborts.
- This means we need frequently to do ```ays mdupdate``` to keep local metadata repo @```/opt/code/github/jumpscale/ays_jumpscale7/``` in sync with [Remote Metadata Repo](https://github.com/jumpscale/ays_jumpscale7)


