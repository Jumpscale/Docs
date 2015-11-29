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

## docker preparation

- prepare yourself a bigger docker environment
    - std docker is in too small docker env  

```bash
#remove your std vm used as docker host
docker-machine rm default

#create a new one based on virtualbox
docker-machine create --driver virtualbox --virtualbox-disk-size "60000" --virtualbox-cpu-count "2" --virtualbox-memory "4000" default

#or create one on remote ssh node
docker-machine rm ovh5
docker-machine create --engine-storage-driver btrfs --driver=generic --generic-ip-address=ovh5 --generic-ssh-key=id_rsa default

#put the docker env arguments in your os environment
eval $(docker-machine env default)

```

remark check if you have enough memory (here we are giving 4GB mem to the docker host)


## build your own environment

```bash
cd ~/code/jumpscale/play7/docker/compose_devel/
#will get the images as specified in the docker-compose.yml file
docker-compose  up

```

example docker compose file

```yaml
devel:
  image: jumpscale/ubuntu1510_python3
  ports:
   - "2022:22"
  volumes:
   - .:/code
   - /Users/Shared/code/github:/opt/code/github
  links:
   - redis
   - influxdb
   - mongo
influxdb:
  image: jumpscale/influxdb  
  ports:
   - "8083:8083"
   - "8086:8086"
   - "3000:3000"
mongo:
  image: jumpscale/mongo
  ports:
   - "27017:27017"
   - "28017:28017"
redis:
  image: gurpartap/redis
  ports:
   - "6379:6379"
```

### result
- this will install ubuntu 15.10 with python3 inside & jumpscale 7
- also influxdb, mongodb & redis will be installed & all accessible from the devel docker

### to connect
- check ```docker-machine ip default``` to find ip address of docker host
- e,g, foundip=192.168.99.100
- the main development machine is accessible over ssh on the foundip on port 2022
    - access ```ssh -A root@192.168.99.100 -p 2022 ``` login/passwd is root/gig1234

### influxdb
- statistics database
- std login/passwd root:root
- go to admin interface on http://192.168.99.100:8083/

### grafana
- very nice dashboard to visualize stats in influxdb
- is installed in same docker as influxdb
- see http://docs.grafana.org/
- is on port 3000  on http://192.168.99.100:3000/

### mongodb
- json database (very powerful)
- 27017 = db port
- 28017 = web stats port : http://192.168.99.100:28017/

### redis
- 



## other tools

- sourcetree on mac is a very good tool to manipulate your git repo's
- sublimte text is a good editor
- to look at your redis instance use: http://redisdesktop.com/
