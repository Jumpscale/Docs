# osis2

* osis2 is a serious update to osis and supports both mongodb, as well as sqldatabases via [SQLALCHEMY](http://www.sqlalchemy.org)
* osis2 uses the powerful [Python-Eve](http://www.python-eve.org/) framework 
* Currently osis2 works besides osis side by side, in master branch

## Structure of osis2

```
basepath -> /opt/jumpscale7/apps/osis2/
     |
     |__ app -> code for launching the app and generating models
     |__ models
     |__osis -> Contains models for osis2
     |    |
     |    |__ mongo -> mongodb models here
     |    |     |__ $namespacename/model.spec  (spec file)                                    
     |    |
     |    |__sql    -> sql models here
     |         |__ $sqlnamespacename/model.spec  (spec file)                                    
     |
     |__ hooks -> define hooks (pre-create, pre-update, ..)
                  hooks can be globally or per object
                  put your own business logic at this level
```
## Installing osis2

```
#SERVER
ays install -n osis2    
#CLIENT
ays install -n osis2_client
```
the ays install will launch osis as a tmux screen
to investigate do 'tmux a' and look  for osis2_main screen

to play with osis client change/use
- /opt/jumpscale7/apps/osis2/osis2play.py

to see web go to
- http://localhost:5545/


## Docs

* osis2 uses [Swagger.io](http://swagger.io/) to generate docs for us.
* you can see them at `http://<serverip>:5545/models/$namespace/docs`
* You can see a generated swagger spec json for the models definitions at  `http://<serverip>:5545/models/$namespace/docs.json`

example namespaces 
* system
* testsystem
* testsqlnamespace
* sqlnamespace

see dir structure higher defined where the namespaces are 


## Using the client
Below are some examples and you can read more in [osis2 TESTS](https://github.com/jumpscale7/jumpscale_core7/blob/master/apps/osis2/tests/osis_test.py)
```python
In [1]: cl = j.clients.osis2.get()  // main instance, otherwise : j.clients.osis2.get(instance='myinst') 
In [2]: cl.
cl.sqlnamespace  cl.system
In [2]: cl.system.
cl.system.alert       cl.system.grid        cl.system.jumpscript  cl.system.process
cl.system.audit       cl.system.group       cl.system.machine     cl.system.test
cl.system.disk        cl.system.heartbeat   cl.system.nic         cl.system.user
cl.system.eco         cl.system.info        cl.system.node        cl.system.vdisk
In [2]: cl.system.user.
cl.system.user.delete         cl.system.user.new            cl.system.user.set
cl.system.user.get            cl.system.user.partialupdate  cl.system.user.update
cl.system.user.list           cl.system.user.search
In [2]: cl.system.user.list()
Out[2]: [u'1_admin']
In [3]: user = cl.system.user.get('0_admin')

In [4]: user
Out[4]: <user id 0_admin>

# UPDATE
In [7]: cl.system.user.update(user)
Out[7]:
{u'_created': u'Thu, 01 Jan 1970 00:00:00 GMT',
 u'_etag': u'eb9fca3becc768241e5d3f0e6014822a4456866b',
 u'_links': {u'self': {u'href': u'/user/0_admin', u'title': u'User'}},
 u'_status': u'OK',
 u'_updated': u'Mon, 15 Jun 2015 15:08:31 GMT',
 u'guid': u'0_admin'}

# INSERT
In [8]: cl.system.user.new()
In [9]: cl.name = 'ali'
In [10]: cl.system.user.set(user)
Out[11]:  
{u'_created': u'Mon, 27 Jul 2015 13:08:53 GMT',
 u'_links': {u'self': {u'href': u'user/28f62c0d-73b5-4628-931d-ad3d215c3f45',
   u'title': u'User'}},
 u'_status': u'OK',
 u'_updated': u'Mon, 27 Jul 2015 13:08:53 GMT',
 u'guid': u'28f62c0d-73b5-4628-931d-ad3d215c3f45'}

# DELETE
In [12]: cl.system.user.delete('28f62c0d-73b5-4628-931d-ad3d215c3f45')

# COUNT
In [12]: cl.system.user.count() # All users
Out[13]: 2
In [14]: cl.system.user.count(query={'id':'admin'})
Out[15]: 1

# Filtering
  ## For mongo namespaces we just use mongodb search syntax
In [16]: cl.system.user.count(query={'id':'admin'})
In [17]: 1
In [18]: cl.system.user.search({'id':'admin'})
In [19]: ['admin']
In [20]: cl.system.user.search({'gid':{'$gt':9}}) # search for users with gid > 9
Out[20]: [<user id admin>]
   ## For SQL namespaces we just use SqlAlchemy expressions (any, similar, like, in)
In [20]: cl.system.user.count(query={'id':'like("admin%")'})
In [21]: 1
In [22]: cl.system.user.search({'id':'like("admin%")'})
In [23]:  [<user id admin>]
```

## Filtering results
* Filtering results can be found in 2 contexts:
  * count(query={})
  * search(query={})
* query format differs from MONGO namespace to SQL namespace
  * For mongo namespaces we use [Mongodb Query format](http://docs.mongodb.org/manual/reference/method/db.collection.find/)
  * For SQL namespaces we use [SQLAlchemy Expressions](http://eve-sqlalchemy.readthedocs.org/en/stable/tutorial.html#sqlalchemy-expressions)
  * For more examples, check the section above.

```
MONGO namespaces search                                                                                             
***********************                                                                                             
- Same search format found at:                                                                                      
  http://docs.mongodb.org/manual/reference/method/db.collection.find/                                               

- Examples:                                                                                                         
    - Search for records with name=ali:                                                                             
            client.mymongonamespace.user.search({'name':'ali'})                                                     
    - Search for users with age > 20                                                                                
            client.mymongonamespace.user.search({'age':{'$gt':20}})                                                 

SQL namespace search                                                                                                
*******************                                                                                                 
Same search format found at:                                                                                        
http://eve-sqlalchemy.readthedocs.org/en/stable/tutorial.html#sqlalchemy-expressions                                

Examples:                                                                                                           
----------                                                                                                          
    - Search for records with name starts with ali                                                                  
            client.mysaqlnamespace.user.search(.search({'name':'like("ali%")'})) 
```

## How to add a new namespace

* for mongo namespaces, create a directory under  /opt/jumpscale7/apps/osis2/models/osis/mongo/myNewNameSpace
* For sql namespaces, create a directory under  /opt/jumpscale7/apps/osis2/models/osis/sql/myNewNameSpace
* The directory name determines the namespace (name)
* Inside the directory put your models.spec file

## For sql namespaces, can I add python modules defining Sqlalchemy models directly?
* Yes absolutely, under ```/opt/jumpscale7/apps/osis2/models/osis/sql/myNewNameSpace``` add your files
* Example
``` python
from app.sqlalchemy.common import CommonColumns, typemap
import uuid
from sqlalchemy import (
    Column,
    String,
    Boolean,
    Integer,
    ForeignKey,
    DateTime)

class audit(CommonColumns):
    __tablename__ = 'audit'
    guid = Column(String(36), primary_key=True)

    id = Column(typemap['int'])
    user = Column(typemap['str'])
    result = Column(typemap['str'])
    call = Column(typemap['str'])
    statuscode = Column(typemap['str'])
    args = Column(typemap['str'])
    kwargs = Column(typemap['str'])
    timestamp = Column(typemap['str'])

```

## Hooks
* Hooks are powerful mechanism that allows you to control data insertion/update/delete
* 2 Types of Hooks
  * **Per name space hooks**
    * Run before any CRUD operation on all models in a name space
    * defined in /opt/jumpscale7/apps/osis2/models/$namespace/__init__.py
  * **per model hooks**
    * Run before any CRUD operation on certain model
    * You can override behaviors defined in (per name space) hooks
  * Types of hooks
    * Example

``` python
 from .helpers import osis2helpers

 def pre_create(items):
     pass

 def post_create(items):
     pass

 def pre_replace(item, original):
      pass

 def post_replace(item, original):
      pass

 def pre_update(updates, original):
       pass

 def post_update(updates, original):
       pass

 def pre_delete(item):
       pass

 def post_delete(item):
       pass

 def get(response):
       pass
```

## osis2 Tests

* osis2 comes with unit tests in```/opt/code/github/jumpscale7/jumpscale_core7/apps/osis2/tests```
* osis2 tests do tests on MONGO/SQL namespaces
* To run the tests use the command ```python osis2_test.py```

