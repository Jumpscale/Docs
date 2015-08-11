
SSH Remote System Tools
=======================

These are a set of tools inspired on
j.system.fs ...
but they work remotely over ssh.

There is some small overlap with cuisine.

connect
-------
```
sys=j.remote.system.connect(ip, login='', password='', timeout=120.0, port=22)  
#if password=="" then will try to use the ssh-agent or predefined keys
```

sys.fs
------
```
sys.fs.copyDirTree             sys.fs.fileGetContents         sys.fs.removeFile
sys.fs.copyDirTreeLocalRemote  sys.fs.isDir                   sys.fs.uploadFile
sys.fs.copyFile                sys.fs.isEmptyDir              sys.fs.writeFile
sys.fs.createDir               sys.fs.isFile                  
sys.fs.exists                  sys.fs.moveFile
```

sys.portforward
---------------

very cool tools to remote portforward over ssh from out of python
```
sys.portforward.cancelForwardRemotePort
sys.portforward.forwardLocalPort
sys.portforward.forwardRemotePort
```

```
sys.portforward.forwardLocalPort(localPort, remoteHost, remotePort, inThread=False)
    Set up a forward tunnel across an SSH server

    @param localPort: local port to forward
    @param remoteHost: remote host to forward to
    @param remotePort: remote port to forward to
    @param inThread: should we run the forward in a separate thread
```

```
sys.portforward.forwardRemotePort(self, serverPort, remoteHost, remotePort, serverHost='', inThread=False)

    Set up a reverse forwarding tunnel across an SSH server

    @param serverPort: port on server to forward (0 to let server assign port)
    @param remoteHost: remote host to forward to
    @param remotePort: remote port to forward to
    @param serverHost: host on the server to bind to
    @param inThread: should we run the forward in a separate thread

    @return:            Port number used on ther server
    @rtype:             int
```

sys.process
-----------

only 2 commands for now

```
returncode,stdout,stderr=sys.process.execute(command, dieOnNonZeroExitCode=False, outputToStdout=True, loglevel=5, timeout=None)
```

```
sys.process.killProcess(pid)
```