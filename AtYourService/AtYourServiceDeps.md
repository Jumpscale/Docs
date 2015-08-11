## AtYourService Dependencies


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

