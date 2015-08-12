## install of AgentController


###Requirements


-   make sure jumpscale is installed properly (see [JumpScale Installation](/GettingStarted/Install.md))
-   make sure osis & portal are installed (see [Portal Installation](/portal/Install.md) and [OSIS Installation](/OSIS/Install.md))

###install locally as all in 1 install


```
ays install -n singlenode_grid
```
When you are asked about the portal, make sure that you select the same value entered during portal installation This will install all required packages on 1 node

gridportal
osis
influxdb & mongodb (databases behind osis)
the agent controller
the jsagent (connecting to the agentcontroller)


###install modular


```shell
#agentcontroller
ays install -n agentcontroller -i main --data='osis.connection:main'

#agentcontroller client
ays install -n agentcontroller_client -i main --data 'agentcontroller.client.addr:127.0.0.1 agentcontroller.client.port:4444 agentcontroller.client.login:node agentcontroller.client.passwd:'
```
