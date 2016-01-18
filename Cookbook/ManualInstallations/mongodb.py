from JumpScale import j


class MockMONGO(object):
    def mock(self):

         j.system.fs.createDir('/opt/mongodb/bin')
         j.do.pullGitRepo(url = 'https://git.aydo.com/binary/influxdb_bin.git')

         src='/opt/code/git/binary/mongodb/bin'
         dst='/opt/mongodb/bin'
         j.system.fs.symlink(src, dst, overwriteTarget=True)

         j.system.fs.createDir("/opt/jumpscale7/var/mongodb/")
         j.system.fs.changeDir('/opt/mongodb/bin')

         j.system.process.execute('rm -f /opt/jumpscale7/var/mongodb/main/mongod.lock;export LC_ALL=C;/opt/mongodb/bin/mongod --dbpath  /opt/jumpscale7/var/mongodb/ --smallfiles --rest --httpinterface' , dieOnNonZeroExitCode=True, outputToStdout=True) 

if __name__ == '__main__':
    MockMONGO().mock()
