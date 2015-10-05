# Example configuration

```toml
[main]
listen = ":8966"
redis_host =  "127.0.0.1:6379"
redis_password = ""

[tls]
#If specified, enable ssl
#cert = "/path/to/certificate.cert"
#key = "/path/to/keyfile.key"

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

### tls
Enables HTTPS connections, plain text HTTP is no longer supported from then on.
On production environments this should always be configured.
* **cert** is the certificate file. 
If the certificate is signed by a CA, this certificate file should be a concatenation of the server's certificate followed by the CA's certificate.
* **key** is the server's private key file which matches the certificate file.

