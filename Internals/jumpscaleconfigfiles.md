# Jumpscale Config Files

Are in HRD format
In this section we list the known config files (there should be no others).
All other configurations are done in AYS hrd files

all hrd config files are stored in /opt/jumpscale7/hrd/system

## atyourservice.hrd

```bash
#here domain=jumpscale, change name for more domains
metadata.jumpscale =
    url:'https://github.com/Jumpscale/ays_jumpscale7',
    branch:'python3_unstable',

```

## system.hrd

```bash
paths.base=/opt/jumpscale7
paths.bin=$(paths.base)/bin
paths.code=/opt/code
paths.lib=$(paths.base)/lib

paths.python.lib.js=$(paths.lib)/JumpScale
paths.python.lib.ext=$(paths.base)/libext
paths.app=$(paths.base)/apps
paths.var=$(paths.base)/var
paths.log=$(paths.var)/log
paths.pid=$(paths.var)/pid

paths.cfg=$(paths.base)/cfg
paths.hrd=$(paths.base)/hrd

system.logging = 1
system.sandbox = 0
```
can all be left empty, or file does not have to exist


## system redis

```
redis.addr = 
redis.port = 
redis.passwd = 
```


## logging

```


```

