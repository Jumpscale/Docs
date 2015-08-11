Redis
=====

Redis is an open source, BSD licensed, advanced key-value store. It is
often referred to as a data structure server since keys can contain
strings, hashes, lists, sets and sorted sets.

Redis Usage in JumpScale.
-------------------------

Redis is used to cache our in process jobs and used as a queing
mechanism to pass information from one component to the other. Runs on
port 9999

agentcontroller/master node
---------------------------



|Key                       |Type|HashKey|Value|Description                            |
|--------------------------|----|-------|-----|---------------------------------------|
|jobs:last                 |hash|grid id|int  |incremental value for job id           |
|jobs:<gid>                |hash|jobguid|json |All jobs used as cache                 |
|commands:queue:<gid>:<nid>|list|       |json |contains list of jobs that needs to get executed on the gid.nid combintation|
|jobqueue:<jobguid>|list||json|Job object used as return from agent/processmanager/worker|


on each node for workers
------------------------

|Key|Type|HashKey|Value|Description|
|---|----|-------|-----|-----------|
|application|hash|applicationname|json|list of pids of application|
|healthcheck:lastcheck|hash|component name|int|Unix timestamp when component was last checked by monitor|
|healthcheck:monitoring|hash|type|mixed|Used to cache results/errors of healthchecker + lastcheck|
|healthcheck:status|hash|component name|boolean|Last status of component|
|eco:incr:<gid>_<nid>|value||int|Incremental id for eco|
|logs:incr:<gid>_<nid>|value||int|Incremental id for jobs|
|workers:joblastid|value||int|Incremental id for jobs started outside agentcontroller|
|workers:jumpscriptlastid|value||int|Incremental id for jumpscripts stored in cache|
|workers:jumpscripts:id|hash|id of jumpscript|json|Hash with as key the id of the jumpscript and value the jumpscript|
|workers:jumpscripts:name|hash|name of jumpscript|json|Hash with as key the name of the jumpscript and value the jumpscript|
|workers:sessions|hash|sessionid|json|Contains information about applications that make connection to the workers|
|workers:watchdog|hash|component name|int|Unix timestamp containing last heartbeat of component|

