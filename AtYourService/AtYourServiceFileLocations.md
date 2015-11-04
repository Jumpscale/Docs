## File Locations For Service Templates

```
/opt/code/github/jumpscale/ays_jumpscale7/singlenode_portal/
```

* service templates are organized in service domains and are stored in git.
* /opt/code/github/jumpscale/ays_jumpscale7 is a service domain called jumpscale7

```
/opt/jumpscale7/hrd/apps/$role!$instanceName/
/opt/jumpscale7/hrd/apps/$role!$instanceName/actions.py
/opt/jumpscale7/hrd/apps/$role!$instanceName/state.hrd
/opt/jumpscale7/hrd/apps/$role!$instanceName/instance.hrd
/opt/jumpscale7/hrd/apps/$role!$instanceName/instance_old.hrd
/opt/jumpscale7/hrd/apps/$role!$instanceName/template.hrd
/opt/jumpscale7/hrd/apps/$role!$instanceName/log.txt

```

* when a service gets installed the resulting files are put in this location
    - **instance.hrd** : contains all the details relevant to one instance
        - e.g. : instance parameters for configuring a service
    - **template.hrd**: contains details common to all instances of a service.
        - e.g. : domain of service
    - **action.py** : This is a copy of the action.py file from the service template. Service.hrd and instance.hrd values are available through the passed object's hrd.
        - e.g. : in instance.hrd there is a line : ```param.color = green``` and in action.py there is a line with ```setColor(serviceObj.hrd.get('param.color'))``` the result will be ```setColor('green')```  
    - **state.hrd** : this file is used to keep installation state of a service. In action.py you can define steps in your actions. During install if an action failed, the reinstallation will start from the last success step, and not do everything again.
    **Do not modify this file**
    - **log.txt** : simple log file about actions that has been taken with the service
* when re-installing a service whatever information already present in this folder will be used
* it can be useful to remove this file if you want to reset the service configuration state
  * 'service resetstate -n $serviceName -i $instanceName'' has the same result


```
/opt/jumpscale7/hrd/system/
```
there is a whoami.hrd, this hrd makes sure that the right credentials are used when doing a git pull
