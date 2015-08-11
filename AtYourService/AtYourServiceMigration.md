## How to convert JPackage to AtYourService template

AtYourService is a fork of JPackage so the change from a jpackage to a service should be quite straight forward.

1. **action.py**  

In action.py file, check that the value you get from the hrd have still the same name.
In @YS, the hrd data from service.hrd are prefix with 'service.' and the data from instance.hrd are prefix with 'instance.'  
So for example if in instance.hrd there is something like :
```
param.port=22
param.ip=123.234.1.3
```
In the action.py file, you have to get these values using :
```
$(instance.param.port)
$(instance.param.ip)
```

2. **service.hrd**

- It's a good practice to add a '**description**' item inside the service.hrd file. This info could be use to display information about this service through a portal for example.

- **category**  
    - In @YS you can specify a category for your service.  
    - a use case for these categories is the creation of a link between a 'node' service like [node.ssh](https://github.com/Jumpscale/ays_jumpscale7/tree/master/_ays/node.ssh) and another service that need to be executed inside this node.

## Example how to use from python

```python
# here we simply create a node.ssh service
# node.ssh has a category 'node' in its service.hrd
node = j.atyourservice.new(name='node.ssh',instance='node1')
node.init()
node.install()

# then we create a mongodb service and we want it to be installed inside the  
# node previously created. Do to that we use the 'comsune' method.
# consume take two arguments, first is the category of service we want to consume  
# the second is the instance name of a service that provide this category
mongodb = j.atyourservice.new(name='mongodb',instance='main')
mongodb.consume('node',node.instance)
mongodb.init()
mongodb.install()
```

If we look in the service.hrd file of the mongodb service, we can find
```
'producer.node = 'node1'
```
which means that mongodb cosume a service of the category 'node' and wich instance name is 'node1'
This is an exmaple of the flexibility @ys gives you to create complexes relations between your services.
