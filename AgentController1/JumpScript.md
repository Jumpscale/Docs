Jumpscripts
===========

A Jumpscript is a python script that can be execute on remote nodes.

Location
--------

Jumpscripts are located under the AgentController at
'/opt/jumpscaledir/apps/agentcontroller/jumpscripts'

Syntax
------

Each Jumpscript corresponds to one python module and should implement
one method called 'action'. This action can be paramterized.

```python
from JumpScale import j

descr = """
This jumpscript echos back (test)
"""

name = "echo"
category = "test"
organization = "jumpscale"
author = "kristof@incubaid.com"
license = "bsd"
version = "1.0"
async = False
queue = ''
period = 0
roles = []
log=False


def action(msg):
    print msg
    return msg
```

### Attributes

-   'name': Name of the Jumpscript
-   'category': Category of the Jumpscript
-   'organization': Organization of the Jumpscript
-   'author': E-Mail address of author of the Jumpscript
-   'license': License the Jumpscript can be destributed with
-   'version': Version of the Jumpscript
-   'async': Wheter to execute this Jumpscript in the processmanager or
    on one of the workers
-   'log': When set true this job will always be recorded in osis. If
    false it will only be recorded when it fails.
-   'queue': When queue is specified the Jumpscript will be executed on
    the specified worker queue regardless of the async flag
-   'period': Interval the Jumpscript will be automaticly executed at.
    Jumpscript with interval should not have arguments. A period can be
    defined as an number in seconds or in [cron
    format](http://www.nncron.ru/help/EN/working/cron-format.htm).
-   'roles': Roles of the node this Jumpscript can be executed on. This
    is used for Jumpscripts that have a period and also acts as a filter
    of which Jumpscripts are loaded on each node.

