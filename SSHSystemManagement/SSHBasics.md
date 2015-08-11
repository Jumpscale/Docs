
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

ssh agent tips
--------------

```
#start the ssh agent in background
eval "$(ssh-agent -s)"

#add your private ssh key(s) you require
ssh-add /home/despiegk/ssh2/id_rsa

#list agent keys
ssh-add -l

#kill my own agents started as above
ssh-agent -k

```

just add all the keys you require & the sshagent will remember them for you

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

ssh daemon tips
===============

generate keys
--------------

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

authorize remote key
--------------------

bash way
```
#copy your pub key to remote server authorized keys (add at end of file)
scp root@remoteserver.com:/home/despiegk/ssh2/id_rsa.pub /tmp/mykey.pub
ssh root@remoteserver.com cat /tmp/mykey.pub >> /root/.ssh/authorized_keys
```

this will allow me from my local server to login as root on the remote machine

jumpscale way
```
@todo
```

varia
-----

```
#restart
/etc/init.d/ssh restart

#kill all ssh-agents (is dirty)
killall ssh-agent

```

secure your sshd config
-----------------------
```
#create recovery user (if needed)
adduser recovery

#make sure user is in sudo group
usermod -a -G sudo recovery

#sed -i -e '/texttofind/ s/texttoreplace/newvalue/' /path/to/file
sed -i -e '/.*PermitRootLogin.*/ s/.*/PermitRootLogin without-password/' /etc/ssh/sshd_config
sed -i -e '/.*UsePAM.*/ s/.*/UsePAM no/' /etc/ssh/sshd_config
sed -i -e '/.*Protocol.*/ s/.*/Protocol 2/' /etc/ssh/sshd_config

#only allow root & recovery user (make sure it exists)
sed -i -e '/.*AllowUsers.*/d' /etc/ssh/sshd_config
echo 'AllowUsers root' >> /etc/ssh/sshd_config
echo 'AllowUsers recovery' >> /etc/ssh/sshd_config

/etc/init.d/ssh restart

```

allow root to login
-------------------
dangerous do not do this, use sudo -s from normal user account
```
sed -i -e '/.*PermitRootLogin.*/ s/.*/PermitRootLogin yes/' /etc/ssh/sshd_config
/etc/init.d/ssh restart
```


tip: how to only allow root to login? (or other user)
----------------


