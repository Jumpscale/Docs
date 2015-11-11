How to configure a new service
------------------------------

- In order to create a service template called `fancyPackage` (Without going into much details) you've to do:
    - Publish service binary data
        - ofcourse only if you have binary data to use which you want to repackage yourselves
        - Initiate a local git repo anywhere in your file system called `fancyPackage`.
        - Add the binary data files to this repo
        - Push this repo to e.g. [Remote Binary Repo/Aydo](http://git.aydo.com/org/binary)
    - Create service templates
        - create a directory under your ays metadata repo e.g. ```/opt/code/github/jumpscale/ays_jumpscale7/``` called ```fancyPackage```
        - Inside the service template directory, add 3 files *(actions.py, service.hrd, instance.hrd)*
        - Those metadata files draw the life cycle plan of the service from creation to monitoring.
        - Metadata will contain the URL for binary data repo for that service on [Remote Binary Repo/Aydo](http://git.aydo.com/org/binary)
    
In the next sections we'll explain in details how to configure and create a new service.


A service has 2 HRD files and up to 3 python files. HRD files are where configuration is kept, python file describe the actions possible of the services.
- **service.hrd** : instance specific configuration
- **instance.hrd**: common configuration for all instance of this service
- **actions_tmpl.py** : contains the actions possible for a templates directly without the need to create an instance of the service to call them. Can be seen as "static" method of a service.
- **actions_mgmt.py** : contains actions executed from the management location.
- **actions_node.py** : contains actions executed remotely on a node.
     
    - contains ```Actions``` class with predefined functions that do certain actions
    - here're the steps involved in a service installation
      - At management location
        - ```init``` : instantiate service, check dependencies and install them if possible
        - ```prepare``` 
        - ```configure```
        - ```check_up``` : Checks if process already running (from previous installation)
          * If process running try execute ```stop``` for graceful stop
          * execute  ```check_up``` to check if process still running
          * If process still running try execute ```halt``` for hard stop
      - ```start``` using the config files to start the application
      - ```check_up``` to check process is started
      - ```monitor``` to check local application is running & healthy
    - If the service is installed on a remote node, after management actions. method from action_node.py are executed on the remote node.
      - ```configure```
        - ```check_up``` : Checks if process already running (from previous installation)
          * If process running try execute ```stop``` for graceful stop
          * execute  ```check_up``` to check if process still running
          * If process still running try execute ```halt``` for hard stop
      - ```start``` using the config files to start the application
      - ```check_up``` to check process is started
      - ```monitor``` to check local application is running & healthy

You can read more about the HRD format [here](HRD.md).