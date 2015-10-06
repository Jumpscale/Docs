# Example configuration

```toml
[main]
redis_host =  "127.0.0.1:6379"
redis_password = ""

#Default http
[[listen]]
  Address = ":8966"

#Example for https with multiple virtual hosts
[[listen]]
  Address = ":8443"
  [[listen.tls]]
    cert = "/path/to/domain1_certificate.cert"
    key = "/path/to/domain1_keyfile.key"
  [[listen.tls]]
    cert = "/path/to/domain2_certificate.cert"
    key = "/path/to/domain2_keyfile.key"
    
    
#Example for https with client certificates
[[listen]]
  Address = ":8445"
  [[listen.tls]]
    cert = "/path/to/domain1_certificate.cert"
    key = "/path/to/domain1_keyfile.key"
  [[listen.clientCA]]
    cert= "/path/to/CA1_certificate.cert"
  [[listen.clientCA]]
    cert= "/path/to/CA2_certificate.cert"

[influxdb]
host = "127.0.0.1:8086"
db   = "main"
user = "root"
password = "root"

[handlers]
binary = "python2.7"
cwd = "./handlers"
    [handlers.env]
    PYTHONPATH = "/opt/jumpscale7/lib"
    HOME = "/root"
    SYNCTHING_URL = "http://localhost:18384/"
    #SYNCTHING_API_KEY = ""
    REDIS_ADDRESS = "localhost"
    REDIS_PORT = "6379"
    #REDIS_PASSWORD = ""
```
## listen
The agencontroller can listen on multiple addresses. Specify a `[[listen]]` block for every address to listen on.

### tls
A `[[listen.tls]]` block enables HTTPS connections on the address supplied in the parent `[[listen]]` block.
On production environments this should always be configured.

* **cert** is the certificate file. 
If the certificate is signed by a CA, this certificate file should be a concatenation of the server's certificate followed by the CA's certificate.
* **key** is the server's private key file which matches the certificate file.


The cert and key files must contain PEM encoded data.

Multiple `[[listen.tls]]` blocks may be specified to allow multiple dns entries and corresponding certificates to be served from the same address.

### client certificates
If tls is enabled by specifying a `[[listen.tls]]` block, client certificates can be configured by adding `[[listen.clientCA]]` configurations. 
* **cert** is a CA certificate file.

Clients connecting to this endpoint will then be required to provide a client certificate. The certificate will be verified against the CA certificate. Multiple `[[listen.clientCA]]` blocks may be specified and a client certificate will be accepted if it is accepted by at least 1 of the CA's.
