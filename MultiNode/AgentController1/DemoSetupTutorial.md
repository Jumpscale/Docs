Demo Setup For AgentController & Agents
=======================================

This tutorial will explain how to get started with a debug environment
for the agentcontroller. This can be used to experiment with Jumpscale,
the Grid & Agentcontroller Framework.

Requirements
------------

-   Ubuntu 14.04 64-bit (It possibly works on other ubuntu versions too
    but is not tested)
-   Install jumpscale in debug mode
    [see](../../GettingStarted/Install.md)

Installation
------------

### Install an all-in-1 grid master

A grid master has everything required to manage a grid

### Working with multiple agents in debug mode

On a new Ubuntu 14.04 server, [install jumpscale in debug
mode](../../GettingStarted/Install.md), then run the following
command

```shell
ays install -n jsagent
```

This will install a new jsagent. The jsagent agent registers itself to
the agentcontroller.

Starting the agent
------------------
This will be automatically done with installation. But if you want to manually install the JSAgent, do:

```shell
ays start -n jsagent
```

Of-course you can put this agent in 'init.d' or so (PS on the roadmap
(Q4 2014) the agent will register itself optionally in init.d and work
as daemon)

Test the worker functionality on the gridmaster node itself
-----------------------------------------------------------

```shell
cd /opt/jumpscale/apps/jsagent/
python workertest.py
```

In case you are wondering, this is the code inside 'workertest.py'

```python
#!/usr/bin/env python

from JumpScale import j

j.application.start("jumpscale:workertest")

import JumpScale.baselib.redisworker

def atest(msg):
    print(msg)
    # raise RuntimeError("e")
    return msg

w=j.clients.redisworker

def test1():
    print("START")
    for i in range(10):
        job=w.execFunction( method=atest, _category='mytest', _organization='unknown', _timeout=60, _queue='default', _log=True,_sync=True, msg="this is a test")
    print(job)
    print("STOP")

print(w.getQueuedJobs())

test1()

j.application.stop()
```

Here you execute a function remotely in the worker of the jsagent. This
will be executed async and result returned. This is handy to schedule &
launch long running jobs.

Visit [Gridportal](../GridPortal/Home.md) and see the different nodes (agents)
------------------------------------------------------------------------------

The grid portal gives you an overview what is going on your environment
single or multigrid.

-   [Nodes](../gridportal/Nodes.md)
-   [Jobs](../gridportal/Jobs.md)
-   [Errors](../gridportal/ECOs.md)

It also provides a [status overview](../gridportal/checkstatus).

Executing Jumpscripts
---------------------

One can use [JSAC](shellcommands/JSAC) to interact with the AgentController and
execute remote scripts.

```
jsac exec -o jumpscale -n exec -a cmd:hostname -nid 1
Job:

achost: 127.0.0.1
args: {cmd: hostname}
category: jumpscale
cmd: exec
errorreport: false
gid: 77
guid: f2b57166e0a9_77_2
id: 2
jscriptid: 48
log: false
nid: 1
parent: null
queue: ''
result: [0, 'jsagent

    ']
resultcode: 0
roles: []
sessionid: 77_1_0_91c0b8f2-725d-4599-824a-c42a4f1c9021
state: OK
timeStart: 1413724079
timeStop: 1413724079
timeout: 600
wait: true
```

Tutorial How To add a Jumpscripts
=================================

```
cd /opt/jumpscale/apps/agentcontroller/jumpscripts/
mkdir tutorial
cd tutorial
```

Add with your favorite editor a file
'/opt/jumpscale/apps/agentcontroller/jumpscripts/tutorial/sumtutorial.py'
here containing.

```
from JumpScale import j
descr = "This is a tutorial jumpscripts"
name = "sumtutorial" # this is the name to use to call the jumpscripts if left blank the filename is used
category = "tutorial"
author = "tutorial@jumpscale.org"
organization = "jumpscale"
license = "BSD"
version = "1.0"
async = False
log = True
roles = []
period = 0
queue = ''

def action(a, b):
    return int(a) + int(b)
```

Reload Agentcontroller / JSAgent
--------------------------------

```
jsac reload
```

Execute Newly created Jumpscript and see it in the portal
---------------------------------------------------------

```
jsac exec -o jumpscale -n sumtutorial -a "a:2,b:5" -nid 1
Job:

: _ckey: ''
_meta: [system, job, 1]
achost: localhost
args: {a: 2, b: 5}
category: jumpscale
cmd: sumtutorial
errorreport: false
gid: 1
guid: 2673542ba6fa_1_1
id: 1
jscriptid: 9
log: true
nid: 1
parent: null
queue: ''
result: 7
resultcode: null
roles: []
sessionid: 1_1_0_5204ca41-812e-4073-a1d3-5b08605ce355
state: OK
timeStart: 1413876868
timeStop: 0
timeout: 600
wait: true
```

You can find the Job result in the [Portal](/grid/jobs)

What happens when error accurs.
-------------------------------

Lets say for instance we pass a character instead of a number to our sum
Jumpscript

```
jsac exec -o jumpscale -n sumtutorial -a "a:2,b:a" -nid 1
Job:

: _ckey: ''
_meta: [system, job, 1]
achost: localhost
args: {a: 2, b: a}
category: jumpscale
cmd: sumtutorial
errorreport: false
gid: 1
guid: 2673542ba6fa_1_2
id: 2
jscriptid: 9
log: true
nid: 1
parent: null
queue: ''
result: {appname: jsagent, backtrace: "Traceback (most recent call last):\n~   File\
    \ \"/usr/local/lib/python2.7/dist-packages/JumpScale/grid/jumpscripts/JumpscriptFactory.py\"\
    , line 108, in executeInProcess\n    return True, self.module.action(*args, **kwargs)\n\
    ~   File \"/opt/jumpscale/apps/processmanager/jumpscripts/tutorial/sumtutorial.py\"\
    , line 16, in action\n    return int(a) + int(b)\n~ ValueError: invalid literal\
    \ for int() with base 10: 'a'\n", backtraceDetailed: "  File \"/usr/local/lib/python2.7/dist-packages/JumpScale/grid/jumpscripts/JumpscriptFactory.py\"\
    \ Line 108, in executeInProcess\n    return True, self.module.action(*args, **kwargs)\n\
    \  File \"/opt/jumpscale/apps/processmanager/jumpscripts/tutorial/sumtutorial.py\"\
    \ Line 16, in action\n    return int(a) + int(b)\n", category: '', code: /opt/jumpscale/apps/processmanager/jumpscripts/tutorial/sumtutorial.py,
  epoch: 1413877236, errormessage: 'Exec error procmgr jumpscr:jumpscale_sumtutorial
    on node:1_1 ValueError: invalid literal for int() with base 10: ''a''', errormessagePub: '',
  exceptionclassname: ValueError, exceptioninfo: '{"message":"invalid literal for
    int() with base 10: ''a''"}', exceptionmodule: null, funcfilename: /usr/local/lib/python2.7/dist-packages/JumpScale/grid/jumpscripts/JumpscriptFactory.py,
  funclinenr: 16, funcname: action, gid: 1, guid: '1_1_18', id: 18, jid: 0, level: 1,
  masterjid: 0, nid: 1, pid: 0, tags: 'jscategory:tutorial jsorganization:jumpscale
    jsname:sumtutorial', tb: null, type: '2'}
resultcode: null
roles: []
sessionid: 1_1_0_c9d07840-18d3-43ec-aa0b-736d72955e2e
state: ERROR
timeStart: 1413877236
timeStop: 0
timeout: 600
wait: true
```

If we now go look at the [Jobs](/grid/jobs) we will se our job is in
status error. And shows a stacktrace of what went wrong.

Recurring Jumpscripts
---------------------

One can schedule Jumpscript on specific nodes by combining roles and
period.

```
from JumpScale import j
descr = "This is a tutorial jumpscripts"
name = "backupdbtutorial" # this is the name to use to call the jumpscripts if left blank the filename is used
category = "tutorial"
author = "tutorial@jumpscale.org"
organization = "jumpscale"
license = "BSD"
version = "1.0"
async = False
log = True
roles = ['db']
period = 3600
queue = ''

def action():
    j.system.fs.copyDirTree('/opt/jumpscale/var/db', '/mnt/data')
```

This script will run every hour (3600 seconds) on all nodes that have
the 'role' db.
