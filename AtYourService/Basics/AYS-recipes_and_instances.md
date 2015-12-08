# Recipes and instances

*AYS Recipe*
- Defines the full life cycle from pre-installation, over installation, to upgrades and monitoring of a service, all described in the above mentioned recipe files:
    - service.hrd
    - instance.hrd
    - action*.py
- In a recipe we describe
    - Parameters relevant for a service instance
    - How to start/stop the instance
    - How to monitor the instance
    - How to install the binary files for the instance
    - How to configure the instance
    - How to get stats from the instance
    - How to export/import the data


*Instances*

Example: Running several instances of MongoDB on the same machine on different ports.

```shell
#the following will init the MongoDB recipe as an instance
ays init -n MongoDB # Use default instance name (main)
ays init -n MongoDB -i mongo2 #instance name is (mongo2)
```
