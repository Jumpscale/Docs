## service.hrd Process Section

this is how you can define processes & how they will be run on a local or remote system

```
process.1=
    cmd:'/opt/mongodb/bin/mongod',
    args:'--dbpath $(system.paths.var)/mongodb/$(service.instance)/ --smallfiles --rest --httpinterface',
    prio:5,
    cwd:'/opt/mongodb/bin',
    timeout_start:60,
    timeout_stop:10,
    ports:27017;28017,
    startupmanager:tmux,
    filterstr:'bin/mongod'

env.procces.1 =
    LC_ALL:C,
```

### process.1

The number `1` here is the order of the process if multiple processes are defined they have to have a unique order.

| Key | Type | Description |
|-----|------|-------------|
|cmd  | string| Commands to execute |
|args | string | Arguments to command |
|prio | int | Priority when all process are started from low to high |
|cwd  | string | Current working directory for the process |
|timeout_start| int | Timeout in seconds to mark the process as failed if not running yet |
|timeout_stop| int | Timeout in seconds to forcekill process if not stopped yet |
|ports| list of int| Semi column seperate list of tcp ports the process should listen on |
|startupmanager| sting | Tmux|
|filterstr| string| grep like string to identify the started process |

* Note: If ports is defined it is used to check if the process is started or stopped

### env.process.1

Environment variables for process `1`
