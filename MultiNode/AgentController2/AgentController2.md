jsagentcontroller
===================

JumpScale Agentcontroller in Go

# Installation
```
go get github.com/Jumpscale/jsagentcontroller
```

# Running jsagencontroller
```
go run main.go -c agentcontroller.toml
```

# REST Service
Note: GID, NID and JID is extracted from URL or from JSON body

## GET /[gid]/[nid]/cmd
* If some commands are in redis queue (*$GID:$NID*), it's directly pushed
* If nothing is pending, waits (long poll) for a command from redis

## POST /[gid]/[nid]/log
* Push logs to redis queue (*$GID:$NID:LOG*)

## POST /[gid]/[nid]/result
* Push job result to redis queue (*$JID*)

## GET /[gid]/[nid]/stats
* Save logs in influxdb database
* Format: {timestamp: xxx, series: [[key, value], [key, value], ...]}

# Commands Reader
* Wait for commands from *\_\_master\_\_* queue
* Decode JSON from this queue
* Push JSON on the right queue based on GID:NID



---


JSAgent
========

* [JSAgent](JSAgent/Home.md)
* [AYS Integration](JSAgent/AYS-Integration.md)
* [Command Syntax](JSAgent/Command-Syntax.md)
* [Examples](JSAgent/Examples.md)
* [Port-forwarding](JSAgent/Port-forwarding.md)
* [Stats](JSAgent/Stats.md)
* [Using-Client-Certificate-For-Security](JSAgent/Using-Client-Certificate-For-Security.md)
* [agent-configuration](JSAgent/agent-configuration.md)