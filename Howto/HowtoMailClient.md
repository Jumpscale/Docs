## Send Mail


### install
```
ays install -n mailclient
```
will ask for appropriate info about mail server

### cmd
```
j.clients.email.send(self, recipients, sender, subject, message, files=None, mimetype=None)
Docstring:
@param recipients: Recipients of the message
@type recipients: mixed, string or list
@param sender: Sender of the email
@type sender: string
@param subject: Subject of the email
@type subject: string
@param message: Body of the email
@type message: string
@param files: List of paths to files to attach
@type files: list of strings
@param mimetype: Type of the body plain, html or None for autodetection
@type mimetype: string
```

### example
```
import JumpScale.baselib.mailclient
j.clients.email.send("kristof@incubaid.com","kristof@incubaid.com","test","test")
```
