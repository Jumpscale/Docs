# Instance keys

Each At Your Service instance has a unique key.

Key in format $domain|$name!$instance@role ($version)

Different format examples
+ $domain|$name!$instance
+ $name
+ !$instance
+ $name!$instance
+ @role

Version is added with ()
+ e.g. node.ssh (1.0), where "node.ssh" is the name of the service, which in this case contains a "." where "node" is the role of the service and "ssh" the name of the instance

## AYS instances can be found using this key format

e.g.
```shell
#find 1 service instance with role MongoDB and then start (if not started yet), if more than 1 then this will fail
ays start -n @mongodb

#find all service instances with role node and print their status
ays status -n @node

#find a service instance which has instance name ovh4
ays status -n !ovh4
```

If more than 1 instance is found then there will be an error
