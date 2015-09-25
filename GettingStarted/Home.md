# GettingStarted

## js

```js``` is the main jumpscale shell.

to execute a jumpscale cmd in the shell do
```
js 'j.do.loadSSHAgent()'
```
everything behind hs will be evalled in the jumpscale shell session 

## to install jumpscale apps use ays (at your service)

- To install mongodb we do:
```
ays mdupdate #Update metadata locally
ays install -n mongodb #Install
```
required questions will be asked for

- to list ays packages do

```
ays list
```

## ssh key management

- ssh is used a lot in the jumpscale framework
    - its used to do remote system management
    - but also to checkout code from e.g. github
- if you don't have ssh keys yet
    - do ```js 'j.do.loadSSHAgent(createkeys=True,keyname="despiegk")' ofcourse keyname can be anything, specify a meaningfull name
    - this will check if you have ```$homedir/.ssh/id_rsa``` or ```$homedir/.ssh/$keyname``` key available, if yes will be loaded, if no a new one will be created
    - if a new one PLEASE use a passphrase you only know
    - the public key will be under ```$homedir/.ssh/id_rsa.pub``` or ```$homedir/.ssh/$keyname``` this is the key you will have to give to e.g. github
    - if you are under a 'sudo -s' session your $homedir will still be your original login session
- to load your sshkey & ssh-agent do
    -```js 'j.do.loadSSHAgent()'```
    - this will start sshagent if required & load all the keys it can find in ```$homedir/.ssh```
    - you only need to do this once on a system, from now on the .bashrc file will make sure that in every new terminal you have access to your keys
    - remark: if this is the first time then your current session does not have access to sshkeys yet, go into a new terminal to see the results & start using ssh
- if you want to read more about key mgmt see
    - [tips & tricks about ssh keys & agents (e.g. how to create your keys)](SSHSystemManagement/SSHKeysAgent.md)

## Some handy shortcuts

```
#configure git & make sure ssh-agent is configured & ready to go
jscode init

#pull git repo with jumpscale docs, feel free to contribute
j.do.installer.installJSDocs()


```

## further

* [IPythonTricks](IPythonTricks.md)
* [JSCode](JSCode.md)
* [Configuration Files](Configuration Files.md)
