Schedule work
=============

```
# get an AgentConroller client
acl = j.clients.agentcontroller.get()

#Schedule a jumpscript to run asynchronously
acl.executeJumpscript('jumpscale', 'echo', nid=j.application.whoAmI.nid, args={'msg':'test'}, wait=False)

```
