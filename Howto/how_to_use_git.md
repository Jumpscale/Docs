## How To Use Git Automated
We have a handy tool `jscode` to make working with source code easier. 

```bash
jscode --help
usage: jscode [-h] [-n NAME] [--url URL] [-m MESSAGE] [-b BRANCH]
              [-a ACCOUNTS] [-u] [-f] [-d] [-o]
              {get,commit,push,update,status,list,init}

positional arguments:
  {get,commit,push,update,status,list,init}
                        Command to perform

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  name or partial name of repo, can also be comma
                        separated, if not specified then will ask, if '*' then
                        all.
  --url URL             url
  -m MESSAGE, --message MESSAGE
                        commit message
  -b BRANCH, --branch BRANCH
                        branch
  -a ACCOUNTS, --accounts ACCOUNTS
                        comma separated list of accounts, if not specified
                        then will ask, if '*' then all.
  -u, --update          update merge before doing push or commit
  -f, --force           auto answer yes on every question
  -d, --deletechanges   will delete all changes when doing update
  -o, --onlychanges     will only do an action where modified files are found

```

###jscode init
```bash
jscode init
```

- this will check if there is ~/.ssh/id_rsa
- if not keys will be generated
- your git configuration will be done (email, username)
- your bashrc will be adjusted to make sure your ssh-agent gets loaded properly

> If you entered a passphrase for your key, you will get asked for it when you do a relogin

###jscode status and jscode list
`jscode status` Show all the code repos status (if it has local modifications). 
`jscode list` shows the remote `URLs`

###jscode commit
Commit changes in a repo (or all repos) optionally commit to branch using the `-b` option.

###jscode update
Pulls all new remote changes to local clone.

###jscode push
Pushes all local commit to remote.

## How To Use Git Manual Way

### Generate Keys

- generate your own ssh keys
    - look at https://help.github.com/articles/generating-ssh-keys/ has a good explanation
- best to use a passphrase !!! you will only have to use the passphrase when you load it in your ssh-add

### Manually Load Keys

ssh-agent is a very nice tool which allows you to use your keys without having to type the passphrase all the time.

if you manually want to use ssh-agent to load your keys
Look at next session which is the better way !

```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

- ```~/.ssh/id_rsa``` is your private key you have generated, never expose this key, its only for you
- ```~/.ssh/id_rsa.pub``` is your public key, this one needs to be used to get access to other machine or service (like git in this case)

### How to get ssh-agent to work without having to do this manually

add this to end of $homedir/.bashrc
```
ssh-add -l &>/dev/null
if [ "$?" == 2 ]; then
  test -r ~/.ssh-agent && \
    eval "$(<~/.ssh-agent)" >/dev/null

  ssh-add -l &>/dev/null
  if [ "$?" == 2 ]; then
    (umask 066; ssh-agent > ~/.ssh-agent)
    eval "$(<~/.ssh-agent)" >/dev/null
    ssh-add
  fi
fi
```

this will make sure your ssh-agent get's loaded and keys are in mem for maximum 10h


### set your git private details

```
git config --global user.email "your_email@example.com"
git config --global user.name "Billy Everyteen"
```

### How to manually checkout a git repo

```
mkdir -p ~/code
cd ~/code/
git clone git@github.com:Jumpscale/jumpscale_core7.git
```

the nice thing is you will not have to use login/passwd when doing code mgmt as long as you have your keys filled in.



