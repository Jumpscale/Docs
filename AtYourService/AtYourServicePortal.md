## At Your Service Portal

AYS services and templates are visualized in space [AYS](http://localhost:82/AYS).


### Templates list

![Templates](AYS-Templates.png)

The Templates page lists all the templates available on your system as well as configuration templates as defined in /opt/jumpscale7/hrd/system/atyourservice.hrd

```
ays.1                          =
    name:'my_@ys',
    url:'https://git.aydo.com/racktivity/ays.git',

metadata.jumpscale             =
    branch:'master',
    url:'https://github.com/jumpscale7/ays_jumpscale7',

metadata.openvcloud            =
    url:'https://git.aydo.com/0-complexity/openvcloud_ays',

```

The prefix `ays` denotes configuration repos of installed services on another system.
The prefix `metadata` denotes domains of templates for local usage.


The templates are separated into "local" templates (further divided by template domain) and -in this example- "my_@ys" which further has two domains defined.

### Services list

![Services](AYS-Services.png)

The services page lists installed services on the system as well as those configured in the `atyourservice.hrd`.


This makes it easy to see what services are available where as well as how they've been configured.


To reload your services and templates at any point, the reload button will dump its database and reload everything from the freshly.

The details pages offer further information.
### Template details

![](Template-details.png)

The templates details page shows information pertinent to the template; such as its domain, name, metadata path, installed instances (which point to the detail page of those services) and a code editor to easily configure the template.

### Service details

![](Service-details.png)

The service details page shows information pertinent to the service.
It gives a link to the template used to install.

The code editors give a handy way to edit/configure services.

You can also perform actions on the services through the action links to start/stop/restart the services.

