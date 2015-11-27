First, you'll need to make sure the poral libs are made available. You can do that like this:
```
from JumpScale import j

class MockPortal():
    def mock():

        j.system.fs.symlink('/opt/code/github/jumpscale/jumpscale_portal/lib/portal', '/opt/jumpscale7/lib/JumpScale/portal', overwriteTarget=True)

        for item in j.system.fs.listFilesAndDirsInDir('/opt/code/git/binary/web_python3/root/lib/'):
            if j.system.fs.isLink(item):
                continue
            if j.system.fs.isDir(item):
                try:
                    j.system.fs.copyDirTree(item, '/opt/jumpscale7/lib/', keepsymlinks=True, overwriteFiles=False)
                except Exception as e:
                    print(e)
            else:
                j.system.fs.copyFile(item, '/opt/jumpscale7/lib/')

        for item in j.system.fs.listFilesAndDirsInDir('/opt/code/git/binary/web_python3/root/jslib/'):
            if j.system.fs.isLink(item):
                continue
            if j.system.fs.isDir(item):
                j.system.fs.copyDirTree(item, '/opt/jumpscale7/apps/portals/jslib', keepsymlinks=True, overwriteFiles=True)
            else:
                j.system.fs.copyFile(item, '/opt/jumpscale7/apps/portals/jslib/')

        for src, dest in [('apps/portalbase', 'apps/portals/portalbase/')]:
            source = j.system.fs.joinPaths(j.dirs.codeDir, 'github', 'jumpscale', 'jumpscale_portal', src)
            target = j.system.fs.joinPaths(j.dirs.baseDir, dest)
            j.system.fs.symlink(source, target, overwriteTarget=True)


if __name__ == '__main__':
    MockPortal.mock()


```

Then, in a jsshell, do:
```
hrdstr = """
#param.osis.connection=@ASK default:main descr:'PORTAL: OSIS connection instance'
param.portal.rootpasswd = 'admin'

param.cfg.ipaddr = '127.0.0.1'
param.cfg.port= '82'
param.cfg.appdir = /opt/jumpscale7/apps/portals/portalbase
param.cfg.filesroot = /opt/jumpscale7/var/portal/files
param.cfg.secret = 'admin'
param.cfg.defaultspace = 'home'
param.cfg.admingroups = 'admin,'
param.cfg.authentication.method=''
param.cfg.gitlab.connection='main'
param.cfg.force_oauth_instance=''

param.cfg.contentdirs = ''
"""
hrd = j.core.hrd.get(content=hrdstr)
import JumpScale.portal
j.application.instanceconfig = hrd
j.core.portal.getServer().start()
```



Now, to connect to the portal, in a jsshell:
```
 cl = j.clients.portal.get(port=82, secret='admin')
```
