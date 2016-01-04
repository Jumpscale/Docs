First, you'll need to make sure the poral libs are made available. You can do that like this:
```
ln -s /opt/code/github/jumpscale/jumpscale_portal8/lib/portal /usr/local/lib/python3.5/dist-packages/JumpScale/
mkdir -p /opt/jumpscale8/apps/portals/main
ln -s /opt/code/github/jumpscale/jumpscale_portal8/jslib /opt/jumpscale8/apps/portals/
ln -s /opt/code/github/jumpscale/jumpscale_portal8/apps/portalbase /opt/jumpscale8/apps/portals/

mkdir -p /opt/jumpscale8/apps/portals/main/base/home/.space
cp -rf  /opt/jumpscale8/apps/portals/jslib/old/images  /opt/jumpscale8/apps/portals/jslib/old/elfinder
cd /opt/jumpscale8/apps/portals/main  

```
Then, create a file.py script, with :
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



