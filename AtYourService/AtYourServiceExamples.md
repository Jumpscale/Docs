## AYS Examples

We believe that the best way to understand something is through example.

## Create a NodeJS service templates

### Binary Files

In case there are binary files then they can be uploaded to any binary git repository.
This is optional, can also use a packaging system of the OS or any other download mechanism.
We explain here how to put binaries on one of our GIT repo's, this is just as example

- Create a repo on [Aydo](https://git.aydo.com) with the name: *nodejs* - Contact us on *info@incubaid.com* if you need access.
- Download Linux binaries service of nodejs from [here](http://nodejs.org/)
- Extract the contents of that service in a directory called (nodejs)
- Initialize a git Repo in that directory, commit changes and push to remote nodejs repo on [Aydo](https://git.aydo.com)
     
```
cd nodejs
git init
git add -A
git commit -m 'Initializing Nodejs Package'
git remote add origin https://git.aydo.com/binary/nodejs.git #Relace with proper URL
git push -u origin master
```
- Check [https://git.aydo.com/binary/nodejs/tree/master](https://git.aydo.com/binary/nodejs/tree/master) for an example on the binary data

### AYS Metadata Service Template

- To create a metadata for a package, ```cd /opt/code/github/jumpscale/ays_jumpscale7```
- Create a directory called nodejs that will hold the package metadata
- Add to it, our 3 config files ```service.hrd```, ```instance.hrd``` and ```actions.py```
- This is not a server app, that needs to run/stop/.... , we only need the ```node```&```npm``` tools that's why ```actions.py``` is not required for this particular service, so we leave it empty
- We need only to tell config file where to get binary package and where to put it, this can be added to ```service.hrd```

- define the GIT URL of the binary package
- e.g. we use
    - shell git.url='https://git.aydo.com/binary/nodejs.git'

- We can later refer to the ```git.url``` using the syntax ```$(git.url)```
* We need to tell the script that we are defining a downloadable git block
* We do this as follows:

```cfg
git.export.1=
  url:$(git.url),
  source:'',
  dest:'/opt/nodejs/,
  link:False
```

* Define ```git.export.2```,  ```git.export.3```, ... if you want several GIT Blocks.
  * This will clone the repo into /opt/nodejs and that is it.
       
* Test package installation locally
  - Use ```ays install -n nodejs```
  - If error happens:
    - Fix error in configuration files
    - clean up previous installation using ```ays reset -n nodejs```
    - Reinstall package using ```ays install -n nodejs```
  - If all OK:
    - ```/opt/code/github/jumpscale/ays_jumpscale7``` is a git repo, so commit and push changes to [ays_jumpscale](https://github.com/Jumpscale/ays_jumpscale7) in order to publish the package
    - If you don't have access, contact us at info@incubaid.com]

* normal install nodejs from other node
  * ```ays mdupdate``` or alternatively pull/update metadata repo 
      * This comes from ```/opt/code/github/jumpscale/ays_jumpscale7```
  * ```ays install -n nodejs```


## Create a MongoDB service template

### Binary Files

* 1st Add binary data to binary repo @[Aydo](https://git.aydo.com/binary).
  * under the path ```/opt/code/git/binary/``` create a directory called mongodb
  * Inside the directory, add mongodb installation files
  * Push new changes [If you don't have access, please contact us at info@incubaid.com]

* Because Mongodb is already added to our Repo, please take a look following repo
  * [https://git.aydo.com/binary/mongodb/tree/master](https://git.aydo.com/binary/mongodb/tree/master)


### AYS Metadata Service Template

see [ays_jumpscale7](https://github.com/jumpscale/ays_jumpscale7)

* under the path ```/opt/code/github/ays_jumpscale7/``` create a directory called mongodb
* under ```/opt/code/github/ays_jumpscale7/openfire``` create 3 files:

#### service.hrd

* The main configuration file
* Because it uses HRD format, we can even define variables and reuse them inside that file.

* Similar to shell script we can define var info@incubaid.comiable using ```(VAR=VAL)``` then later we use the variable using ```$(VAR)```

* service.hrd knows by default several system variables (which you can use) like:
  * ```$(system.paths.base)``` This is the main path for jumpscale instalation default is ```/opt/jumpscale/```
  * ```$(system.paths.var)``` refers to ```/opt/jumpscale7/vars``` a place to put package configuration data and files that may be used by the package like database files in case of a database package
  * ```$(service.instance)``` refers to the instance name of the package, usually we have one instance and its name is always ```main```, in some cases we may have more than one instance for a package with different names but one of them will be always called ```main```


* Define Max number of instances to run on one machine to 1 ``` instances.maxnr=1 ```

* Provide supported Platform for that package ``` platform.supported=linux64, ```

* Define the git URL for the binary files

```cfg
git.url='http://git.aydo.com/binary/mongodb'
```

* Investigate [http://git.aydo.com/binary/mongodb](http://git.aydo.com/binary/mongodb) to see that it has only one sub-directory called (bin) under which we have mongo executables
* Our intention is to tell the configuration file that we need to move those executables to the proper destination ```/opt/mongodb/bin``` but because the [http://git.aydo.com/binary/mongodb](http://git.aydo.com/binary/mongodb) binaries will be cloned, we need the new location to just refer to the binary repo path in ```/opt/code/git/binary/mongodb```


```cfg
git.export.1=
   url:$(git.url),  # we use the git URL defined above
   source:'mongodb/bin', # this is the relative path under $(git.url) :http://git.aydo.com/binary/mongodb/mongodb/bin
   dest:'/opt/mongodb/bin', # destination on file system
   link:True,  # make sym link form /opt/code/git/binary/mongodb/mongodb/bin to /opt/mongodb/bin
```

* If Mongodb binary repo has another directory **This is not the case** called ```newPath```, then we can use ```git.export.2=``` to define its destination upon installation

```cfg
git.export.2=
   url:$(git.url),  # we use the git URL defined above
   source:'mongodb/newPath',
   dest:'/opt/mongodb/newPath', # destination on file system
   link:True,

```

* You can add ```git.export.3   git.export.4   ...... ``` to define multiple destinations

* Now it's time to define processes and the same as in ```git.export.number``` we can define multiple processes.

``` cfg
process.1=
    cmd:'rm -f /opt/jumpscale7/var/mongodb/main/mongod.lock;export LC_ALL=C;/opt/mongodb/bin/mongod --dbpath $(system.paths.var)/mongodb/$(service.instance)/ --smallfiles --rest --httpinterface',
    args:,
    prio:10,
    env:,
    cwd:'/opt/mongodb/bin',
    timeout_start:60,
    timeout_stop:10,
    ports:27017;28017,
    startupmanager:tmux,
    filterstr:'bin/mongod' 

```

* ```--dbpath $(system.paths.var)/mongodb/$(service.instance)/```  put the database files under the directory ```/opt/jumpscale7/vars/mongodb/main``` Note that this directory is not there by default that is why it's needed to be created [this will be handled by the file actions.py ]explained later
* ```cwd``` is the place where the process will start [usually contains the binary file that we'll use to start the process
* ```cmd``` the command that will start the process
* ``` args``` arguments to the ```cmd``` , in this particular case we don't need it
* ```ports``` package used ports, those ports used to get the process PID when trying to stop it
* ``` startupmanager``` : we use tmux by default to start the process inside
* ```prio```: package priority 
      
### actions.py

* This file is used to configure the life cycle of the package from the time before actual downloading until it dies

* You may not use file frequently for all packages you create, but it's an important file that gives you fine control over the package you're creating
* Suppose for mongodb service you want to make sure that your ubuntu  system doesn't have already mongodb installation, then you may put some code in ```actions.py``` in the prepare function which runs before actual installation to remove older installations of mongodb
* ``` j.system.fs.createDir("$(system.paths.var)/mongodb/$(jp.instance)")``` creates the dir ```/opt/jumpscale7/vars/mongodb/main``` in which we will put the database files


```python
def prepare(self,**args):
   """
   this gets executed before the files are downloaded & installed on approprate spots
   """
   j.do.execute('apt-get purge \'mongo*\' -y')
   j.do.execute('apt-get autoremove -y')
   j.system.platform.ubuntu.stopService("mongod")
   j.system.platform.ubuntu.serviceDisableStartAtBoot("mongod")
   j.system.fs.createDir("$(system.paths.var)/mongodb/$(jp.instance)")
```
     
### instance.hrd

* Usually contains definition for parameters that we need to ask user about but in the same time provide default value for it, just in case user is happy with default values.
* In case of mongodb, no need for that file, but it's handy in other places

```cfg
host=@ASK type:str default:'127.0.0.1'
port=@ASK type:int default:27017
replicaset=@ASK descr:'Name of replicaset, leave empty if not part of replicaSet'

```
* If this file has parameter definitions, user will be prompted to provode values for those params during installation and those param names can be used in either ```actions.py``` or ```service.hrd``` and will be substituted with those values.
* in ``service.hrd``` you can use $(instance.port) to substitute for the port value (chosen by user)
