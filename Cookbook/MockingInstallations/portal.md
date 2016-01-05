First, you'll need to make sure the poral libs are made available. You can do that like this:
```
ln -s /opt/code/github/jumpscale/jumpscale_portal8/lib/portal /usr/local/lib/python3.5/dist-packages/JumpScale/
ln -s /opt/code/github/jumpscale/jumpscale_portal8/lib/portal /opt/jumpscale8/lib/JumpScale/
```
Make sure your redis reflects these new additions to JS libs by flushing your redis and deleting `/opt/jumpscale8/bin/metadata.db` if it exists

```
mkdir -p /opt/jumpscale8/apps/portals/main
ln -s /opt/code/github/jumpscale/jumpscale_portal8/jslib /opt/jumpscale8/apps/portals/
ln -s /opt/code/github/jumpscale/jumpscale_portal8/apps/portalbase /opt/jumpscale8/apps/portals/


mkdir -p /opt/jumpscale8/apps/portals/main/base/home/.space
cp -rf  /opt/jumpscale8/apps/portals/jslib/old/images  /opt/jumpscale8/apps/portals/jslib/old/elfinder
```
* Create an admin user
```
jsuser add -d admin:admin:admin::
```
* To get GridPortal

```
ln -s /opt/code/github/jumpscale/jumpscale_portal8/apps/gridportal/base/* /opt/jumpscale8/apps/portals/main/base/


```
Then, under /opt/jumpscale8/apps/portals/main/ create a file.py script:
```
from JumpScale import j

hrdstr = """                        
param.mongoengine.connection=host:localhost, port:27017
param.portal.rootpasswd = 'admin'

param.cfg.ipaddr = '127.0.0.1'
param.cfg.port= '82'
param.cfg.appdir = /opt/jumpscale8/apps/portals/portalbase
param.cfg.filesroot = /opt/jumpscale8/var/portal/files
param.cfg.defaultspace = 'home'
param.cfg.admingroups = 'admin,'
param.cfg.authentication.method='me' #Empty for minimal portal which doesn't authenticate
param.cfg.gitlab.connection='main'
param.cfg.force_oauth_instance=''

param.cfg.contentdirs = ''
"""


hrd = j.data.hrd.get(content=hrdstr)
import JumpScale.portal
j.application.instanceconfig = hrd
j.core.portal.getServer().start()
                                  
```

