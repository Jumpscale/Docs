## AtYourService Dependencies

## DEPRECATED

### Basics
dependencies are marked in the service template hrd as follows

```
dependencies.1                 =
    name:'ubuntukernel',
    domain:,
    instance:,

```

### more complex example where arguments are embedded

```
dependencies.1                 =
    args:'dep.args.redis',
    instance:'system',
    name:'redis',

dep.args.redis                 =
    param.disk:1,
    param.mem:100,
    param.passwd:'$(param.rootpasswd)',
    param.port:9999,
    param.unixsocket:0,

#next dependency will only be used when doing a build
dependencies.2               =
    instance:'main',
    name:'gcc',
    type:'build',


```

### Pre-filled hrd
When instanciating  a new service, it is also possible to pass an hrd file prefilled with the arguments. This is particuly usefull when you want to configure your service more deeply or when you have services that has lot of depencecies.

#### format
Pre-filled HRD should follow this format :
```
domaine.name.instance.argument = value
```
e.g. :
To set the value of ```param.disk``` of the ```redis``` service, one would do
```
jumpscale.redis.main.param.disk = 1
```
