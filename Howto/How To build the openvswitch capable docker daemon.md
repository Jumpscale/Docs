# How to build a dockerdaemon with openvswitch support

First, set up a buildenvironment for docker as described on the [docker docs](http://docs.docker.com/opensource/project/set-up-dev-env/). Build a docker as described to initialize all dependencies and name it `dockerdev`.

Clone the jumpscale version of docker/libnetwork and check out the ovs branch:
```
git clone git@github.com:Jumpscale/libnetwork.git
cd libnetwork
git checkout ovs
```

Now start the docker to build docker with the jumpscale libnetwork repository mounted on the default dependencylocation (replace `<docker repository location>` and `<libnetwork repository location>` with the appropriate absolute paths):
```
docker run --privileged --cap-add NET_ADMIN --rm -ti -v <docker repository location>:/go/src/github.com/docker/docker -v <libnetwork repository location>:/go/src/github.com/docker/docker/vendor/src/github.com/docker/libnetwork dockerdev /bin/bash

hack/make.sh
```

The `--cap-add NET_ADMIN` option is only needed if you want to be able to test the openvswitch code from within the build docker.

The docker binary with openvswitch support is now available at `<docker repository location>/bundles/latest/binary/docker`