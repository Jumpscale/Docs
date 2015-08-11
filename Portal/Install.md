# Quick Start

## requirements

The JumpScale portal requires the JumpScale framework to be installed.
So if you didn't do so [install JumpScale](http://github.com/Jumpscale/jumpscale_core7/wiki/Install).

## To make your own portal

Install base portal package

```
ays install -n singlenode_portal
ays install -n portal -i myportal
```

Your portal code can now be placed @ `$basedir/apps/portal/myportal`

## Control your portal

Start your portal with `ays start -n portal -i myportal`  
Stop your portal with `ays stop -n portal -i myportal`

