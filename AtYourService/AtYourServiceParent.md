AYS Parent/Child relationship
-------------------------------

A service can be a parent for other services. It's a way of organizing your services and grouping them.

Child services have the same instance name as that of the parent.
```
ls -l /opt/jumpscale7/hrd/apps
drwxr-xr-x 2 root root 4096 Nov  1 08:23 influxdb_client!local
drwxr-xr-x 2 root root 4096 Nov  1 08:23 influxdb!local
drwxr-xr-x 2 root root 4096 Nov  1 08:23 mailclient!local
drwxr-xr-x 2 root root 4096 Nov  1 08:23 mongodb_client!local
drwxr-xr-x 2 root root 4096 Nov  1 08:58 mongodb!local
drwxr-xr-x 2 root root 4096 Nov  1 10:38 node!local
drwxr-xr-x 2 root root 4096 Nov  1 08:23 osis_client!local
drwxr-xr-x 2 root root 4096 Nov  1 08:59 osis!local
drwxr-xr-x 2 root root 4096 Nov  1 08:23 portal_lib!local
drwxr-xr-x 2 root root 4096 Nov  1 09:00 portal!local
drwxr-xr-x 2 root root 4096 Nov  1 08:59 redis!system
drwxr-xr-x 2 root root 4096 Nov  1 08:23 singlenode_portal!local
drwxr-xr-x 2 root root 4096 Nov  1 08:23 web!local

 |
 | - child1
     | action.py
     | service.hrd
 | - child2
     | action.py
     | service.hrd
 | action.py
 | service.hrd
 
```

A service is also identified by its parent, so two services with the same domain/name/instance can exits if they have different parents.

This is useful for grouping services of a certain location/node together. Then, performing any action is made easier.

#To create a nested child service:
```
# First, create the parent
# Note that the parent can be any service
ays install -n location -i europe --data 'instance.name:Europe'

# Now create a child service with its parent the created location service
ays install -n redis -i test --parent location!europe

# You can even create a child nested within the child that you just created by
ays install -n redis -i test --parent location!europe:redis!test
# Notice that you could have just specified the parent to be --parent redis!test because at that point you only have the one.

# Our current structure looks like this:
# location__europe
# |
# | - redis__test
#     | action.py
#     | service.hrd
#     | - redis__test
#          | action.py
#          | service.hrd
# | action.py
# | service.hrd


# To perform an action on location__europe/redis__test specifically without matching on location__europe/redis__test/redis__test, you'll have to use the '--immediate' argument. This implies that the parent is precisely the one specified.
ays start -n redis -i test --parent location!europe --immediate

```

