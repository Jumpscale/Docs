Loading and working with actors
===============================

When calling j.core.portal.loadActorsInProcess(), then by default system
actors will be available under j.apps.system

```python
import JumpScale.portal

#make sure you are in the appropriate appserver dir
j.system.fs.changeDir("/opt/jumpscale7/apps/portal/main/")

#load the actors
j.core.portal.loadActorsInProcess()
```

If you want your app actors to be loaded under
`j.apps.<your_app_name>.<your_actor_name>`, you will have to
explicitly load them, cause they are lazy-loaded

```python
j.apps.actorsloader.getActor('cloud', 'cloudbroker')

machines = j.apps.cloud.cloudbroker.machineList()
```
