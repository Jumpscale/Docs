How to compare directories
==========================

```shell
ays install -n meld
```

@todo needs to be ported to jumpscale7, not available yet.

this will install some default filters.

unsupported image:/images/unknownspace/meldcompare.png !meldcompare.png!

how to use for comparing quality levels for jpackages.
------------------------------------------------------

e.g.

```shell
meld /opt/code/jumpscale/default__jp_jumpscale/unstable7/ /opt/code/jumpscale/default__jp_jumpscale/test7/ -a
```

this will compare unstable7 with tes7 quality level, don't forget to
select right filters (select them all), to only see what you want.
