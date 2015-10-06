## Introduction
In an cloud architecture, we needs to make sure that the communication between the different services is secure.  
In order to do that, a common technique is to use TLS/SSL.  

JumpScale provide simple ways to deal with servcer and client certificate generation.

### CFSSL Service
The AYS service responsible of all the TLS infrastructure is [cfssl](https://github.com/Jumpscale/ays_jumpscale7/tree/master/_tools/cfsll).

to install simple do 
```
ays install -n cfssl --data 'instance.initca:True'
```
Note here, we tell cfsll service to generate a new Certificate Authority (CA) during the installation.
You can also install the service without generating a new CA.

Once you have this service installed, you can start creating your certificate. Jumpscale proving a extension that expose a simple interface.