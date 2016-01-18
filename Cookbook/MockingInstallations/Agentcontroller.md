AgentController2 in AYS8:

Agentcontroller2 requires a running redis and a running syncthing.
You should already have a redis server (through JumpScale)

1. Get Syncthing:
Get from binaries [here](https://git.aydo.com/binary/syncthing)
Run with
```
./syncthing
```

2. Get AgentController2:
Fetch its binaries from [the binary repo](https://git.aydo.com/binary/agentcontroller2)
Run with
```
./agentcontroller2 -c agentcontroller2.toml
```
PS: Make sure the toml configuration points to the correct syncthing port (default 8384) and redis port


3. Get Agent2:
Fetch the agent2 binaries from [here](https://git.aydo.com/binary/agent2)
Run with
```
./agent2 -c agent2.toml 
```


Furthere documentation can be found in the [gitbook](https://gig.gitbooks.io/jumpscale/content/MultiNode/AgentController2/AgentController2.html)
