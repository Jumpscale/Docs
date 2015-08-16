### How to install

- Currently, installation requires the contoml module which is still not part of base. 
- So we need to pip this module before we can continue with the installation. 
- This step will get dropped once `contoml` is integrated with `jumpscale` base

```bash
pip install --upgrade contoml

ays install -n agentcontroller2
ays install -n agentcontroller2_client
ays install -n agent2
```

#### Testing setup
Start a `jumpscale` shell

```python
client = j.clients.agentcontroller2.Client()
client.get_os_info(1, 1)
```

this should return something like
```python
{u'hostname': u'ea724b563ab8',
 u'os': u'linux',
 u'platform': u'ubuntu',
 u'platform_family': u'debian',
 u'platform_version': u'14.04',
 u'procs': 0,
 u'uptime': 1436087357,
 u'virtualization_role': u'',
 u'virtualization_system': u''}
```