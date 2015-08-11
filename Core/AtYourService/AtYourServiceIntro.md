AtYourService Details
=================

Introduction
------------

**AtYourService** An hybrid between a modelisation tool and a package manager

**Modelisation tool**:
AtYourService let you create so called 'service templates' that can be used to represent nearly anything. From your datacenter infrastructure to a server cluster.
AtYourService will create a hierarchy of folder in which are contained all the metadata about your services (see [AtYourServiceRemote](AtYourServiceRemote) for examples)

**Package manager**
It's kind of like Ubuntu's ```apt-get & service``` and ```ant``` tools all together in one easy command line tool that can control a whole cloud.
Instead of the traditional (complicated) way of handling services data through databases or file system, AtYourService make use of [Revision Control Systems](http://en.wikipedia.org/wiki/Revision_control), especially [git](git-scm.com) in an elegant and modern way that suits A cloud architecture.
AtYourService preserves the installation/build state, so if for example an installation/build attempt fails, next time the process will continue from the last point, this behavior of course could be changed, but it's the default behavior and it's very handy.
AtYourService is able to install several instances of a service on the same machine.

Migration from JPackage to AtYourService
----------------------------------------
It's possible that you find bugs or not implemted feature in AtYourService. In that case, fill open a bug so we can work on it.  

### From an already installed jumpscale system:
if you want to start using @ys with your old installation of Jumpscale make sure you updated these files :
- rename **/opt/jumpscale7/hrd/system/jpackage.hrd** to **/opt/jumpscale7/hrd/system/atyourservice.hrd**  
- you can safely remove **/opt/jumpscale7/jpackage_actions** cause this folder is no longer use. the actions files of a service are now location next to its HRD file in **/opt/jumpscale7/hrd/apps**/opt/jumpscale7/hrd/apps
be carefull is you just move your actions.py files to this new location without any other verification cause it's most likely that it will not be direclty compatible with @ys.  
See this link to know [How to convert jpackage to service](AtYourServiceMigration.md)

AtYourService system features
---------------------------

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


AtYourService Basics
------------------

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


- In order to create a service template called ```fancyPackage``` (Without going into much details) you've to do:
    - Publish service binary data
          - Initiate a local git repo anywhere in your file system called ```fancyPackage```.
          - Add the binary data files to this repo
          - Push this repo to [Remote Binary Repo/Aydo](http://git.aydo.com/org/binary)
          - If you need access to that repo, contact us on info@incubaid.com
    - Create service templates
          - create a directory under ```/opt/code/github/jumpscale/ays_jumpscale7/``` called ```fancyPackage```
          - Inside the service template directory, add 3 files *(actions.py, service.hrd, instance.hrd)*
          - Those metadata files draw the life cycle plan of the service from creation to monitoring.
          - Metadata will contain the URL for binary data repo for that service on [Remote Binary Repo/Aydo](http://git.aydo.com/org/binary)
          - In the next sections we'll explain in details how to configure and create a new service.

- Examples see: [AtYourServiceExamples](AtYourServiceExamples)
- [How to define dependencies in service.hrd](AtYourServiceDeps)
- [How to define the exports (link between git repo's & filesystem)](AtYourServiceExports)
- [How to define a process in service.hrd](AtYourServiceProcess)
- [How to define Ubuntu features in service.hrd](AtYourServiceUbuntu)
- [How to use the command line](AtYourServiceCmd)
- [Locations of the important files](AtYourServiceFileLocations)
- [AtYourServiceRemote](AtYourServiceRemote)


How to configure a new service
------------------------------

the 3 important files

- **actions.py**
     - contains ```Actions``` class with predefined functions that do certain actions
     - here're the steps involved in a service installation
          - [```prepare```, ```check_requirements```] actions are executed in order.
          - Then actual service files will be downloaded/installed
          - [```configure```, ```check_uptime_local```] will be executed in order.
              * ```check_uptime_local``` : Checks if process already running (from previous installation)
              * If process running try execute ```stop``` for graceful stop
              * execute  ```check_uptime_local``` to check if process still running
              * If process still running try execute ```halt``` for hard stop
          - execute ```start``` using the config files to start the application
          - execute ```check_uptime_local``` to check process is started
          - execute ```monitor_local``` to check local application is running & healthy
          - execute ```monitor_remote``` to check if remote application is running & healthy
     - see [AtYourServiceActions]

- **service.hrd**
- **instance.hrd**

- [HRD format](Human-Readable-Data-Format) files + 1 python file)



Installed AtYourService files
-------------------------

* [Service templates file locations](AtYourServiceFileLocations)
