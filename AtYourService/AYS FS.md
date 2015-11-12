## AYS FS - AtYourService FileSystem

AYS FS is a fuse file system that simplifies the distribution of files over the grids.

It's written in Go which make it really simple to deploy on bare metal machine and can be use to bootstrap environment, install JumpsScale and AYS Services.

### How it works
#### Metadata and binary files
AYS FS uses two kind of files to recreate a file system: 
- Metadata files
- Binary files

There is one metadata files by AYS templates or instance.
This list contains all the files required by an AYS.

The following is an excerpt of the metadata file of the ```jumpscale__base``` service.
```
/opt/jumpscale7/bin/jsnet|8a3e5e03a10ecc3601a1f14fbc371019|4857
/opt/jumpscale7/bin/jsnode|793384b5bde2901461606146adbed382|5088
/opt/jumpscale7/bin/jsportalclient|76f87551c60336da45c379f38625144b|1553
/opt/jumpscale7/bin/jsprocess_monitor|127546640e1f98c3d35bbd03153a1e17|248
/opt/jumpscale7/bin/jsprocess_startAllReset|e839ddaa3d391c9d099cb513d538c62b|184
/opt/jumpscale7/bin/jsprocess|397f026a662f1316421b78e8c6c5b5f7|4506

```

The format is   ```/$path/$name|$hash|$size```

The hash is an md5 hash of the content of the file. It's used to link the metadata with it's binary content. It also allow us to creates dedupe namespace where the binary content is never duplicated.

The binary content is stores in a directory structure with 3 levels.
First two level are the first and second character of the hash of the file and the last level contain the actual binary file named with the full md5 hash.
```
a
├── 0
│   ├── a001d62d00fbeb0f1ef4e77e5d8c5e3d
│   ├── a0237c980711ed468f39b5c178ccf875
│   ├── a03e021c3623542e16c47df9799ff8a5
│   ├── a043b3974df8701a8d3cf686690795f8
├── 1
│   ├── a12abc97671995529a05ae1fa73120c9
│   ├── a134ce45aa49528684f9bbc6c2e8042c
│   ├── a139377c7036f280449d8a6746501c18
│   ├── a13bc16af414cc4bdfb9d554c50842d9
...
```


### AYS FS workflow
When starting, AYS FS
- looks in its configuration file which stores can be used.
- looks for the AYS it needs to expose in the fuse and download the corresponding metadata files from a stores.
- Then as the user opens files, AYS FS will download the binary files and cache it locally.

In an OpenVCloud environment, it can have multiple layer of caching available.
To speed up files download, some 'Grid caches' can exists. These are used the same way as the stores, but they are populated by the AYS FS as it downloads files and located in the local network of the OVC nodes

AYS FS will always first look into its local cache for the binary files, if can't find them, it will look into 'grid caches' if any the files are still not available it will download it from a store.
