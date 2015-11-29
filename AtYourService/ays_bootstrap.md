# AYS Bootstrap


## mount a connection to the master cache of ays

- this works over http or ssh

how to mount it over sshfs
```
mkdir -p /mnt/ays/master1
sshfs ays@94.23.38.89:/ays/master /mnt/ays/master1
```

## if you use a local network cache

```
mkdir -p /mnt/ays/cachelan
sshfs ays@192.168.1.4:/mnt/ays/cache /mnt/ays/cachelan
```
## bootstrap jumpscale

### ubuntu 15.10 64 bit

- install / use a ubuntu 15.10 64 bit OS
- execute following

```
mkdir -p /mnt/ays/master1
curl ... ays readonly key & put for root user (no passphrase)
sshfs ays@94.23.38.89:/ays/master /mnt/ays/master1
rsync -r ays@94.23.38.89:/ays/pre/ubuntu1510/ /etc/ays/local/
rsync -r ays@94.23.38.89:/ays/bin/ /usr/local/bin/
@todo how to put the aysfs in upstart?
```

##TODO
- golang creates auto: /mnt/ays/cachelocal & /mnt/ays/cachelan
- how to define which caches to use
    - check if you can find aysmaster1(2...) as hostname & do tcp port test on port 443
        - if tcp port test succeeds 
        - do a https test to download predefined ping file
        - if all ok the nuse these as http master
        - url is https://$aysmaster/aysmaster/...
    - check /mnt/ays/master or /mnt/ays/master1 or /mnt/ays/master2 exists
        - use those as masters  
- how to define which caches to use
    - check if you can find ayscache1(2...) as hostname & do tcp port test on port 9990
        - if tcp port test succeeds use these as http cache
    - check /mnt/ays/cachelan or /mnt/ays/cachelan1 or /mnt/ays/cachelan2 exists
        - use those as caches
- as local cache use /mnt/ays/cachelocal (ONLY USE IF DIR EXISTS !!!)
