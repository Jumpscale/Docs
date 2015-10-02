
## easy client

### init

- the current j.ac.get goes to j.ac.getAdvanced(...)

- j.ac.get(... gets new client)

### execution of cmds, jumpscripts

```
cl=j.ac.get()
#cmd is e.g. 'ls /' no separate args
#path is where to execute the cmd
#die is std True
#timeout is std 5 sec, if timeout raise an error
rc,stdout,stderror=cl.execute(cmd,path,die,timeout)

#cmds is content of a bash file which will be executed remotely
rc,stdout,stderror=cl.executeBash(gid,nid,cmds,die,timeout)

#cmds is content to execute in jumpscale format
rc,stdout,stderror=cl.executeJumpscriptContent(cmds,die,timeout)

#will execute existing jumpscript by name (js needs to be available on remote)
result=cl.executeJumpscript(gid,nid,domain,name,die,timeout,data="") #data send to it for std in (I believe that was the std way how we are doing it)
result is whatever organized return using our conventions of using stdout from script

jobs=cl.executeJumpscriptAsync(gid=None,nid=None,roles=[],domain,name,data="") #data send to it for std in (I believe that was the std way how we are doing it)
#if nid specified then roles not used, roles=[] means we ignore it and then we execute over gid & nid
#gid==None: means all gids
#nid==None: means all nids

for job in jobs:

    #job is a nice python object with relevant info about job
    job.check() #will ask agent2 about status and fill in job.status, job.mem, job.cpu
    #for mem & cpu, should be avg over e.g. last 5 min (does agent support that?, if not give last)
    job.status  = done,running,warning or error
    job.mem=
    job.cpu= #is in percentage of total
    job.id = unique id to job
    job.result= #will be none if job still running

    #loglevels see LogLevels page
    logitems=job.getLogs(levels="1-5")
    logitems=job.getLogs(levels="*")
    logitems=job.getLogs(levels="1,2,3")

    job.wait(timeout=5) #wait till job done

    if job.state=="error":
        print job.error  #error is a full error object from jumpscale (ECO)
        ...

    if job.state=="warning":
        print job.warning  #warning is a full error object from jumpscale (ECO)
        ...


```

some remarks
- so when we want to do more complex stuff & execute over multiple agents, jumpscripts need to be used
- error in jumpscript (ECO)
-- new errorhandler is created who dumps the output as json & gets captured (log level 8 or 9)
-- this info can get back serialzed as eco & returned to job.error in case there was error


### agent & process info

```
cl=j.ac.get()
agents=cl.getAgents()
for agent in agents:
    print agent.gid
    print agent.nid
    print agent.hostname
    print agent.macaddr #do as property so we fetch the info when required (all macaddr in list)
    print agent.ipaddr  #do as property so we fetch the info when required (all ip in list)
    print agent.watchdog #time in seconds since last time we saw agent
    print agent.status is : ok, error, unreachable
    print agent.cpu (is cpu aggregated for all processes running underneath agent and agent itself)
    print agent.mem (is mem aggregated for all processes running underneath agent and agent itself)

    for process in agent.processes:
        print process.name
        print process.path ???
        print process.mem ???
        print process.cpu ???
        ...

    #make sure when properties are used that if agent is error or unreachable right errorcondition is thrown (j.events....)



```

### sync

```
cl=j.ac.get()
share=cl.sync_createshare(gid,nid,path,ignore=[])
#ignore is list of items not to sync
print share.path
print share.gid
print share.nid
print share ... #see what else is relevant

share=cl.sync.getshare(gid,nid,path) #gets existing info
print share.peers (see who is connected with their status !!!, need to know if this share is fully synced !!!)
#info is fetched from the syncthing running on that location
print share.insync (means all peerst have the same data for this share !!!)

share.attach(git,nid,path,readonly=False)
#readonly means that destinations will not be able to modify


```

example with master to 2 agents remote

```
cl=j.ac.get()
#1-1 is master
share_downloads=cl.sync_createshare(1,1,"/opt/downloads",ignore=["*.pyc","*.bak","*/.git/*"])
share_downloads.attach(1,2,"/opt/downloads",readonly=True)
share_downloads.attach(1,3,"/opt/downloads",readonly=True)

```

some of the syncthing agents will have to expose their port to internet, otherwise this will not work, this is not job of this interface


### portforward

```
cl=j.ac.get()
cl.tunnel_create(...)
#make sure you check if agents relevant are accesible and if not tell

```