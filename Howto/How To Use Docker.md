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

## Use docker extension to start docker containers
Here you are an example script on how to use `JumpScale` docker extension to manage your
docker machines.

[do.py](https://github.com/Jumpscale/play7/blob/master/docker_jumpscale_development/do.py)

```python
from JumpScale import j


def _create_docker_machine(name, image='despiegk/mc'):
    ports = "8086:8086 8083:8083 28017:28017 27017:27017 5544:5544 82:82"
    vols = "/opt/jumpscale/var/influxdb:/var/mydocker/influxdb # /opt/jumpscale/var/mongodb:/var/mydocker/mongodb"
    j.tools.docker.destroy(name)
    j.tools.docker.create(
        name=name,
        ports=ports,
        vols=vols,
        volsro='',
        stdout=True,
        base=image,
        nameserver=['8.8.8.8'],
        replace=True,
        cpu=None,
        mem=0,
        jumpscale=True
    )


def docker_create_machine(name='master', reset=False, image='despiegk/mc'):
    containers = j.tools.docker.list()
    if name not in containers or reset:
        _create_docker_machine(name, image)

    return j.tools.docker.getSSH(name)


def install_portal(ssh):
    """
    install portal
    """

    ssh.run('ays install -n singlenode_portal')
    ssh.run('ays start')


###################################################################################
if __name__ == '__main__':
    name = 'master'
    ssh = docker_create_machine(name=name, reset=True)

    install_portal(ssh)

    info = j.tools.docker.inspect(name)

    port = info['NetworkSettings']['Ports']['22/tcp'][0]['HostPort']
    print "SSH port of docker is: %s" % port
```