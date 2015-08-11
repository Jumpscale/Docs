A service can be a parent for other services. It's a way of organizing your services and grouping them.

Child services are located inside the directory of the parent.
```
parent
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

To create a nested child service:
```
# First, create the parent
# Note that the parent can be any service
ays install -n location -i europe --data 'instance.name:Europe'

# Now create a child service with its parent the created location service
ays install -n redis -i test --parent jumpscale__location__europe

# You can even create a child nested within the child that you just created by
ays install -n redis -i test --parent jumpscale__location__europe:jumpscale__redis__test
# Notice that you could have just specified the parent to be --parent jumpscale__redis__test because at that point you only have the one.

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
ays start -n redis -i test --parent jumpscale__location__europe --immediate



