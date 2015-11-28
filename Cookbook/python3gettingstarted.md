# Python 3 GettingStarted

## goal 

- is to show how to get started as developer with most recent version of jumpscale and python 3.5


## how

- we will use docker & docker tools on mac to demonstrate this tutorial (with small changes this should work on windows too)


## pre-requisites

- install https://www.docker.com/docker-toolbox
- install git in terminal do ```brew install git```
- checkout jumpscale code to appropriate directory

```python
mkdir -p  ~/code/jumpscale

#checkout
cd ~/code/jumpscale
git clone git@github.com:Jumpscale/jumpscale_core7.git
cd jumpscale_core7/
git fetch
git checkout -b python3_unstable origin/python3_unstable
git pull origin python3_unstable

#checkout ays repo
cd ~/code/jumpscale
git clone git@github.com:Jumpscale/ays_jumpscale7.git
cd ays_jumpscale7/
git fetch
git checkout -b python3_unstable origin/python3_unstable
git pull origin python3_unstable


#get the playdirectory (has examples to play with)
cd ~/code/jumpscale
git clone git@github.com:Jumpscale/play7.git

```

## build your own environment



## other tools

- sourcetree on mac is a very good tool to manipulate your git repo's
- sublimte text is a good editor