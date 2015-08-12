How to configure a new service
------------------------------

- In order to create a service template called ```fancyPackage``` (Without going into much details) you've to do:
    - Publish service binary data
          - ofcourse only if you have binary data to use which you want to repackage yourselves
          - Initiate a local git repo anywhere in your file system called ```fancyPackage```.
          - Add the binary data files to this repo
          - Push this repo to e.g. [Remote Binary Repo/Aydo](http://git.aydo.com/org/binary)
    - Create service templates
          - create a directory under your ays metadata repo e.g. ```/opt/code/github/jumpscale/ays_jumpscale7/``` called ```fancyPackage```
          - Inside the service template directory, add 3 files *(actions.py, service.hrd, instance.hrd)*
          - Those metadata files draw the life cycle plan of the service from creation to monitoring.
          - Metadata will contain the URL for binary data repo for that service on [Remote Binary Repo/Aydo](http://git.aydo.com/org/binary)
          - In the next sections we'll explain in details how to configure and create a new service.


the 3 important files

- **actions.py**
     - contains ```Actions``` class with predefined functions that do certain actions
     - here're the steps involved in a service installation
          - [```prepare```, ```check_requirements```] actions are executed in order.
          - Then actual service files will be downloaded/installed
          - [```configure```, ```check_uptime_local```] will be executed in order.
              * ```check_uptime_local``` : Checks if process already running (from previous installation)
              * If process running try execute ```stop``` for graceful stop
              * execute  ```check_uptime_local``` to check if process still running
              * If process still running try execute ```halt``` for hard stop
          - execute ```start``` using the config files to start the application
          - execute ```check_uptime_local``` to check process is started
          - execute ```monitor_local``` to check local application is running & healthy
          - execute ```monitor_remote``` to check if remote application is running & healthy
- **service.hrd**
- **instance.hrd**

You can read more about the HRD format [here](HRD.md).