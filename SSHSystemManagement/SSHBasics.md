
SSH Basic Connection Tool Using Paramiko (low level)
==========================

connect using an ssh agent
----

```
cl=j.remote.ssh.getSSHClientUsingSSHAgent(host='remote', username='root', port=22, timeout=10)

#to test connection

cl.execute("ls /")

Out[2]: 
(2,
 'bin\nboot\nbootstrap.py\ncdrom\ndev\netc\nhome\ninitrd.img\ninitrd.img.old\nlib\nlib64\nlost+found\nmedia\nmnt\nopt\nproc\nroot\nrun\nsbin\nsrv\nsys\ntmp\nusr\nvar\nvmlinuz\nvmlinuz.old\n\n',
 '')

```


connect using login/passwd
--------------------------

```
cl=j.remote.ssh.getSSHClient(password="apasswd", host='remote', username='root', port=22, timeout=10)
```

connect using local ssh private key
--------------------------

```
cl=j.remote.ssh.getSSHClientUsingKey(keypath="/home/despiegk/ssh2/id_rsa", host='remote', username='root', port=22, timeout=10)
```

connect using ssh-agent (RECOMMENDED)
--------------------------
```
cl=j.remote.ssh.getSSHClientUsingSSHAgent(host='remote', username='root', port=22, timeout=10)
```
the ssh-agent will know which agents to use & also remember passphrases of the keys so we don't have to provide them in code

