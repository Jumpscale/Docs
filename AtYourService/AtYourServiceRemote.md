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

ays init -n node.local -i local --data 'jumpscale.install:False jumpscale.update:False node.tcp.addr:172.17.0.5


# Now we're ready to install the service on the defined node
# By defining the node as the parent of the singlenode_portal service,
# we're basically saying it will be installed on that node.
ays init -n singlenode_portal --parent '!local@node'
```


**Through a script**
```python
from JumpScale import j

# creation of a location, this is a container for nodes and it represent the
# datacenter
location = "Europe"
data = {}
data["instance.name"] = location
data["instance.description"] = "Our %s location." % location
location = j.atyourservice.new(name="location", instance=location.lower(), args=data)
location.init()

# creation of a sshkey service
data = {}
data['instance.key.priv'] = ''  # empty private key trigger auto generation
# notice here how we specifiy the relation between the location and the sshkey service,
# just add the 'parent=' parameter to the service creation and the sshkey will be a child service of the location.
keyInstance = j.atyourservice.new(name='sshkey', instance="mykey", args=data, parent=location)
keyInstance.init()
keyInstance.install()

# creation of a node inside the location
data = {}
data["instance.ip"] = "172.17.0.5"
data["instance.ssh.port"] = 22
# here we give the instance name of the sshkey service to use to connect to this node
# if the key is not yet present on the node, login/passwd will be use for first
# connection and to push the key in authorized_key file.
data['instance.sshkey'] = keyInstance.instance
data['instance.login'] = 'root'
data['instance.password'] = 'supersecret'
node = j.atyourservice.new(name='node.ssh', args=data, parent=location)
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
