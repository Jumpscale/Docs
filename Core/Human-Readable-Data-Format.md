Human Readable Data
===================

About HRD
---------
* HRD is the configuration format in jumpscale.
* Used in AtYourService configuration.
* HRD is a more easily read and interpreted format for data, that is friendly to system engineers too.
* Can even be used as a template engine!
* It can be used to represent:
 * Configuration files
 * Database objects

* * * * *
Example Of An HRD File
----------------------

```shell

#!text
osis.elasticsearch.ip=localhost
osis.elasticsearch.port=9200
osis.db.type=filesystem
```

* * * * *
Usage As Template Engine
------------------------

**Getting application instance HRD's**

```python
hrd=j.application.getAppInstanceHRD(name, instance, domain='jumpscale')
#then e.g. use
j.application.config.applyOnDir
j.application.config.applyOnFile
```

**Getting system wide HRD's**

they are all mapped under j.application.config
you can e.g. use following 2 functions to apply your templates to dirs or files

```shell
j.application.config.applyOnDir
j.application.config.applyOnFile
```
to look at the HRD just go in ipshell & print the config

The templateing function will look for template params \$(hrdkey) and replace them

you can replace additional arguments e.g:

```python
j.application.config.applyOnDir(adir,additionalArgs={"whoami","kds"})
```

would replace \$(whoami) with kds additional to what found in hrd's