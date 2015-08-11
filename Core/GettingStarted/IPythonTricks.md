IPython Tricks
==============

how to play with the default loaded libraries
---------------------------------------------

you can walk around in the JumpScale namespace by using j. and tab

how to get info about a method for an JumpScale lib
---------------------------------------------------

e.g. j.system.fs.createDir(?

```python
In [1]: j.system.fs.createDir(?
File:       /usr/lib/python2.7/JumpScale/core/system/fs.py
Definition: o.system.fs.createDir(self, newdir, skipProtectedDirs=False)
Docstring:
Create new Directory
@param newdir: string (Directory path/name)
if newdir was only given as a directory name, the new directory will be created on the default path,
if newdir was given as a complete path with the directory name, the new directory will be created in the specified path
```

how to know where a library is on the filesystem
------------------------------------------------

see above, look at help of method, the File: info shows where the file
is which implements the method

how to load extra modules in JumpScale
--------------------------------------

do

```python
import JumpScale.[tab]
```

this will show you which libs can be imported. The only relevant ones
for now to import are

-   JumpScale.baselib : a std set of quite a log of libraries
-   JumpScale.grid : only import as import JumpScale.grid will load
    everything underneath, is the core grid system
-   JumpScale.portal : only import as import JumpScale.portal will load
    everything underneath, is the core portal system

to drill deeper do

```python
import JumpScale.baselib.[tab]
```

how to know which modules are availabe in JumpScale
---------------------------------------------------

)-: needs to be further implemented but the ones which are probably
relevant to play with now are found by

```python
import JumpScale.baselib.[tab]
```
