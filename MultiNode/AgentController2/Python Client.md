## Installation
To install the python client extension
```bash
ays install -n agentcontroller2_client
```
## Getting client instance
```python
client = j.clients.ac.getByInstance('main')
#OR if you have `redis` info.
client = j.clients.ac.get(address, port, password)
```
<div class="section" id="welcome-to-acclient-s-documentation">
<div class="toctree-wrapper compound">
</div>
<span class="target" id="module-acclient"></span><dl class="class">
<dt id="acclient.BaseCmd">
<em class="property">class </em><code class="descclassname">acclient.</code><code class="descname">BaseCmd</code><span class="sig-paren">(</span><em>client</em>, <em>id</em>, <em>gid</em>, <em>nid</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.BaseCmd" title="Permalink to this definition">¶</a></dt>
<dd><p>Base command. You never need to create an instance of this class, always use <a class="reference internal" href="#acclient.Client.cmd" title="acclient.Client.cmd"><code class="xref py py-func docutils literal"><span class="pre">acclient.Client.cmd()</span></code></a> or any of
the other shortcuts.</p>
<dl class="method">
<dt id="acclient.BaseCmd.get_msgs">
<code class="descname">get_msgs</code><span class="sig-paren">(</span><em>levels='*'</em>, <em>limit=20</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.BaseCmd.get_msgs" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets job log messages from agent</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
<li><strong>levels</strong> – Log levels to retrieve, default to ‘*’ (all)</li>
<li><strong>limit</strong> – Max number of log lines to retrieve (max to 1000)</li>
</ul>
</td>
</tr>
<tr class="field-even field"><th class="field-name">Return type:</th><td class="field-body"><p class="first last">list of dict</p>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="acclient.BaseCmd.get_result">
<code class="descname">get_result</code><span class="sig-paren">(</span><em>timeout=0</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.BaseCmd.get_result" title="Permalink to this definition">¶</a></dt>
<dd><p>Pops and returns the first available result for that job. It blocks until the result is givent</p>
<dl class="docutils">
<dt>The result is POPed out of the result queue, so a second call to the same method will block until a new</dt>
<dd>result object is available for that job. In case you don’t want to wait use noblock_get_result()</dd>
</dl>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>timeout</strong> – Waits for this amount of seconds before giving up on results. 0 means wait forever.</td>
</tr>
<tr class="field-even field"><th class="field-name">Return type:</th><td class="field-body">dict</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="acclient.BaseCmd.get_stats">
<code class="descname">get_stats</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#acclient.BaseCmd.get_stats" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets the job cpu and memory stats on agent. Only valid if job is still running on
agent. otherwise will give a ‘job id not found’ error.</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.BaseCmd.gid">
<code class="descname">gid</code><a class="headerlink" href="#acclient.BaseCmd.gid" title="Permalink to this definition">¶</a></dt>
<dd><p>Grid ID</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.BaseCmd.id">
<code class="descname">id</code><a class="headerlink" href="#acclient.BaseCmd.id" title="Permalink to this definition">¶</a></dt>
<dd><p>Command ID</p>
</dd></dl>

<dl class="method">
<dt id="acclient.BaseCmd.kill">
<code class="descname">kill</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#acclient.BaseCmd.kill" title="Permalink to this definition">¶</a></dt>
<dd><p>Kills this command on agent (if it’s running)</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.BaseCmd.nid">
<code class="descname">nid</code><a class="headerlink" href="#acclient.BaseCmd.nid" title="Permalink to this definition">¶</a></dt>
<dd><p>Node ID</p>
</dd></dl>

<dl class="method">
<dt id="acclient.BaseCmd.noblock_get_result">
<code class="descname">noblock_get_result</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#acclient.BaseCmd.noblock_get_result" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a list with all available job results (non-blocking)</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">list of dicts</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="acclient.Client">
<em class="property">class </em><code class="descclassname">acclient.</code><code class="descname">Client</code><span class="sig-paren">(</span><em>address='localhost'</em>, <em>port=6379</em>, <em>password=None</em>, <em>db=0</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new client instance. You need a client to send jobs to the agent-controller
and to retrieve results</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>address</strong> – Redis host address</li>
<li><strong>port</strong> – Redis port</li>
<li><strong>password</strong> – (optional) redis password</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="method">
<dt id="acclient.Client.cmd">
<code class="descname">cmd</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em>, <em>cmd</em>, <em>args</em>, <em>data=None</em>, <em>id=None</em>, <em>role=None</em>, <em>fanout=False</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.cmd" title="Permalink to this definition">¶</a></dt>
<dd><p>Executes a command, return a cmd descriptor</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>gid</strong> – grid id (can be None)</li>
<li><strong>nid</strong> – node id (can be None)</li>
<li><strong>cmd</strong> – one of the supported commands (execute, execute_js_py, get_x_info, etc...)</li>
<li><strong>args</strong> – instance of RunArgs</li>
<li><strong>data</strong> – Raw data to send to the command standard input. Passed as objecte and will be dumped as json on
wire</li>
<li><strong>id</strong> – id of command for retrieve later, if None a random GUID will be generated.</li>
<li><strong>role</strong> – Optional role, only agents that satisfy this role can process this job. This is mutual exclusive
with gid/nid compo in that case, the gid/nid values must be None or a ValueError will be raised.
There is a special role ‘*’ which means ANY.</li>
<li><strong>fanout</strong> – Send job to ALL agents that satisfy the given role. Only effective is role is set.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>Allowed compinations:</p>
<table border="1" class="docutils">
<colgroup>
<col width="9%">
<col width="9%">
<col width="11%">
<col width="71%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">GID</th>
<th class="head">NID</th>
<th class="head">ROLE</th>
<th class="head">Meaning</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>X</td>
<td>X</td>
<td>O</td>
<td>To specific agent Gid/Nid</td>
</tr>
<tr class="row-odd"><td>X</td>
<td>O</td>
<td>X</td>
<td>Any agent with that role on this grid</td>
</tr>
<tr class="row-even"><td>O</td>
<td>O</td>
<td>X</td>
<td>Any agent with that role globaly</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><a class="reference internal" href="#acclient.Cmd" title="acclient.Cmd"><code class="xref py py-class docutils literal"><span class="pre">acclient.Cmd</span></code></a></td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.execute">
<code class="descname">execute</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em>, <em>executable</em>, <em>cmdargs=None</em>, <em>args=None</em>, <em>data=None</em>, <em>id=None</em>, <em>role=None</em>, <em>fanout=False</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.execute" title="Permalink to this definition">¶</a></dt>
<dd><p>Short cut for cmd.execute</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>gid</strong> – grid id</li>
<li><strong>nid</strong> – node id</li>
<li><strong>executable</strong> – the executable to run_args</li>
<li><strong>cmdargs</strong> – An optional array with command line arguments</li>
<li><strong>args</strong> – Optional RunArgs</li>
<li><strong>data</strong> – Raw data to the command stdin. (see cmd)</li>
<li><strong>id</strong> – Optional command id (see cmd)</li>
<li><strong>role</strong> – Optional role, only agents that satisfy this role can process this job. This is mutual exclusive
with gid/nid compo in that case, the gid/nid values must be None or a ValueError will be raised.</li>
<li><strong>fanout</strong> – Fanout job to all agents with given role (only effective if role is set)</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.execute_js_py">
<code class="descname">execute_js_py</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em>, <em>domain</em>, <em>name</em>, <em>data=None</em>, <em>args=None</em>, <em>role=None</em>, <em>fanout=False</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.execute_js_py" title="Permalink to this definition">¶</a></dt>
<dd><p>Executes jumpscale script (py) on agent. The execute_js_py extension must be
enabled and configured correctly on the agent.</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>gid</strong> – Grid id</li>
<li><strong>nid</strong> – Node id</li>
<li><strong>domain</strong> – Domain of script</li>
<li><strong>name</strong> – Name of script</li>
<li><strong>data</strong> – Data object (any json serializabl struct) that will be sent to the script.</li>
<li><strong>args</strong> – Optional run arguments</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.get_by_id">
<code class="descname">get_by_id</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em>, <em>id</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.get_by_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a command descriptor by an ID. So you can read command result later if the ID is known.</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><a class="reference internal" href="#acclient.BaseCmd" title="acclient.BaseCmd"><code class="xref py py-class docutils literal"><span class="pre">acclient.BaseCmd</span></code></a></td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.get_cpu_info">
<code class="descname">get_cpu_info</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.get_cpu_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Get CPU info of the agent node</p>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.get_disk_info">
<code class="descname">get_disk_info</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.get_disk_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Get disk info of the agent node</p>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.get_jobs">
<code class="descname">get_jobs</code><span class="sig-paren">(</span><em>start=0</em>, <em>count=100</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.get_jobs" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieves jobs losgs. This by default returns the latest 100 jobs. You can
change the <cite>start</cite> and <cite>count</cite> argument to thinking of the jobs history as a list where
the most recent job is at index 0</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>start</strong> – Start index to retrieve, default 0</li>
<li><strong>count</strong> – Number of jobs to retrieve</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.get_mem_info">
<code class="descname">get_mem_info</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.get_mem_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Get MEM info of the agent node</p>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.get_msgs">
<code class="descname">get_msgs</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em>, <em>jobid=None</em>, <em>timefrom=None</em>, <em>timeto=None</em>, <em>levels='*'</em>, <em>limit=20</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.get_msgs" title="Permalink to this definition">¶</a></dt>
<dd><p>Query and return log messages stored on agent side.</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>gid</strong> – Grid id</li>
<li><strong>nid</strong> – Node id</li>
<li><strong>jobid</strong> – Optional jobid</li>
<li><strong>timefrom</strong> – Optional time from (unix timestamp in seconds)</li>
<li><strong>timeto</strong> – Optional time to (unix timestamp in seconds)</li>
<li><strong>levels</strong> – Levels to return (ex: 1,2,3 or 1,2,6-9 or * for all)</li>
<li><strong>limit</strong> – Max number of log messages to return. Note that the agent in anyways will not return
more than 1000 record</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.get_nic_info">
<code class="descname">get_nic_info</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.get_nic_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Get NIC info of the agent node</p>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.get_os_info">
<code class="descname">get_os_info</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.get_os_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Get OS info of the agent node</p>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.get_processes">
<code class="descname">get_processes</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em>, <em>domain=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.get_processes" title="Permalink to this definition">¶</a></dt>
<dd><p>Get stats for all running process at the moment of the call, optionally filter with domain and/or name</p>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.tunnel_close">
<code class="descname">tunnel_close</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em>, <em>local</em>, <em>gateway</em>, <em>ip</em>, <em>remote</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.tunnel_close" title="Permalink to this definition">¶</a></dt>
<dd><p>Closes a tunnel previously opened by tunnel_open. The <cite>local</cite> port MUST match the
real open port returned by the tunnel_open function. Otherwise the agent will not match the tunnel and return
ignore your call.</p>
<p>Closing a non-existing tunnel is not an error.</p>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.tunnel_list">
<code class="descname">tunnel_list</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.tunnel_list" title="Permalink to this definition">¶</a></dt>
<dd><p>Return all opened connection that are open from the agent over the agent-controller it
received this command from</p>
</dd></dl>

<dl class="method">
<dt id="acclient.Client.tunnel_open">
<code class="descname">tunnel_open</code><span class="sig-paren">(</span><em>gid</em>, <em>nid</em>, <em>local</em>, <em>gateway</em>, <em>ip</em>, <em>remote</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Client.tunnel_open" title="Permalink to this definition">¶</a></dt>
<dd><p>Opens a secure tunnel that accepts connection at the agent’s local port <cite>local</cite>
and forwards the received connections to remote agent <cite>gateway</cite> which will
forward the tunnel connection to <cite>ip:remote</cite></p>
<p>Note: The agent will proxy the connection over the agent-controller it recieved this open command from.</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>gid</strong> – Grid id</li>
<li><strong>nid</strong> – Node id</li>
<li><strong>local</strong> – Agent’s local listening port for the tunnel. 0 for dynamic allocation</li>
<li><strong>gateway</strong> – The other endpoint <cite>agent</cite> which the connection will be redirected to.
This should be the name of the hubble agent.
NOTE: if the endpoint is another superangent, it automatically names itself as ‘&lt;gid&gt;.&lt;nid&gt;’</li>
<li><strong>ip</strong> – The endpoint ip address on the remote agent network. Note that IP must be a real ip not a host name
dns names lookup is not supported.</li>
<li><strong>remote</strong> – The endpoint port on the remote agent network</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="acclient.Cmd">
<em class="property">class </em><code class="descclassname">acclient.</code><code class="descname">Cmd</code><span class="sig-paren">(</span><em>client</em>, <em>id</em>, <em>gid</em>, <em>nid</em>, <em>cmd</em>, <em>args</em>, <em>data</em>, <em>role</em>, <em>fanout</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Cmd" title="Permalink to this definition">¶</a></dt>
<dd><p>Child of <a class="reference internal" href="#acclient.BaseCmd" title="acclient.BaseCmd"><code class="xref py py-class docutils literal"><span class="pre">acclient.BaseCmd</span></code></a></p>
<p>You probably don’t need to make an instance of this class manually. Alway use <a class="reference internal" href="#acclient.Client.cmd" title="acclient.Client.cmd"><code class="xref py py-func docutils literal"><span class="pre">acclient.Client.cmd()</span></code></a> or
ony of the client shortcuts.</p>
<dl class="attribute">
<dt id="acclient.Cmd.args">
<code class="descname">args</code><a class="headerlink" href="#acclient.Cmd.args" title="Permalink to this definition">¶</a></dt>
<dd><p>Command run arguments</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.Cmd.cmd">
<code class="descname">cmd</code><a class="headerlink" href="#acclient.Cmd.cmd" title="Permalink to this definition">¶</a></dt>
<dd><p>Command name</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.Cmd.data">
<code class="descname">data</code><a class="headerlink" href="#acclient.Cmd.data" title="Permalink to this definition">¶</a></dt>
<dd><p>Command data</p>
</dd></dl>

<dl class="method">
<dt id="acclient.Cmd.dump">
<code class="descname">dump</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#acclient.Cmd.dump" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets the command as a dict</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">dict</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="attribute">
<dt id="acclient.Cmd.fanout">
<code class="descname">fanout</code><a class="headerlink" href="#acclient.Cmd.fanout" title="Permalink to this definition">¶</a></dt>
<dd><p>Either to fanout command</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.Cmd.role">
<code class="descname">role</code><a class="headerlink" href="#acclient.Cmd.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Command role</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="acclient.RunArgs">
<em class="property">class </em><code class="descclassname">acclient.</code><code class="descname">RunArgs</code><span class="sig-paren">(</span><em>domain=None</em>, <em>name=None</em>, <em>max_time=0</em>, <em>max_restart=0</em>, <em>recurring_period=0</em>, <em>stats_interval=0</em>, <em>args=None</em>, <em>loglevels='*'</em>, <em>loglevels_db=None</em>, <em>loglevels_ac=None</em>, <em>queue=None</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.RunArgs" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new instance of RunArgs</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>domain</strong> – Domain name</li>
<li><strong>name</strong> – script or executable name</li>
<li><strong>max_time</strong> – Max run time, 0 (forever), -1 forever but remember during reboots (long running),
other values is timeout</li>
<li><strong>max_restart</strong> – Max number of restarts if process died in under 5 min.</li>
<li><strong>recurring_period</strong> – Scheduling time</li>
<li><strong>stats_interval</strong> – How frequent the stats aggregation is done/flushed to AC</li>
<li><strong>args</strong> – Command line arguments (in case of execute)</li>
<li><strong>loglevels</strong> – Which log levels to capture and pass to logger</li>
<li><strong>loglevels_db</strong> – Which log levels to store in DB (overrides logger defaults)</li>
<li><strong>loglevels_ac</strong> – Which log levels to send to AC (overrides logger defaults)</li>
<li><strong>queue</strong> – Name of the command queue to wait on.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>This job will not get executed until no other commands running on the same queue.</p>
<dl class="attribute">
<dt id="acclient.RunArgs.args">
<code class="descname">args</code><a class="headerlink" href="#acclient.RunArgs.args" title="Permalink to this definition">¶</a></dt>
<dd><p>List of command line arguments (if applicable)</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.RunArgs.domain">
<code class="descname">domain</code><a class="headerlink" href="#acclient.RunArgs.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Command domain name</p>
</dd></dl>

<dl class="method">
<dt id="acclient.RunArgs.dump">
<code class="descname">dump</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#acclient.RunArgs.dump" title="Permalink to this definition">¶</a></dt>
<dd><p>Return run arguments dict</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">dict</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="attribute">
<dt id="acclient.RunArgs.loglevels">
<code class="descname">loglevels</code><a class="headerlink" href="#acclient.RunArgs.loglevels" title="Permalink to this definition">¶</a></dt>
<dd><p>Log levels to process</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.RunArgs.loglevels_ac">
<code class="descname">loglevels_ac</code><a class="headerlink" href="#acclient.RunArgs.loglevels_ac" title="Permalink to this definition">¶</a></dt>
<dd><p>Which log levels to report back to AC</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.RunArgs.loglevels_db">
<code class="descname">loglevels_db</code><a class="headerlink" href="#acclient.RunArgs.loglevels_db" title="Permalink to this definition">¶</a></dt>
<dd><p>Which log levels to store in agent DB</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.RunArgs.max_restart">
<code class="descname">max_restart</code><a class="headerlink" href="#acclient.RunArgs.max_restart" title="Permalink to this definition">¶</a></dt>
<dd><p>Max number of restarts before agent gives up</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.RunArgs.max_time">
<code class="descname">max_time</code><a class="headerlink" href="#acclient.RunArgs.max_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Max exection time.</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.RunArgs.name">
<code class="descname">name</code><a class="headerlink" href="#acclient.RunArgs.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Script or executable name. It’s totally up to the <code class="docutils literal"><span class="pre">cmd</span></code> to interpret this</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.RunArgs.queue">
<code class="descname">queue</code><a class="headerlink" href="#acclient.RunArgs.queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Which command queue to wait in (in case of serial exection)</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.RunArgs.recurring_period">
<code class="descname">recurring_period</code><a class="headerlink" href="#acclient.RunArgs.recurring_period" title="Permalink to this definition">¶</a></dt>
<dd><p>How often to run this job (in seconds)</p>
</dd></dl>

<dl class="attribute">
<dt id="acclient.RunArgs.stats_interval">
<code class="descname">stats_interval</code><a class="headerlink" href="#acclient.RunArgs.stats_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>How frequent the stats aggregation is done/flushed to AC</p>
</dd></dl>

<dl class="method">
<dt id="acclient.RunArgs.update">
<code class="descname">update</code><span class="sig-paren">(</span><em>args</em><span class="sig-paren">)</span><a class="headerlink" href="#acclient.RunArgs.update" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a new instance of run arguments with updated arguments</p>
<table class="docutils field-list" frame="void" rules="none">
<colgroup><col class="field-name">
<col class="field-body">
</colgroup><tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>args</strong> (<a class="reference internal" href="#acclient.RunArgs" title="acclient.RunArgs"><code class="xref py py-class docutils literal"><span class="pre">acclient.RunArgs</span></code></a> or <code class="xref py py-class docutils literal"><span class="pre">dict</span></code>) – overrides the current arguments with this set</td>
</tr>
<tr class="field-even field"><th class="field-name">Return type:</th><td class="field-body"><a class="reference internal" href="#acclient.RunArgs" title="acclient.RunArgs"><code class="xref py py-class docutils literal"><span class="pre">acclient.RunArgs</span></code></a></td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>