## File Locations For Service Templates

```
/opt/code/github/jumpscale/ays_jumpscale7/singlenode_portal/
```

* service templates are organized in service domains and are stored in git.
* /opt/code/github/jumpscale/ays_jumpscale7 is a service domain called jumpscale7

```
/opt/jumpscale7/hrd/apps/$role!$instanceName/
/opt/jumpscale7/hrd/apps/$role!$instanceName/service.hrd
/opt/jumpscale7/hrd/apps/$role!$instanceName/actions.py
/opt/jumpscale7/hrd/apps/$role!$instanceName/state.json
/opt/jumpscale7/hrd/apps/$role!$instanceName/log.txt
```

* when a service gets installed the resulting files are put in this location
    - **service.hrd** : it's the result of the merging of service.hrd and instance.hrd
        - all metadata from service.hrd are prefixed with 'service.' in service.hrd
        - all metadata from instance.hrd are prefixed with 'instance.' in service.hrd
    - **action.py** : This is a copy of the action.py file from the service template where special variable like $(varname) has been replaced with their value from service.hrd
        - e.g. : in service.hrd there is a ligne : ```instance.color = green``` and in action.py there is a ligne with ```setColor($(instance.color))``` the resul will be ```setColor('green')```  
    - **state.json** : this file is used to keep installation state of a service. In action.py you can define steps in your actions. During install if an action failed, the reinstallation will start from the last success step, and not do everything again.
    **do not modify this file**
    - **log.txt** : simple log file about actions that has been taken with the service
* when re-installing a service whatever information already present in this folder will be used
* it can be useful to remove this file if you want to reset the service configuration state
  * 'service resetstate -n $serviceName -i $instanceName'' has the same result


```
/opt/jumpscale7/hrd/system/
```
there is a whoami.hrd, this hrd makes sure that the right credentials are used when doing a git pull
