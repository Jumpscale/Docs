
## Available SSH enabled SAL's

@todo improve
@put each SAL in separate doc & in SUMMARY.md

* OpenWRT
 * Network
 * DNS
 * DHCP
 * FTP
* Linux (Ubuntu)
 * Network
 * NFS
 * Disk manager
 * Nginx
 * SSH
 * UFW
 * AOE

### OpenWRT

```python
#getting manager.
wrt = j.ssh.openwrt.get(con)
```

The `wrt` manager has interface to work with the various parts

### Network

All network related properties and functions are grouped under `wrt.network` 
* configure uci based network configuration of openwrt, all over ssh
 * wrt = j.ssh.openwrt.get(sshconnection)
 * wrt.network.<method>
* methods on SAL
 * nics, list of all available nics in the form [(dev, mac), ...]
 * interfaces, list of all configured virtual interfaces (as defined in open wrt UCI network)
 * addInterface(name), add new interface section
 * removeInterface(interface), remove interface section
 * find(nic), find all interfaces bind to the given nic name (basically finds sections with ifname==nic
 * commit(), apply changes and restart networking

#### Examples

To list all `nics` (physically attached devices)

```python
wrt.network.nics
[('br-lan', '52:54:00:3d:59:01'),
 ('eth0', '52:54:00:3d:59:01'),
 ('lo', '00:00:00:00:00:00')]
```

To list all `interfaces` (logical devices)

```python
wrt.network.interfaces
```
Interfaces allows you to configure the network device `nic` and each single interface is associated with a physical device or another interface. 

To add a new interface

```python
inf = wrt.network.addInterface('test')
inf.ifname = 'eth0'
inf.proto = 'static'
inf.ipaddr = '1.2.3.4'
inf.netmask = '255.255.255.0'

wrt.network.commit()
```

Note changes to network configuration won't take effect unless a call to `commit()` is made.
Also make sure that your changes will not drop your ssh connection, otherwise you might not be able to reach the `OpenWRT` machine anymore.

### DNS

* configure dnsmasq, all over ssh
* limited support now e.g. A records
* work with factory class
 * wrt.dns.<method>()
* methods on dns SAL
 * records, dict with all A records in form {name: [ip, ...], ...}
 * erase(), removes all A records
 * addArecord(name, ip) add a new A record to DNS
 * removeArecord(name, ip=None) removes A record for name and IP. if ip is None, removes all A records for that name
 * commit(), apply changes and restart dnsmasq

#### Examples

```python
wrt.dns.records
{}

wrt.dns.addARecord('test', '1.2.3.4')
wrt.dns.commit()
```

```bash
ping test
PING test (1.2.3.4): 56 data bytes
64 bytes from 1.2.3.4: seq=0 ttl=64 time=0.083 ms
64 bytes from 1.2.3.4: seq=1 ttl=64 time=0.088 ms
^C
```

```python
wrt.dnt.records
{'test': ['1.2.3.4']}

wrt.dns.removeARecord('test')
wrt.dns.commit()
```

### DHCP

* configure dhcp server, all over ssh
* limited support now e.g. boot to pxe
* work with factory class
 * wrt = j.ssh.openwrt.get(sshconnection) 
 * wrt.dhcp.<method>
* methods on SAL
 * hosts, list of all static hosts.
 * erase(), removes all static hosts
 * addHost(name, mac, ip), add static host with name, mac and IP
 * removeHost(name), removes static host with name
 * pxe, configuration for pxe boot
 * pxe.filename,
 * pxe.serveraddress,
 * pxe.servername
 * pxe.options
 * commit(), apply changes and restart dnsmasq

### FTP
- configure chosen ftp server, all over ssh
- limited support now e.g. just expose directory
- work with factory class
    - wrt = j.ssh.openwrt.get(sshconnection) 
    - wrt.ftp.<method>
> ftp configures PureFTP server, by default it uses unix authentication to serve users. So to access you need a user account on the openwrt device.
    - commit(), apply all ftp settings

FTP API exposes the following properties:
```raw
wrt.ftp.EXPOSED_BOOLEAN_FIELDS      wrt.ftp.ipv6only
wrt.ftp.EXPOSED_FIELDS              wrt.ftp.keepallfiles
wrt.ftp.PACKAGE                     wrt.ftp.limitrecursion
wrt.ftp.SECTION                     wrt.ftp.login
wrt.ftp.allowanonymousfxp           wrt.ftp.logpid
wrt.ftp.allowdotfiles               wrt.ftp.maxclientsnumber
wrt.ftp.allowuserfxp                wrt.ftp.maxclientsperip
wrt.ftp.altlog                      wrt.ftp.maxdiskusagepct
wrt.ftp.anonymousbandwidth          wrt.ftp.maxidletime
wrt.ftp.anonymouscancreatedirs      wrt.ftp.maxload
wrt.ftp.anonymouscantupload         wrt.ftp.minuid
wrt.ftp.anonymousonly               wrt.ftp.natmode
wrt.ftp.anonymousratio              wrt.ftp.noanonymous
wrt.ftp.antiwarez                   wrt.ftp.nochmod
wrt.ftp.authentication              wrt.ftp.norename
wrt.ftp.autorename                  wrt.ftp.notruncate
wrt.ftp.bind                        wrt.ftp.package
wrt.ftp.bonjour                     wrt.ftp.passiveportrange
wrt.ftp.brokenclientscompatibility  wrt.ftp.peruserlimits
wrt.ftp.chrooteveryone              wrt.ftp.pidfile
wrt.ftp.clientcharset               wrt.ftp.port
wrt.ftp.commit                      wrt.ftp.prohibitdotfilesread
wrt.ftp.createhomedir               wrt.ftp.prohibitdotfileswrite
wrt.ftp.customerproof               wrt.ftp.section
wrt.ftp.daemonize                   wrt.ftp.syslogfacility
wrt.ftp.displaydotfiles             wrt.ftp.trustedgid
wrt.ftp.dontresolve                 wrt.ftp.trustedip
wrt.ftp.enabled                     wrt.ftp.umask
wrt.ftp.forcepassiveip              wrt.ftp.uploadscript
wrt.ftp.fortunesfile                wrt.ftp.userbandwidth
wrt.ftp.fscharset                   wrt.ftp.userratio
wrt.ftp.ipv4only                    wrt.ftp.verboselog
```

## Linux (Ubuntu)
The next set of SAL's are designed mainly to work with ubuntu, but they can be used with other distributions of linux (or even OpenWRT) if the configuration files are compatible.

### Network
Get the ubuntu network manager as following:

```python
u = j.ssh.ubuntu.get(cl)
#where cl is the cuisine connection to the desired machine
```

Ubuntu API only provides `network` interface atm. the `network` interface is used to inspect network setup of ubuntu machine and to modify it as desired.

Provided methods and properties
* `commit`: Commit/Apply and changes done by the API 
* `ipGet`: Get IP of a nic
* `ipReset`: Reset IP settings for a nic
* `ipSet`: Sets IP
* `nics`: List of known machine nics
* `nsGet`: Get the configured nameserver
* `nsSet`: Sets the nameserver
* `setHostname`: Sets the machine hostname

### NFS
* configure nfs server, all over ssh
* limited support now e.g. just expose directory
* work with factory class
 * j.ssh.uci_nfs.get(sshconnection) 
* methods on SAL
 * exports (property): List of exported paths
 * erase(): Remove all exports
 * add(path): Exposes a path (returns an `NFSExport` objects, that can be use to fine-tune the xport)
 * delete(path): Unexposes a path
 * commit(): Apply the changes to the nfs /etc/exports file and reload

### Disk Manager
```python
sshconnection = j.remote.cuisine.connect(...)
mgr = j.ssh.disklayout.get(sshconnection)
```
### Manager API
#### getDisks()
```python
disks = mgr.getDisks()
"""Get list of all available disks on machine"""
```

### Disk API
Each disk holds the following information:
- disk.partitions, list of partitions on that disk
- disk.name, device name (ex: /dev/sda)
- disk.size, disk size in bytes

#### disk.erase
```python
disk.erase(force=False)
"""
Clean up disk by deleting all non protected partitions
if force=True, delete ALL partitions included protected

:force: delete protected partitions, default=False
"""
```
#### disk.format
```python
disk.format(size, hrd)
"""
Create new partition and format it as configured in hrd file

:size: in bytes
:hrd: the disk hrd info

:return: new partition instance
Note:
hrd file must contain the following

filesystem                     = '<fs-type>'
mountpath                      = '<mount-path>'
protected                      = 0 or 1
type                           = data or root or tmp
"""
```

### Partition API
Each disk has a list of attached partitions. The only way to create a new partition is to call `disk.format()` as explained above.
Each partition holds the following attributes

- partition.name, holds the device name (ex: /dev/sda1)
- partition.size, partition size in bytes
- partition.fstype, partition filesystem 
- partition.uuid, filesystem UUID
- partition.mountpoint, where the partition is mounted
- partition.hrd, the HRD instance used when creating the partition or None 

> partition.hrd can be `None`, in that case partition is considered `unmanaged` Which means partition is NOT created by the SAL. This type of partitions is considered 'protected' by default

> Partition attributes reflects the **real** state of the partition. For example, `mountpoint` will be set IF the partition is actually mounted, and is not related to the `mountpath` defined in the hrd file.

#### partition.delete
```python
partition.delete(force=False)
"""
Delete the partition

:force: Force delete protected partitions, default False
"""
```

#### partition.format
```python
partition.format()
"""
Reformat the partition according to HRD
"""
```

#### partition.mount
```python
parition.mount()
Mount partition to `mountpath` defined in HRD
```

#### partition.setAutoMount
```python
partition.setAutoMount(options='defaults', _dump=0, _pass=0)
"""
Configure partition auto mount `fstab` on `mountpath` defined in HRD
"""
```

#### partition.unsetAutoMount
```python
partition.unsetAutoMount()
"""
remote partition from fstab
"""
```

### Nginx
- configure nginx server, all over ssh
- work with factory class
    - j.ssh.nginx.get(sshconnection, configpath="/etc/nginx") 
- methods on SAL
    - erase
    - add(...
    - delete(...
    - addconfig(... #push nginx configuration file to server and make sure it gets included when loading)
    - reload

### SSH
- configure ssh server, all over ssh
- work with factory class
    - j.ssh.server.get(sshconnection) 
- methods on SAL
    - erase
    - addkey(key)
    - deletekey(key)
    - disableNonKeyAccess()
    - commit()

### ufw SAL
- configure ufw firewall, all over ssh  - work with factory class
    - j.ssh.ufw.get(sshconnection) 
- methods on SAL
    - enabled, ufw status
    - rules, all configured rules
    - portOpen(port), short cut to open a port
    - portClose(port), short cut to close a port
    - addRule(action, source, destination), add a ufw rule
    - removeRule(rule), remove a ufw rule
    - reset(), drop all rules
    - commit(), apply changes to ufw
    
```python
ufw = j.ssh.ufw.get(connection)

ufw.enabled = False
ufw.reset()
ufw.addRule(ufw.ACTION_ALLOW_IN, 'any', '22/tcp')
ufw.enabled = True

ufw.commit()
```