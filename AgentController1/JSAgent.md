JSAgent
=======

Description
-----------

The JSAgent has multiple purposes. It acts as an agent towards the
AgentController it makes connections to it and asks for tasks. It
schedules Jumpscript by interval and keeps track of processes.

When the JSAgent receives a task from the AgentController it validates
if it should be execute sync or async or on which queue. When it should
be execute async it executes it itself. When the job however has a queue
or is requested to be execute async it is put on the correct queue, when
the queue is empty and async is true the default queue is used.

how to debug a JSAgent
----------------------

```shell
jsprocess disable -n jsagent
```

open a new console and do:

```shell
cd /opt/jumpscale/apps/jsagent/
python jsagent.py --instancename=main --debug
```

you will now see the output from the jsagent + worker processes

to check e.g. that jsagent reloads do

```shell
jsac reload
```
