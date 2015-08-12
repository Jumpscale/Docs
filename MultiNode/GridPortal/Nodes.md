##Nodes

An overview of all nodes in a set up. Shown under [http:localhost:82/Grid/Nodes](http:localhost:82/grid/Nodes)

Jobs are sortable and filterable by time of occurrence, command, result and STATE. Further details show Grid and node IDs where the job ran, roles the job ran by, the executed [JumpScript](../AgentController1/JumpScript.md) if one was, which queue the job ran on and logs from the job.

Job states can be:
* "OK" for jobs that have been executed successfully.
* "ERROR" for jobs that have failed.
* "TIMEOUT" for jobs that have timed out.
* "SCHEDULED" for jobs that have not yet run.
