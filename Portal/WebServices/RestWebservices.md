query as json
=============

```
http://localhost:82/rest/system/contentmanager/getSpaces?format=json
```
(where 82 is your configured port)



if no error:

```
['tests', 'system', 'testwebsite', 'grid', 'testspace', 'home', 'ays']
```


if error:

```
"Param with name:namespace is missing."
```

or

```
Execute method GET_system_contentmanager_modelobjectlist failed.
Traceback (most recent call last):
~ File "/opt/jumpscale7/lib/JumpScale/portal/portal/PortalRest.py", line 163, in execute_rest_call
result = method(ctx=ctx, **ctx.params)
~ File "/opt/jumpscale7/apps/portals/portalbase/system/system__contentmanager/methodclass/system_contentmanager.py", line 94, in modelobjectlist
data = dtext.getData(namespace, category, key, **args)
~ File "/opt/jumpscale7/apps/portals/portalbase/system/system__contentmanager/extensions/extension_datatable/DataTables.py", line 88, in getData
datainfo = self.getFromCache(key)
~ File "/opt/jumpscale7/apps/portals/portalbase/system/system__contentmanager/extensions/extension_datatable/DataTables.py", line 69, in getFromCache
return self.cache.cacheGet(key)
~ File "/opt/jumpscale7/lib/JumpScale/baselib/key_value_store/store.py", line 102, in cacheGet
r=self.get("cache",key)
~ File "/opt/jumpscale7/lib/JumpScale/baselib/key_value_store/memory_store.py", line 21, in get
raise RuntimeError("Could not find object with category %s key %s"%(category,key))
~ RuntimeError: Could not find object with category cache key 1234

type/level: UNKNOWN/1
Execute method GET_system_contentmanager_modelobjectlist failed.
querystr was:category=%27%27&namespace=%27%27&key=1234&format=json
method was:/rest/system/contentmanager/modelobjectlist
```


how to know if appropriate result result is always a dict check on key
"result" if not there is an errorcondition object with props as shown
above

if no format str -\> text readable
----------------------------------

very difficult to parse but ideal to play around with on webserver
