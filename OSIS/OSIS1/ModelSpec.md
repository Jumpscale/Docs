# Osis Model Specs

* A `model.category` is placed under the osis application inside the namespace the model represent.
* Example.
```
[rootmodel:alert] @index
    prop:id int,,
    prop:gid int,,
    prop:nid int,,
    prop:description str,,
    prop:descriptionpub str,,
    prop:level int,, 1:critical, 2:warning, 3:info
    prop:category str,, dot notation e.g. machine.start.failed
    prop:tags str,, e.g. machine:2323
    prop:state str,, ["NEW","ALERT","CLOSED"]
    prop:inittime int,, first time there was an error condition linked to this alert
    prop:lasttime int,, last time there was an error condition linked to this alert
    prop:closetime int,, alert is closed, no longer active
    prop:nrerrorconditions int,, nr of times this error condition happened
    prop:errorconditions list(int),, ids of errorconditions
```

## Supported data types

#### Primitive data types
   * **int**     [integer]
   * **list**    [List/Array]
   * **str**     [String]
   * **list(int)**   [List of integers]
   * **list(dict)**  [List of dictionaries]
   * **dict**        [Dictionary]

#### Complex datatypes
   * We have 2 types of models 
     * ROOT models defined by ```[rootmodel:rootmodelname]```
     * Child models defined by ```[model:childmodelname]```
   * Only child models can be referenced by root models
   * You can't reference one root model from another root model
   * You can't reference one child model from another child model
   * you can reference a child model directly as in:
     * Example:
      ```
      [rootmodel:A] @index
         prop:value AA,,     # References another Child model (AA)

      [model:AA] @index      # Child model AA
          prop:value int,,

      [rootmodel:AList] @index  
         prop:value list(A),,   # References List of As
```

## Support Time to live for model records
* Add the `@TTL: seconds` tag
* This means that each record will live for those seconds (unless updated)
* This works by using mongodb TTL functionality.
* Example
```
    [rootmodel:sessioncache] @TTL:432000
        prop:value dict,,
        prop:createdat datetime,,
        prop:lastupdatedat datetime,,
```
