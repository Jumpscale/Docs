from JumpScale import j
import os
from os.path import expanduser

class MockREDIS(object):
    def mock(self):
        #j.system.fs.changeDir(expanduser('~'))
        bin = os.path.join(expanduser('~'),'redis')
        j.system.fs.createDir(bin)
        j.do.pullGitRepo(url='https://git.aydo.com/binary/redis.git', dest=bin, login=None, passwd=None, depth=1, ignorelocalchanges=False, reset=False, branch=None, revision=None)
        
        src = os.path.join(expanduser('~'),'redis/redis')
        dst = j.system.fs.joinPaths(j.dirs.baseDir, 'apps/redis')

        j.system.fs.createDir(dst)
        j.system.fs.symlink(src, dst, overwriteTarget=True)
        j.system.fs.changeDir('%s/apps/redis' % j.dirs.baseDir)
        j.system.process.execute('/opt/jumpscale7/apps/redis/redis-server' , dieOnNonZeroExitCode=True, outputToStdout=True)

if __name__ == '__main__':
    MockREDIS().mock()
