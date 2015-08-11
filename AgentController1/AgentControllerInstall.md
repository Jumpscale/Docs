install of agent controller
===========================

requirements
------------

-   make sure jumpscale is installed properly (see [JumpScale Installation](../Core/Install/Install.md))
-   make sure osis & portal are installed (see [Portal Installation](../portal/Install.md) and [OSIS Installation](../OSIS/Install.md))

install locally as all in 1 install
---------------------------

```
ays install -n singlenode_grid
```

install modular
---------------

```shell
#agentcontroller
ays install -n agentcontroller -i main --data='osis.connection:main'

#agentcontroller client
ays install -n agentcontroller_client -i main --data 'agentcontroller.client.addr:127.0.0.1 agentcontroller.client.port:4444 agentcontroller.client.login:node agentcontroller.client.passwd:'
```
