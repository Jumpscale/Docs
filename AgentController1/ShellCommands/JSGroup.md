JSGroup
=======

The 'jsgroup' command is a tool to manage groups. It is possible to
create delete and list groups.

Help
----

```shell
jsgroup --help
usage: jsgroup [-h] [-d DATA] [-p PASSWD] [-a ADDR] [-gl GROUP] [-gd DOMAIN]
               {add,delete,list}

positional arguments:
  {add,delete,list}     Command to perform

optional arguments:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  add group as groupname:domain
  -p PASSWD, --passwd PASSWD
                        superadmin passwd for grid
  -a ADDR, --addr ADDR  ip addr of master, if not specified will be the one as
                        specified in local config
  -gl GROUP, --group GROUP
                        groupname
  -gd DOMAIN, --domain DOMAIN
                        domain for group to list
```

Actions
=======

Add
---

```shell
jsgroup add -d level1:jumpscale.org
{
  "_ckey": "", 
  "_meta": [
    "system", 
    "group", 
    1
  ], 
  "active": true, 
  "description": "", 
  "domain": "jumpscale.org", 
  "gid": 55, 
  "guid": "55_level1", 
  "id": "level1", 
  "lastcheck": 1405238371, 
  "roles": [], 
  "users": []
}
```

Delete
------

```shell
jsgroup delete -gl newgroup
```

List
----

```
jsgroup list

name                 domain                    users
================================================================================ 
None                 incubaid.com              admin
admin                incubaid.com              admin
level1               jumpscale.org
```
