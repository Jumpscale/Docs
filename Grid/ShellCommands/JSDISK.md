jsdisk command
==============

when new system do an init first, this is done to find all new disks. On
the disk there will be a disk.hrd which has relevant info about the
disk. This is done to make sure we can always find the disk back even
when put on wrong location or in wrong server.

List only works after a succesfull init was done.

```shell
usage: jsdisk [-h] {init,list}

positional arguments:
  {init,list}  Command to perform

optional arguments:
  -h, --help   show this help message and exit
```
