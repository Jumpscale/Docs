First, you'll need to make sure the poral libs are made available. You can do that like this:
```
ln -s /opt/code/github/jumpscale/jumpscale_portal8/lib/portal /opt/jumpscale8/lib/JumpScale/
ln -s /opt/code/git/binary/web_python3/root/lib/* /opt/jumpscale8/lib/
mkdir -p /opt/jumpscale8/apps/portals/main
ln -s /opt/code/github/jumpscale/jumpscale_portal8/jslib /opt/jumpscale8/apps/portals/
ln -s /opt/code/github/jumpscale/jumpscale_portal8/apps/portalbase /opt/jumpscale8/apps/portals/

mkdir -p /opt/jumpscale8/apps/portal/main/base/home/.space
cp -rf  /opt/jumpscale8/apps/portals/jslib/old/images  /opt/jumpscale8/apps/portals/jslib/old/elfinder
cd /opt/jumpscale8/apps/portals/main  

```
Then, in a jsshell, do:
```

hrdstr = """                        
#param.osis.connection=@ASK default:main descr:'PORTAL: OSIS connection instance'
param.portal.rootpasswd = 'admin'

param.cfg.ipaddr = '127.0.0.1'
param.cfg.port= '82'
param.cfg.appdir = /opt/jumpscale8/apps/portals/portalbase
param.cfg.filesroot = /opt/jumpscale8/var/portal/files
param.cfg.secret = 'admin'
param.cfg.defaultspace = 'home'
param.cfg.admingroups = 'admin,'
param.cfg.authentication.method='' #Empty for minimal portal which doesn't authenticate
param.cfg.gitlab.connection='main'
param.cfg.force_oauth_instance=''

param.cfg.contentdirs = ''
"""
hrd = j.data.hrd.get(content=hrdstr)
j.application.instanceconfig = hrd
j.core.portal.getServer().start()
```



