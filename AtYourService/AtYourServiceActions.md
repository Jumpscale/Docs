## AYS Actions

* Manages the life-cycle of your AYS
* you need to implement one or more methods (actions) on your atyourservice actions.py file

### Example:

 ```python
class ActionsBase():
    """
    implement methods of this class to change behaviour of lifecycle management of service
    """


    def init_pre(self,serviceObj):
        """
        gets executed before init happens of this ays
        use this method to manipulate the arguments which are given or already part of ays instance
        this is done as first action on an ays, even at central location 

        ## example how to use

        # call parent, to make sure std init_post is executed 
        ActionsBase.init_pre(self,serviceObj)
        if serviceObj.name.startswith("node"):
            serviceObj.hrd.set("something","data") #can of course come from everywhere
        """

    def init_post(self,serviceObj):
        """
        gets executed after init happens of all ays recipe's
        use this method to manipulate the hrd's as they are applied (inited) after init

        default we register the service to the nameservice

        if nameserver has not been consumed then will check if there is one nameserver already deployed (init) and use that one
        this action can ofcourse also be overruled to do a custom registration

        the name used for registration is

            $instance.$firstpartaysname.$ns.domain
            - $instance is name instance
            - $firstpartyaysname is the name of the ays before first . e.g node.ssh becomes 'node'
            - $ns.domain is the specified domain in the nameserver service

        ## example how to use
        # call parent, to make sure std init_post is executed 
        ActionsBase.init_post(self,serviceObj)
        serviceObj.hrd.set("something","data") #can ofcourse come from everywhere

        """


    def prepare(self,serviceObj):
        """
        this gets executed before the files are downloaded & installed on approprate spots
        this gets done remotely
        typically used to prepare a system e.g. make sure appropriate updates or packages installed
        the next step will copy files from the recipe's to the destination locations on the target (if binary git repo's used)
        """
        return True


    def configure(self,serviceObj):
        """
        this gets executed after the files are installed
        this step is used to do configuration steps to the platform
        after this step the system will try to start the service if anything needs to be started
        
        @return if you return "r" then system will restart after configure, otherwise return True if ok. False if not.

        """
        return True

    def configureLocal(self,serviceObj):
        """
        this gets executed just before configure and only if we work in remote mode e.g. over ssh
        """
        return True

    def start(self,serviceObj):
        """
        start happens because of info from main.hrd file but we can overrule this
        make sure to also call ActionBase.start(serviceObj) in your implementation otherwise the default behaviour will not happen

        only use when you want to overrule

        """
        return True

    def stop(self, serviceObj):
        """
        if you want a gracefull shutdown implement this method
        a uptime check will be done afterwards (local)
        return True if stop was ok, if not this step will have failed & halt will be executed.
        """
        return True

    def halt(self,serviceObj):
        """
        hard kill the app, std a linux kill is used, you can use this method to do something next to the std behaviour
        """
        return True

    def build(self,serviceObj):
        """
        build instructions for the service
        as part of this action you should copy the builded files to binary repository
        it will be up to user to push the binary repository (do not do this as part of this action)

        example location for a binary build would be

        /opt/code/git/binary/mongodb/mongodb

        the build action should be called from the ays template (not from the ays instance)

        you can then do std install to get the binaries on the right location

        """
        return True

    def check_up_local(self, serviceObj, wait=True):
        """
        do checks to see if process(es) is (are) running.
        this happens on system where process is
        """
        return True

    def check_down_local(self,serviceObj):
        """
        do checks to see if process(es) are all down
        this happens on system where process is
        return True when down
        """
        return True

    def check_requirements(self,serviceObj):
        """
        do checks if requirements are met to install this app
        e.g. can we connect to database, is this the right platform, ...
        """
        return True

    def monitor_local(self,serviceObj):
        """
        do checks to see if all is ok locally to do with this service
        this happens on system where process is
        """
        return True

    def monitor_remote(self,serviceObj):
        """
        do checks to see if all is ok from remote to do with this service
        this happens on system from which we install or monitor (unless if defined otherwise in hrd)
        """
        return True

    def cleanup(self,serviceObj):
        """
        regular cleanup of env e.g. remove logfiles, ...
        is just to keep the system healthy
        """
        return True

    def data_export(self,serviceObj):
        """
        export data of app to a central location (configured in hrd under whatever chosen params)
        return the location where to restore from (so that the restore action knows how to restore)
        we remember in $name.export the backed up events (epoch,$id,$state,$location)  $state is OK or ERROR
        """
        return False

    def data_import(self,id,serviceObj):
        """
        import data of app to local location
        if specifies which retore to do, id corresponds with line item in the $name.export file
        """
        return False

    def uninstall(self,serviceObj):
        """
        uninstall the apps, remove relevant files
        """
        return False

    def removedata(self,serviceObj):
        """
        remove all data from the app (called when doing a reset)
        """
        return False

    def test(self,serviceObj):
        """
        test the service on appropriate behaviour
        """
        pass

    def execute(self,serviceObj, cmd):
        """
        execute is not relevant for each type of service
        for e.g. a node.ms1 service it would mean remote some shell command on that machine
        for e.g. postgresql it would mean execute a sql query
        """
        return False        

```
