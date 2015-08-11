Distributed Work Controller
===========================

Introduction.
-------------

JumpScale provides the capability to execute tasks on x number of nodes.

Those tasks can be executed in different ways

-   async, task is executed in a [worker](workers.md)
-   sync, task is executed in the [JSAgent](JSAgent.md)
-   on interval, task is executed either in the
    [JSAgent](JSAgent.md) or [worker](workers.md) on the
    specified interval

Read more about the AgentController [here](AgentControllerServer.md)

Useful links
-------------

-   [How To Schedule Work using AgentController](ScheduleWork.md)
-   [Usage of redis in AgentController and JSAgent](redis.md)
-   [Understanding JumpScripts and utilizing](JumpScript.md)

