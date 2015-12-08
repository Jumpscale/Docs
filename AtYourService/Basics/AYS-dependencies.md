# Dependencies

Usage of dependencies
```
dependencies.global            = mongodb,influxdb
dependencies.node              = portal_lib,influxdb_client,mongodb_client
```

- Dependencies are specified with a role name (not based on AYS name)
- Global & node dependencies
  - Global dependencies are dependencies between AYS instance on level not specific to 1 node e.g. portal needs MongoDB
  - Node dependencies are specific for 1 node, they tell us which local(=node) AYS instance need to be locally installed
- If the local & global dependencies are properly defined then there is no need to specify the consumption flag
  - AYS will lookup a service with specified role on global or node level, if only 1 is found the the consumption will configured automatically
