## recipe part of service.hrd

this explains how a binary repo will be checked out to local filesystem

### legacy format (still works)

```
git.build.1=
    url:'http://git.aydo.com/aydo/qemu-ledis',

git.export.1=
    url:'http://git.aydo.com/binary/kvm',
    source:'root/apps/kvm',
    revision:,
    dest:'$(system.paths.base)'/apps/kvm,
    link:False

```

git.build means will only be checkout during build


### recommended new format

```
git.build.1=
    site:'git.aydo.com',
    account:'static-websites',
    repo:'new-gig',

git.export.1                   =
    dest:'$(system.paths.base)/apps/www/gig',
    link:'True',
    source:'www.greenitglobe.com',
    site:'git.aydo.com',
    account:'static-websites',
    repo:'new-gig',
```

- if ssh-agent is loaded & a key has been found then the checkout will happen over ssh.
    - we strongly recommend this way of working
- if not http will be used