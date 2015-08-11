## Quick Start

### Requirements

The JumpScale portal requires the JumpScale framework to be installed.
So if you didn't do so [install JumpScale](../Core/Install.md).


### Install OSIS service

```
ays install -n osis -i test --data 'param.osis.key: param.osis.connection.mongodb:main param.osis.connection.influxdb:main param.osis.superadmin.passwd:rooter'

#Where param.osis.connection.mongodb is the installed mongodb client's instance
#and param.osis.connection.influxdb is the installed influxdb client's instance

```



### Install OSIS client

```
ays install -n osis_client --data 'param.osis.client.addr:127.0.0.1 param.osis.client.login:root param.osis.client.passwd:rooter'
```

### Control your OSIS service

Start your OSIS with `ays start -n osis`  
Stop your OSIS with `ays stop -n osis`

