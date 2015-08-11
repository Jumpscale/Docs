JSAC
====

JumpScale Agentcontroller management script

Help
----

```shell
jsac --help
usage: jsac [-h] [-nid NID] [-r ROLE] [-n NAME] [-o ORGANIZATION]
            [-a ARGUMENTS]
            {reload,exec,listsessions}

positional arguments:
  {reload,exec,listsessions}
                        Command to perform

optional arguments:
  -h, --help            show this help message and exit
  -nid NID, --nodeid NID
                        Use for exec
  -r ROLE, --role ROLE  Use for exec
  -n NAME, --name NAME  Use for exec
  -o ORGANIZATION, --organization ORGANIZATION
                        Use for exec
  -a ARGUMENTS, --arguments ARGUMENTS
                        Use for exec, eg. msg:test
```

Actions
-------

### Reload

Reloads Jumpscripts on agentcontroller and instructs all processmanagers
and workers in the grid to reload aswell. This action is exactly the
same as 'jsgrid reloadjumpscripts'

### Listssions

This commands list all connected session to the agentcontroller handy to
have a quick look which processmanagers have connected to the
agentcontroller and which roles they have

#### Example

```shell
jsac listsessions
Sessions:

computenode.kvm: ['55_1']
master: ['55_1']
node: ['55_1']
```

### Exec

Execute a Jumpscript on a specific node/role passing organization, name
and arguments from the cli and returns the Job

#### Example

```shell
jsac exec -o jumpscale -n echo -a msg:helloworld -r node -gid 55
Job:

: args: {msg: helloworld}
category: jumpscale
cmd: echo
gid: 55
guid: afced53b8ddf4d4eb6e9b0e84fd2dac9
id: 4106
jscriptid: 19
log: true
nid: 1
parent: null
queue: default
result: helloworld
resultcode: 0
roles: [node]
sessionid: 55_1_0_9949f946-3dcf-4682-9631-927adaba49e7
state: OK
timeStart: 1404930166
timeStop: 1404930166
timeout: 600
wait: true
```
