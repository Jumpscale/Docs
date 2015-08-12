## Introduction
JS Agent, is a process manager and a remote command executor that gets it's jobs and tasks by polling from AC (Agent Controller).

The Agent will also monitor the jobs, updating the AC with `stats` and `logs`. All according to specs. 

## Installation
```bash
go get github.com/Jumpscale/jsagent
```

## Running the agent
Make sure you have an AC (agent controller) running before attempting to start the agent. Also review the agent [[configurations|Agent Configuration]]

```bash
cd $GOPATH/src/github.com/Jumpscale/jsagent
go superagent.go -c agent.toml
```

The `agent.toml` is described in details in [Agent Configuration](agent-configuration.md) page

## Command syntax
see section about cmd syntax

## Stats
Check [Stats](Stats.md) page for more details on how stats aggregation works, and how scripts/external processes can send stats messages to the stats aggregator.