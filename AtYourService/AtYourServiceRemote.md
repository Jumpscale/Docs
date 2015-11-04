### AtYourService remote execution

AtYourService allow you to create and manage a full environment.
In order to be able to contact the remote machines, you need to write the services that will handle these communications.

To have an idea of what can be created, lets have a look at a concrete example.

1. **Situation**
    - 1 datacenter located in Europe and US
    - 1 servers running in the datacenter
2. **Goal**
    - install mongodb on the server from remote location
3. **How to do it**
    - Through the AYS cmd
    - A simple script



Example of a remote node installation

**Through the cmdline**
```
# First, install the node service which will define everything you
# need to manage a remote node.

# Notice that we use "--data" to pass arguments directly to the ays
# instance to avoid being asked configuration questions during installation.

ays init -n node.local -i local --data 'jumpscale.install:False jumpscale.update:False node.tcp.addr:localhost'


# Now we're ready to install the service on the defined node
# By defining the node as the parent of the singlenode_portal service,
# we're basically saying it will be installed on that node.
ays init -n singlenode_portal --parent '!local@node'
```


**Through a script**
```python
from JumpScale import j

# creation of a node
data = {}
data['jumpscale.install'] = False
data['jumpscale.update'] = False
data['node.tcp.addr'] = "localhost"

node = j.atyourservice.new(name='node.local', args=data, parent=location)
node.init()
node.install()

# then we create a mongodb service and we want it to be installed inside the
# node previously created. Do to that we use the 'comsune' method.
# consume take two arguments, first is the category of service we want to consume
# the second is the instance name of a service that provide this category
# any service that consume another service with category node will be executed from inside this node.
data = {
    'instance.param.replicaset': 0,
    'instance.param.host': '127.0.0.1',
    'instance.param.port': 27017
}
mongo = j.atyourservice.new(name='mongodb', args=data, parent=node)
mongo.consume('node', 'main')
mongo.init()
mongo.install()
```

Have a look at the services template used in this example :
- [sshkey](https://github.com/Jumpscale/ays_jumpscale7/tree/master/_ays/sshkey)
- [location](https://github.com/Jumpscale/ays_jumpscale7/tree/master/_aggregattion/location)
- [node.ssh](https://github.com/Jumpscale/ays_jumpscale7/tree/master/_ays/node.ssh)
- [mongodb](https://github.com/Jumpscale/ays_jumpscale7/tree/master/_servers/mongodb)
