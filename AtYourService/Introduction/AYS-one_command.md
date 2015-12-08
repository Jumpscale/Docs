# One command to rule them all

We use only one command ```ays``` to control everything:
- Configure a service and all its dependencies (if any): ```ays init -n service-name```
- Install service: ```ays apply```
- Start a service: ```ays start -n service-name```
- Stop a service: ```ays stop -n service-name```
- Check status for all installed services: ```ays status```
- Check status for only local services (on this machine) ```ays status --local ```
- Update metadata (like Ubuntu's ```apt-get update```) ```ays mdupdate```
