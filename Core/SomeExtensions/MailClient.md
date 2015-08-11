E-Mail client
=============

JPackage
--------

This package is responsible for configuring the mail client

```shell
ays install -n mailclient
Mail server [smtp.googlemail.com]:
Mail port [587]:
Mail ssl
 (y/n):y
Mail username: mymail@gmail.com
Mail passwd: mypassword
```

Usage
-----

```python
import JumpScale.baselib.mailclient

j.clients.email.send(['receipient@gmail.com'], 'sender@gmail.com', 'my subject', 'My email body', ['/root/.hgrc', '/opt/jumpscale/apps/portalbase/wiki/TestWebsite/Automate.png'])
```

This will send an email to <receipient@gmail.com> from
<sender@gmail.com> having two attachments '/root/.hgrc' and
'/opt/jumpscale/apps/portalbase/wiki/TestWebsite/Automate.png'
