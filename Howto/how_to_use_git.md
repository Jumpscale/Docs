## How To Use Git

### Generate Keys

- generate your own ssh keys
    - look at https://help.github.com/articles/generating-ssh-keys/ has a good explanation
- best to use a passphrase !!! you will only have to use the passphrase when you load it in your ssh-add

### Make sure you use those keys

```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

- ```~/.ssh/id_rsa``` is your private key you have generated, never expose this key, its only for you
- ```~/.ssh/id_rsa.pub``` is your public key, this one needs to be used to get access to other machine or service (like git in this case)

### How to get ssh-agent to work without having to do this manually


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

