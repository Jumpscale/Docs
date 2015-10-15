# Quick Start

## requirements

The JumpScale portal requires the JumpScale framework to be installed.
So if you didn't do so [install JumpScale](../GettingStarted/Install.md).

## To install your own portal with all local dependencies installed

Install base portal package

```
ays init -n singlenode_portal
ays init -n portal -i myportal
ays apply
```

Your portal code can now be placed @ `$basedir/apps/portal/myportal`

## Control your portal

Start your portal with `ays start -n portal -i myportal`  
Stop your portal with `ays stop -n portal -i myportal`

## install portal with minimal dependencies
```
#first make sure redis is installed
ays install -n redis -i system --data 'param.name:system param.port:7766 param.disk:0  param.mem:100 param.ip:127.0.0.1 param.unixsocket:0 param.passwd:'


```

## install portal with all dependencies
```
#first make sure redis is installed
ays install -n redis -i system --data 'param.name:system param.port:7766 param.disk:0  param.mem:100 param.ip:127.0.0.1 param.unixsocket:0 param.passwd:'

#install mongodb
ays init -n mongodb --data "param.host:0.0.0.0 param.port:27017 param.replicaset:"

#

```
