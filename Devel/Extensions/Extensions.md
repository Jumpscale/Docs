Extensions Documentation
========================

Extension in JumpScale are really easy to write they are just Python modules hooked into the `j` namespace.

## Example

Lets call our extension demo

lets put our moduel at `/opt/jumpscale7/lib/JumpScale/lib/demo/`
We will have two files `__init__.py` and `demo.py`


```python
class DemoFactory(object):
    def play(self):
        print 'play'
```

```python
form JumpScale import j

def cb():
    from .demo import DemoFactory
    return DemoFactory()

# register our exnteions on the j namespace
j.base.loader.makeAvailable(j, 'clients')
j.clients._register('demo', cb)

```