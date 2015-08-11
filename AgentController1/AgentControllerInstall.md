install of agent controller
===========================

requirements
------------

-   make sure jumpscale is installed properly (see [JumpScale Installation](../Core/Install/Install.md))
-   make sure osis & portal are installed (see [Portal Installation](../portal/Install.md) and [OSIS Installation](../OSIS/Install.md))

install as all in 1 install
---------------------------

install modular
---------------

```shell
#agentcontroller
ays install -n agentcontroller -i main --data="\
osis.connection=main #

#@todo complete
```
