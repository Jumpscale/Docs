### How to install


```bash
# make sure you have a redis instance installed.

ays install -n agentcontroller2
ays install -n agentcontroller2_client
ays install -n agent2
```

#### Testing setup
Start a `jumpscale` shell

```python
client = j.clients.ac.getByInstance('main')
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