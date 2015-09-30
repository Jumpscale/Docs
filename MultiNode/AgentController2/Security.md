

> Currently generating and using client certificates is not automated. So the page will requires some manual intervention from you to get things working.

# Introduction
To secure the controller/agent communication, the agent was built with SSL client certificate support. So to make sure you have a secure setup. the Agent Controller must run behind an SSL protected proxy that only allows clients with valid certificates, and the agent must be configured to use the correct certificate which is accepted by the proxy.

We will use `nginx` as the `ssl` proxy, in this walk through. So make sure it's installed or install it as
```bash
ays install -n nginx
```

# Generating the certificates.
Under agent2 repo, there is tools folder with 2 scripts to help you generating a self signed keys for testing.

- Run servercerts.sh to generate a self signed server certificate and key. Answer the questions as seems appropriate.

```bash
./servercerts.sh 

Generating server key...
Generating RSA private key, 2048 bit long modulus
.....+++
......................+++
e is 65537 (0x10001)
Generating server certificate signing request...
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:EG
State or Province Name (full name) [Some-State]:Cairo
Locality Name (eg, city) []:Cairo
Organization Name (eg, company) [Internet Widgits Pty Ltd]:codescalers
Organizational Unit Name (eg, section) []:cloudvaders
Common Name (e.g. server FQDN or YOUR name) []:localhost
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
Self signing the certificate
Signature ok
subject=/C=EG/ST=Cairo/L=Cairo/O=codescalers/OU=cloudvaders/CN=localhost
Getting Private key
Please manually install the server.key and server.crt in nginx
```

Now generate the client keys as following
```bash
./clientcerts.sh server.key server.crt testagent
Generating client key...
Generating RSA private key, 2048 bit long modulus
.........................................................................................................................................+++
.+++
e is 65537 (0x10001)
Gernerating client certificate signing request...
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:EG
State or Province Name (full name) [Some-State]:Cairo
Locality Name (eg, city) []:Cairo
Organization Name (eg, company) [Internet Widgits Pty Ltd]:codescalers
Organizational Unit Name (eg, section) []:cloudvaders
Common Name (e.g. server FQDN or YOUR name) []:testagent
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
Signing client certificate, with server certificate
Signature ok
subject=/C=EG/ST=Cairo/L=Cairo/O=codescalers/OU=cloudvaders/CN=testagent
Getting CA Private Key
```
> You can generate more client certificate by giving different agent name on the command line. agent name can be anything and is just used to name the generate client `key` and `crt` files.

now the current folder should have the following files
* server.key
* server.crt
* client-testagent.key
* client-testagent.crt

# Setting up nginx
Add this `server` section to nginx configuration

```nginx
server {
        listen       443 ssl;
        server_name  localhost;
        ssl on;
        ssl_certificate     /path/to/generated/server.crt;
        ssl_certificate_key /path/to/generated/server.key;
        ssl_client_certificate /path/to/generated/server.crt;
        ssl_verify_client on;
        #access_log  logs/host.access.log  main;

        location /controller/ {
                proxy_pass http://localhost:8966/;
                # the proxy read timeout must be set to a value bigger than the long poll timeout (of 60s)
                # other wise agent will start getting Bad Gateway errors.
                proxy_read_timeout 300s;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
        }
}
```
> Make sure to restart nginx after updating its configuration and that it started without error.

# Configuring the agent.
Now open `agent2.toml` file (located under `/opt/jumpscale7/apps/agent2`) and change the following:
* change `main.agent_controllers` to `["https://localhost/controller/"]
* set `security.client_certificate` to `/path/to/generated/client-testagent.crt`
* set `security.client_certificate_key` to `/path/to/generated/client-testagent.key`
* set `security.certificate_authority` to `/path/to/generated/server.crt` (This is only needed because we are using a self-signed certificate so we all telling the agent to trust this certificate, if this is not set agent will refuse to connect to the controller because it doesn't provide a trusted certificate)

Then restart the agent.

