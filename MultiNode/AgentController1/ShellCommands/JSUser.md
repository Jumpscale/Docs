JSUser
======

The 'jsuser' command is a tool to manage users. It is possible to create
and delete users, change password and change group memberships.

Help
----

```shell
jsuser --help
usage: jsuser [-h] [-d DATA] [-ul USERLOGIN] [-up USERPASSWD] [-ud DOMAIN]
              [-gu GROUPUSER] [-gg GROUPGROUP] [-l LOGIN] [-p PASSWD]
              [-a ADDR]
              {add,set,delete,list,auth,addgroup,delgroup,passwd}

positional arguments:
  {add,set,delete,list,auth,addgroup,delgroup,passwd}
                        Command to perform

optional arguments:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  add user as
                        username:passwd:group1,group2:email1,email2:domain
  -l LOGIN, --login LOGIN
                        login for grid, if not specified defaults to root
  -p PASSWD, --passwd PASSWD
                        passwd for grid
  -a ADDR, --addr ADDR  ip addr of master, if not specified will be the one as
                        specified in local config

Authentication:
  -ul USERLOGIN, --userlogin USERLOGIN
                        username to do check,edit
  -up USERPASSWD, --userpasswd USERPASSWD
                        passwd for user to check,edit

List:
  -ud DOMAIN, --domain DOMAIN
                        domain for user to list

GroupManipulation:
  -gu GROUPUSER, --groupuser GROUPUSER
                        user
  -gg GROUPGROUP, --groupgroup GROUPGROUP
                        group to add or remove
```

Actions
=======

Add
---

Used to create a user

```shell
jsuser add
name: newuser
passwd: 
passwd (confirm): 
gid [55]: 
domain e.g. incubaid.com: jumpscale.org
do you want to define new groups. (y/n):y
comma separated list of groups: newgroup
comma separated list of emails: newuser@jumpscale.org
{
  "_ckey": "", 
  "_meta": [
    "system", 
    "user", 
    1
  ], 
  "active": true, 
  "authkey": "", 
  "description": "", 
  "domain": "jumpscale.org", 
  "emails": "newuser@jumpscale.org", 
  "gid": 55, 
  "groups": [
    "newgroup"
  ], 
  "guid": "55_newuser", 
  "id": "newuser", 
  "lastcheck": 1405237029, 
  "passwd": "098f6bcd4621d373cade4e832627b4f6", 
  "roles": []
```

Delete
------

Delets a user

```shell
jsuser delete -ul newuser
```

List
----

Lists the users on the grid

```shell
jsuser list

name                 domain                    groups
================================================================================ 
admin                incubaid.com              admin
newuser              jumpscale.org             newgroup
```

Auth
----

Commands allows you to check password from the cli

```shell
jsuser auth
user to check: admin
passwd for user to check: admin
passwdhash           21232f297a57a5a743894a0e4a801fc3
authkey              
authenticated        True
exists               True
groups               [u'admin']
```

Addgroup
--------

Command to add a user to a group

```shell
jsuser addgroup -gu admin -gg newgroup
add group:newgroup from admin
{
  "_ckey": "", 
  "_meta": [
    "system", 
    "user", 
    1
  ], 
  "active": true, 
  "authkey": "", 
  "description": "", 
  "domain": "incubaid.com", 
  "emails": "admin@codescalers.com", 
  "gid": 55, 
  "groups": [
    "admin", 
    "newgroup"
  ], 
  "guid": "55_admin", 
  "id": "admin", 
  "lastcheck": 1405237830, 
  "passwd": "21232f297a57a5a743894a0e4a801fc3", 
  "roles": []
}
```

Delgroup
--------

Delete a user from a group

```shell
jsuser delgroup -gu admin -gg newgroup
del group:newgroup from admin
{
  "_ckey": "", 
  "_meta": [
    "system", 
    "user", 
    1
  ], 
  "active": true, 
  "authkey": "", 
  "description": "", 
  "domain": "incubaid.com", 
  "emails": "admin@codescalers.com", 
  "gid": 55, 
  "groups": [
    "admin"
  ], 
  "guid": "55_admin", 
  "id": "admin", 
  "lastcheck": 1405237935, 
  "passwd": "21232f297a57a5a743894a0e4a801fc3", 
  "roles": []
}
```

Passwd
------

Change the userpassword password can be provided directly as md5sum from
the commandline or as plaintext. It can also be entered interactively.

```shell
jsuser passwd -ul admin -up admin

#or

jsuser passwd -ul admin -up 21232f297a57a5a743894a0e4a801fc3

#or

jsuser passwd -ul admin
passwd: 
passwd (confirm):
```
