#Building your own docker image

We made this task very easy for you. You just need to get the [dockers](https://github.com/Jumpscale/dockers) repository and follow the build instructions below. Also you can customize your image and build it the same way as the examples in the repo.
### Pre-equirements
- Make sure you have the latest version of docker installed
- GNU make

#Building the base images
To start building the base images first clone and prepare the repository:

```bash
git clone https://github.com/Jumpscale/dockers.git
cd dockers
git submodule init
```
> Note: The `git submodule init` is only required once the first time you clone the repository. No need to rerun this command for the future builds.


```bash
cd ./images
ls -l
```
```raw
total 0
drwxr-xr-x 1 azmy azmy 54 Sep  8 15:59 agentcontroller2
drwxr-xr-x 1 azmy azmy 54 Sep  8 15:29 ubuntu15.04
drwxr-xr-x 1 azmy azmy 54 Sep  8 13:19 ubuntu15.10
```
We have 2 base images:
- ubuntu 15.04
- ubuntu 15.10

Each has the following pre-configured
- working SSH
- root password set to `js007`
- latest jumpscale7 (at the time of the build) pre-installed
- auto starts all installed `@ys` services
- system redis

We also have the `agentcontroller2` as an example of custom image that uses `ubuntu15.04` image to pre-install some services. If you need to build a custom image that pre-installs your apps and services you can use this one as a guide. Note that this image won't build unless `ubuntu15.04` was build already.

Now to build the base images do the following:
```bash
cd dockers/images/ubuntu15.04
make
```
Make will take care of everything and will take sometime, but when it's done you will have the `jumpscale/ubuntu15.04` image ready.

```bash
docker images
```
Will have this in its output
```raw
REPOSITORY                   TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
jumpscale/ubuntu             15.04               6cc68f352eb8        20 hours ago        630.4 MB
```