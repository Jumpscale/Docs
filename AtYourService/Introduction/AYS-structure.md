# At Your Service structure

- (1) Metadata Repos
 - Metadata repos contain all the metadata defining the life cycle of a service, from pre-installation to monitoring
 - An example is [ays_jumpscale7](https://github.com/jumpscale7/ays_jumpscale7), defining the full life cycle of the AYS JumpScale7 services
 - You can configure AtYourService to use one or more repos:
  - Edit the file ```/opt/jumpscale7/hrd/system/atyourservice.hrd```
  - Add new section for every metadata repo you want to add
    ```shell
        #here domain=jumpscale, change name for more domains
        metadata.jumpscale             =
            branch:'master',
            url:'https://github.com/jumpscale7/ays_jumpscale7',
        #add this domain
            metadata.openvcloud        =
            url:'https://git.aydo.com/0-complexity/openvcloud_ays',
```
 - AtYourService uses [git](http://git-scm.com) to manage its metadata
  - All metadata repos are cloned into ```/opt/code```
   - Repos from github are cloned into ```/opt/code/github```
   - Repos from other git repos are cloned into ```/opt/code/git/```
    - So ```https://github.com/jumpscale7/ays_jumpscale7``` is cloned into ```/opt/code/github/jumppscale/ays_jumpscale7```
  - Updating/cloning metadata repos:
   - Manually cloning individual repos is achieved with ```git pull```
   - Use ```ays mdupdate``` in order to update all existing repos and clone missing (not yet cloned) repos
 - You can configure a service by editing the recipe of the service, which is made of following files
  - **service.hrd** is the main metadata file which is valid for all service instances
  - **instance.hrd** is the metadata file relevant for 1 instance of a service
  - **actions_mgmgt.py** defines actions executed from the management location
  - **action_node.py** defines actions executed remotely on a node
  - **actions_tmpl.py** defines the "static" actions for the recipe itself, that do not require to first create a service instance in order to call them

- (2) Installation Directory
 -  For each locally and remotely installed service instance a sub directory under ```/opt/jumpscale7/hrd/apps``` will contain the configuration files, the recipe of the running service instance
 - The name of the sub directory reflects the name of the service and the name of the instance: ```{$service-name__$instance-name}```
 - For the AYS JumpScale services itself for example, as defined in the git clone ```/opt/code/github/jumpscale7/ays_jumpscale7```, it will be as below, where the name of each instance is ```main``` which is the default instance name when no other name was specified in the recipe:

 ```shell
  root@ovc2:~# ls /opt/jumpscale7/hrd/apps/
  agentcontroller__main         osis__main
  agentcontroller_client__main  osis_client__jsagent
  base__main                    osis_client__main
  grafana__main                 osis_eve__main
  grafana_client__main          portal__main
  gridportal__main              portal_client__main
  influxdb__main                portal_lib__main
  influxdb_client__main         redis__system
  jsagent__main                 singlenode_grid__main
  mailclient__main              singlenode_portal__main
  mongodb__main                 statsd-collector__main
  mongodb_client__main          statsd-master__main
  nginx__main                   web__main
```
