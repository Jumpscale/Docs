# How to export data in osis


##### Manually execute a jumpscript that does the trick for you.

```
cd /opt/code/github/jumpscale/jumpscale_core7/apps/agentcontroller/jumpscripts/core/backup
python export.py
```
- You can change the namespaces you want to export from inside the jumpscript file itself
- Result can be found at: /opt/jumpscale7/backup



##### using Jumpscale shell
```
osiscl = j.clients.osis.get()
osiscl.export(namespace, category, path)
```