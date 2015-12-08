# Service roles

Each service has a role

If the role is not specified in the 'service.hrd' under parameter 'role' then the role will be auto filled from the first part of name, e.g. if the AYS service name is "node.ssh" the role will become node

Roles are used to define categories of AYS recipes e.g. AYS recipes which define a node & how to execute commands on a node, another example of a role is e.g. ns

## Init redis local or remote (example)

local

```
ays init -n redis -i --data 'param.name:system param.port:7766 param.disk:0  param.mem:100 param.ip:127.0.0.1 param.unixsocket:0 param.passwd:'
```

remote

```
ays init -n node.ssh -i ovh4 --data "ip:94.13.18.89 ssh.port:22"

ays init -n redis -i system --parent '!ovh4' --data 'param.name:system param.port:7766 param.disk:0  param.mem:100 param.ip:127.0.0.1 param.unixsocket:0 param.passwd:'

```

Notice how we use as key !ovh4 this means any ays with instance name ovh4 will be used (only if found 1)
more complete way to specify would have been 'node.ssh!ovh4' or '!ovh4$node' #means instance ovh4 from role node

Remark: install will only happen after 'ays apply'
