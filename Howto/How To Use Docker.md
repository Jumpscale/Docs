# How To Use Docker
Make sure you have the latest `jumpscale` installed

## Install docker
```bash
ays install -n docker
```

## Use docker
We already have a base docker image ready to use `despiegk/mc`. You also can use this [docker file](https://github.com/Jumpscale/jumpscale_core7/blob/master/docker/Dockerfile) to build your image.

```bash
docker pull despiegk/mc

#standard /tmp/docker/tmp will be mapped & /code to be same in docker
#std port 9022 will be mapped to ssh (if only 1 docker)
#-j will also install jumpscale (make sure you have it installed locally)
jsdocker new -n test -j

#more detailed example
#sjdocker new -n kds --ports "22:9022 7766:9766" --vols "/mydata:/mydata" --cpu 100

#to login
ssh localhost -p 9022

#now you can install whatever apps using jumpscale
(test)# apt-get update
```

Now you can use `@ys` to install jumpscale packages.

```bash
ays install -n redis
```

## Commit your changes.
When you setup your apps, and you are happy with your pre-set docker container, you can commit
your changes to later use or distribution by doing the following:

```bash
#first get a docker running e.g. 
jsdocker new -n test -j

#1- SSH to running container
#2- Install apps you want on that instance

#On host, show which docker running
docker ps

#now we can push docker image to repo
docker commit test myimage
# If you have dockerhub account, you can push your image to dockerhub

#to run the newly created docker image do the following
docker run -d -p 9022:22 -v /opt/code/:/opt/code myimage /sbin/my_init
```