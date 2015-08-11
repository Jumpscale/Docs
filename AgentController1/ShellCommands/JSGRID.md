JSGrid
======

```shell
usage: jsgrid [-h] [--force] [--debug] [--from FFROM] [--to TO] [-nid NID]
              [--roles ROLES]

              {reconfigure,healthcheck,purgeall,purgelogs,purgejobs,purgeecos,restartprocessmgrs,reloadjumpscripts,resetlocks}

positional arguments:
  {reconfigure,healthcheck,purgeall,purgelogs,purgejobs,purgeecos,restartprocessmgrs,reloadjumpscripts,resetlocks}
                        Command to perform

optional arguments:
  -h, --help            show this help message and exit
  --force               dont ask yes, do immediate
  --debug               will stop on errors and show all relevant info
  --from FFROM          used with purgelogs, ex: --from=-2h, --from=-2d (note
                        the = sign)
  --to TO               used with purgelogs, ex: --to=-1h, --to=-1d (note the
                        = sign)
  -nid NID, --nodeid NID
                        Used with healtcheck
  --roles ROLES         Used with setroles or deleterole. ex: -roles=node,
                        computenode.kvm(note the = sign). List is comma
                        seperated
```

Healthcheck
-----------

```shell
jsgrid healthcheck
```

The healthchecker checks the health of ElasticSearch of the grid then
iterates over all the nodes in the grid. For each node, it checks Redis,
Workers and Disks health.

-   Redis: that each port is running and its memory usage
-   Workers: that each worker hasn't reached its timeout. (default's
    timeout is 2m, io's is 2h, hypervisor's is 10m)
-   Disks: That all avaialbe disks have more than 10% of free space.

Purgall, Purgelogs, purgejobs and purgeecos
-------------------------------------------

These commands are used to clean up logs of logs, jobs, ecos
respectively. The purgall cleans up all for all dates

```shell
jsgrid purgelogs [--from=-3d --to=-2h]
#OR
jsgrid purgejobs
#OR
jsgrid purgeecos
```

Note: "to" defaults to four hours ago (-4h) if nothing specified
(exception:purgeall removes all till now)

restartprocessmgrs / reloadjumpscripts
--------------------------------------

```shell
jsgrid restartprocessmgrs
```

this will make sure all processmanager restart themselves so load new
jumpscripts

reloadjumpscripts: will only reload the jumpscripts (not the cmds for
processmanager itself)

resetlocks
----------

remove all locks for e.g. jpackages, usefull to troubleshoot a locked
jpackage install
