## ays command line

```
ays commands:

    install:
    - download all related git repo's (if not downloaded yet, otherwise update)
    - prepare & copyfiles & configure
    - start the app
    list:
    - list the ayss
    stop-start-restart
    build
    - if build instructions are given the build repo's will be downloaded & build started
    - build happens to production dir
    mdupdate
    - update all git repo's which have services metadata
    update
    - go over all related repo's & do an update
    - copy the files again
    - restart the app
    reset
    - remove build repo's !!!
    - remove state of the app (same as resetstate) in jumpscale (the configuration info)
    - remove data of the app
    resetstate
    - remove state of the app (same as resetstate) in jumpscale (the configuration info)
    removedata
    - remove data of app (e.g. database, e.g. vmachine when node ays)
    execute
    - execute cmd on service e.g. ssh cmd on node jp or sql statement on database ...
    - use --cmd with to specify command to be execute
    monitor
    - do uptime check, local monitor & remote monitor check, if all ok return True
    configure
    - configure the app
    cleanup
    - remote old logfiles, ...
    export/import
    - use --url to specify where to import from or export to
    create
    - interactively create a ays
    status
    - display status of installed ayss (domain, name, priority, version, port)
    nodes
    - display all remote nodes available for ays remote execution

usage: ays [-h] [--path PATH] [--noremote] [-q] [-n NAME] [-d DOMAIN]
           [-i INSTANCE] [-f] [--nodeps] [--verbose] [--data DATA] [--cmd CMD]
           [--parent PARENT] [--immediate] [-r] [-s] [--url URL] [--installed]
           {install,list,stop,start,restart,build,prepare,mdupdate,update,reset,resetstate,removedata,monitor,configure,cleanup,export,import,uninstall,push,execute,status,nodes}

positional arguments:
  {install,list,stop,start,restart,build,prepare,mdupdate,update,reset,resetstate,removedata,monitor,configure,cleanup,export,import,uninstall,push,execute,status,nodes}
                        Command to perform

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           path to git config repo to be use
  --noremote            bypass the @remote wrapper

Package Selection:
  -q, --quiet           Put in quiet mode
  -n NAME, --name NAME  Name of ays to be installed
  -d DOMAIN, --domain DOMAIN
                        Name of ays domain to be installed
  -i INSTANCE, --instance INSTANCE
                        Instance of ays (default main)
  -f, --force           auto answer yes on every question
  --nodeps              Don't perfomr action on dependencies, default False
  --verbose             Verbose output.
  -tn TARGETNAME, --targetname TARGETNAME
                        node instance on which to execute the action
  -tt TARGETTYPE, --targettype TARGETTYPE
                        node type on which to execute the action
  -hs HRDSEED, --hrdseed HRDSEED
                        path to an hrd file that contains


Install/Update/Expand/Configure:
  --data DATA           use this to pass hrd information to ays e.g.
                        'redis.name:system redis.port:9999 redis.disk:0'
  --cmd CMD             use this to pass cmd to services e.g. 'ls -l'
  --parent PARENT       parent services (domain__name__instance). Can also
                        define ancestors through 'grandparentdomain__grandpare
                        ntname__grandparentinstance__
                        parentdomain__parentname__parentinstance'
  --immediate           use this to get the first level match of services
  -r, --reinstall       Reinstall found service
  -s, --single          Do not install dependencies

Export/Import:
  --url URL             uncpath to export to or import from

List:
  --installed           List installed ayss

```

## ays command line actions


* ```install``` Configure, install and run a service
* ```uninstall``` Uninstall a service
* ```list --installed``` List all installed services
* ```stop``` Stop a running service
* ```start``` Start a service
* ```restart``` Restart a service
* ```update``` Update and restart a service installation
* ```resetstate``` Clear service state (only)
* ```reset```  Does ```resetstate``` + clean build data + clean service data
* ```cleanup``` Remove Old log files, and do Housekeeping.
* ```monitor``` Monitor the state of a local/remote service
* ```import/export --url=...``` Import/Export service data from/to pre-configured location
* ```build```  Build a service, start from the last unsuccessful build stage
* ```configure``` Reconfigure a service installation runtime parameters
* ```mdupdate``` Like Ubuntu's ```apt-get update```, it update metadata for services
* ```status``` display status of installed ayss (domain, name, priority, version, port)
* ```--data``` pass Config data on the fly
* ```--cmd 'command'``` pass command to execute action of ays
* ```--verbose``` Activate verbose mode
* ```-n serviceName``` Use ```-n``` to pass the service name
* ```-n serviceName -d domainName```  Use ```-d``` to pass domain name.
* ```-n serviceName -i instanceName``` Use ```-i``` to pass instance name
* ```-n serviceName --nodeps``` By default if you do an action to service like start/stop this action will be propagated to all service dependencies which is handy thing, but sometimes for certain actions you do want this only to be applied on the service itself like ```resetstate```, use ```--nodeps``` in those cases.
* ```-- local``` to apply action only to locally installed services
* ```--parent domainName__serviceName__instanceName``` to specify parent for service. For further ancestry, can be used ```--parent ancestorDomain__ancestorName__ancestorInstance:parentDomain__parentName__parentInstance```
* ```--console``` to access the console of a remote service
* ```--targetname serviceInstance --targettype serviceName``` to specify action on remote node
* ```consume --category categoryName producerInstanceName``` to consume specified producer category and instance for this service
* --hrdseed ```prefilledHRD.hrd``` to give the path to an hrd file that contains the instance arguments of a services.
* ```--immediate``` to indicate provided parent path is the exact one to use. If neither path nor parent is path, action will be performed on the root of the configured directory.

## AYS cmd line examples:

```shell
#updates the metadata
ays mdupdate

#updates selected ayss from domain jumpscale
ays install -d jumpscale

#select osis, install osis and its dependencies
ays install -n osis
#next will not look at dependencies
ays install -n osis --nodeps

#Install with hrd configuration
ays install -n redis -i system --data 'redis.name:system redis.port:7766 redis.disk:0  redis.mem:100'
#whatever you pass with --data is used to populate the hrd of the instance

# Show current status of installed AYSes
ays status

# Show current status of locally installed AYSes
ays status --local
```

