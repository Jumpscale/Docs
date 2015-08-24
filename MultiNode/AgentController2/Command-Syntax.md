# Example Command
Commands are delivered to the `Agent` from the `Agent Controller` over long polling. Agent keeps polling the AC for jobs. Jobs are delivers as `json` objects as following

```json
 {
    "id": "<job-id>",
    "gid": <grid-id>,
    "nid": <node-id>,
    "name": "<command>",
    "args": {
        ...
    },
    "data": "<data-string>",
}
```

* id: Job ID. Chosen by the caller
* gid: Grid ID
* nid: Node ID
* args: Command specific arguments.
* data (optional): Data string, will be fed to the sub-process over `stdin`. So it actually can be anything including serialized json data.

# args
Arguments fine-tunes the process. The arguments are interpreted by the Agent itself to control the behavior of the sub-process, unlike `data` which is passed unprocessed to the sub-process itself.
Basic arguments support the following args:

* maxtime: How long the sub-process can run, 0 for (forever) or long running process
* max_restart: max times the process will be restarted if failed, if max_restart = 0 then no restart. If the process lived for more than 5 min before it failes the counter will be reset.
* domain: domain of jumpscript (to do categorization)
* name: name of jumpscript or cmd to execute (will give all a name)
* loglevels: list of log levels to process
* loglevels_db: list of log levels to be processed by DB logger (overrides the logger defaults)
* loglevels_ac: list of log levels to be processed by AC logger (overrides the logger defaults)
* recurring_period: 0 or 100
    seconds between recurring execute this cmd
    0 is default means not recurring, so only once
* stats_interval: 120 means we overrule the default for this process and only monitor this porcess every 120 seconds.
* queue: If queue is set, the command will wait on a job queue for serial execution. In other words no 2 processes with the same queue name will get executed on the same agent at the same. time

#Built in commands
* execute
* get_cpu_info
* get_disk_info
* get_mem_info
* get_nic_info
* get_os_info
* killall
* ping
* restart
* get_msgs (Not Implemented Yet)
* del_msgs (Not Implemented Yet)