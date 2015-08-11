Starting application and configuration
======================================

JumpScale enables you to specify custom directories for example for
logging configuration. You should specify these folders before starting
your application ('j.application.start') and before any module loading.

Default directories are configured during the start of the application.

Application start
-----------------

`j.application.start(name=None, basedir='$jumpscaledir',
appdir='.')`

-   Name
    -   If set will change appname
-   basedir
    -   Will set basedir see below
-   appdir
    -   Will set the appdir (see below). If '.' is specified, the
        current directory will be used.

j.dirs
------

-   j.dirs.baseDir
    -   Base directory where all other directories depend on
    -   Defaults to `$jumpscaledir`
    -   If only this directory is set, all other directories will be
        relative to this folder.
-   j.dirs.appDir
    -   Directory used for application specific purpose
    -   Defaults to the current working directoring (set at application
        start)
-   j.dirs.libDir
    -   Internal directory where JumpScale is installed
-   j.dirs.extensionsDir
    -   Currently not used
-   j.dirs.logDir
    -   Used for logging
-   j.dirs.binDir
    -   Directory where binaries are stored
-   j.dirs.packageDir
    -   Used for JumpScale package manager
-   j.dirs.cfgDir
    -   Used for global configuration
-   j.dirs.pidDir
    -   Used for storing pid files
-   j.dirs.homeDir
-   j.dirs.tmpDir
    -   Used for storing temperary files
-   j.dirs.cmdbDir
    -   Used for configuration database (deprecated)
-   j.dirs.varDir
    -   Equivalent to the linux var directory. Typical location where
        the log service pid and db is stored.

there are more directories configured under this module.
