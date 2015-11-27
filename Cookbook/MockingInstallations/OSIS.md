Mimics behavior of the OSIS ays

```
from JumpScale import j

class MockOSIS():
    def mock():

        for src, dest in [('apps/osis/logic', 'apps/osis/logic'), ('apps/osis/tests', 'apps/osis/tests')]:
            j.system.fs.createDir(j.system.fs.joinPaths(j.dirs.baseDir, 'apps/osis'))
            source = j.system.fs.joinPaths(j.dirs.codeDir, 'github', 'jumpscale', 'jumpscale_core7', src)
            target = j.system.fs.joinPaths(j.dirs.baseDir, dest)
            j.system.fs.symlink(source, target, overwriteTarget=True)

        j.system.fs.changeDir('%s/apps/osis' % j.dirs.baseDir)
        j.core.osis.startDaemon(path="", overwriteHRD=False, overwriteImplementation=False, key="", port=5544, superadminpasswd='rooter', dbconnections={'mongodb':'main'}, hrd='')


        #j.system.process.execute('cd %s/apps/osis; jspython osisServerStart.py' % j.dirs.baseDir, dieOnNonZeroExitCode=True, outputToStdout=True)
        
if __name__ == '__main__':
    MockOSIS.mock()
```


To connect to this server, in a jsshell do:
```
from JumpScale.grid.osis.OSISFactory import OSISClientFactory

of = OSISClientFactory()
client = of.get()
client.listNamespaces()
client.listNamespaceCategories('system')

```
