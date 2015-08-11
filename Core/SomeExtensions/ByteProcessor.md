ByteProcessor
=============

```python
j.base.byteprocessor.
j.base.byteprocessor.compress                 
j.base.byteprocessor.disperse                 
j.base.byteprocessor.hashMd5                  
j.base.byteprocessor.hashTiger192             
j.base.byteprocessor.decompress               
j.base.byteprocessor.getDispersedBlockObject  
j.base.byteprocessor.hashTiger160             
j.base.byteprocessor.undisperse
```

-   compress/decompess: blosc compression (ultra fast,+ 250MB/sec)
-   hashTiger... : ultra reliable hashing (faster than MD5 & longer
    keys)
-   disperse/undiserpse: erasure coding (uses zfec :
    <https://pypi.python.org/pypi/zfec>)

