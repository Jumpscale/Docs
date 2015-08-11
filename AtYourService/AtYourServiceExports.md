recipe part of service.hrd
=====================

this explains how a binary repo will be checked out to local filesystem

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

