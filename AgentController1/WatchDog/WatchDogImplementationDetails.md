Implementation Details
======================

value is send to 2 destinations over http post, rest call
format/destination: escalation flow

-   when critical -\> escalate to contact 1
-   when no response in 5 min -\> escalate to contact 2&3
-   when no response in 15 min -\> escalate to all, send SMS to
    Jan,Kristof,Rob
-   response means confirm on rogerthat working on issue
-   format
-   json
-   fields used at client
-   nid
-   gid
-   category e.g. cpu.core
-   state= OK, CRITICAL, WARNING
-   value (int) is last measured value (percent:0-100, otherwise real
    value)
-   ecoguid : optional errorcondition guid
-   remark: for status checks there is no value, only use state &
    category

fields used at server

-   epoch
-   escalationstate
    -   L1 = escalated to contact 1
    -   L2 = escalated to contact 2 & 3 (so contact 1 did not reply in 5
        min)
    -   L3 = escalated to all, Jan, Kristof, Rob (2 and 3 did not reply
        in 15 min)
    -   C = confirmed (the support person confirmed the issue, means
        will now look at it)
    -   A = accepted (the support person accepted the issue, means will
        work on it and resolve)
    -   R = resolved (now support person need to talk with customer if
        required, or if not needed can close)
    -   Z = closed (no need to look at it)
-   log = [[\$epoch,\$userid,\$state]($epoch,$userid,$state)] e.g. at
    14h, despiegk confirmed the issue ©

each grid has a unique GUID (generated at grid level) alerts are stored
under following key

-   \$gridguid:alerts:\$nid\_\$category
-   \$nid is 0 when for grid e.g. grid.healthcheck

how on server
-------------

2 servers 1 server process on each server this server process does the
rogerthat handling
<http://www.rogerthat.net/developers/example-code/#Python_Example> the
main loop puts marker in redis does the escalation process 2 core
watchdogprocesses which use redis of other side to see that the 2 main
server processes are working
