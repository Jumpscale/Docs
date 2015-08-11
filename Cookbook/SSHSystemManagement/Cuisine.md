
cuisine getting started
=======================

'cuisine` makes it easy to write automatic server installation
and configuration recipes by wrapping common administrative tasks
(installing packages, creating users and groups) in Python
functions.

`cuisine` is designed to work with Fabric and provide all you
need for getting your new server up and running in minutes.

Note, that right now, Cuisine only supports Debian-based Linux
systems fully, others might work or not.


```
# -----------------------------------------------------------------------------
# Project   : Cuisine - Functions to write Fabric recipes
# -----------------------------------------------------------------------------
# License   : Revised BSD License
# -----------------------------------------------------------------------------
# Authors   : Sebastien Pierre                            <sebastien@ffctn.com>
#             Thierry Stiegler   (gentoo port)     <thierry.stiegler@gmail.com>
#             Jim McCoy (distro checks and rpm port)      <jim.mccoy@gmail.com>
#             Warren Moore (zypper package)               <warren@wamonite.com>
#             Lorenzo Bivens (pkgin package)          <lorenzobivens@gmail.com>
```

RUN
---

```
def run(command, shell=True, pty=True, combine_stderr=None):
    """
    """
```

FILE OPERATIONS
---------------

```

def file_local_read(location):
    """Reads a *local* file from the given location, expanding '~' and
    shell variables."""


def file_backup(location, suffix=".orig", once=False):
    """Backups the file at the given location in the same directory, appending
    the given suffix. If `once` is True, then the backup will be skipped if
    there is already a backup file."""

def file_read(location, default=None):
    """Reads the *remote* file at the given location, if default is not `None`,
    default will be returned if the file does not exist."""

def file_exists(location):
    """Tests if there is a *remote* file at the given location."""

def file_is_file(location):

def file_is_dir(location):

def file_is_link(location):


def file_attribs(location, mode=None, owner=None, group=None):
    """Updates the mode/owner/group for the remote file at the given
    location."""

def file_attribs_get(location):
    """Return mode, owner, and group for remote path.
    Return mode, owner, and group if remote path exists, 'None'
    otherwise.
    """

def file_write(location, content, mode=None, owner=None, group=None, sudo=None, check=True, scp=False):
    """Writes the given content to the file at the given remote
    location, optionally setting mode/owner/group."""
    # FIXME: Big files are never transferred properly!


def file_ensure(location, mode=None, owner=None, group=None, scp=False):
    """Updates the mode/owner/group for the remote file at the given
    location."""


def file_upload(remote, local, sudo=None, scp=False):
    """Uploads the local file to the remote location only if the remote location does not
    exists or the content are different."""
    # FIXME: Big files are never transferred properly!


def file_update(location, updater=lambda x: x):
    """Updates the content of the given by passing the existing
    content of the remote file at the given location to the 'updater'
    function. Return true if file content was changed.

    For instance, if you'd like to convert an existing file to all
    uppercase, simply do:

    >   file_update("/etc/myfile", lambda _:_.upper())

    Or restart service on config change:

    >   if file_update("/etc/myfile.cfg", lambda _: text_ensure_line(_, line)): run("service restart")
    """


def file_append(location, content, mode=None, owner=None, group=None):
    """Appends the given content to the remote file at the given
    location, optionally updating its mode/owner/group."""

def file_unlink(path):

def file_link(source, destination, symbolic=True, mode=None, owner=None, group=None):
    """Creates a (symbolic) link between source and destination on the remote host,
    optionally setting its mode/owner/group."""


def file_base64(location):
    """Returns the base64-encoded content of the file at the given location."""


def file_sha256(location):
    """Returns the SHA-256 sum (as a hex string) for the remote file at the given location."""


def file_md5(location):
    """Returns the MD5 sum (as a hex string) for the remote file at the given location."""

```

PROCESS OPERATIONS
-------------------

```
def process_find(name, exact=False):
    """Returns the pids of processes with the given name. If exact is `False`
    it will return the list of all processes that start with the given
    `name`."""

def process_kill(name, signal=9, exact=False):
    """Kills the given processes with the given name. If exact is `False`
    it will return the list of all processes that start with the given
    `name`."""
```

DIRECTORY OPERATIONS
--------------------

```
def dir_attribs(location, mode=None, owner=None, group=None, recursive=False):
    """Updates the mode/owner/group for the given remote directory."""

def dir_exists(location):
    """Tells if there is a remote directory at the given location."""

def dir_remove(location, recursive=True):
    """ Removes a directory """

def dir_ensure(location, recursive=False, mode=None, owner=None, group=None):
    """Ensures that there is a remote directory at the given location,
    optionally updating its mode/owner/group.

    If we are not updating the owner/group then this can be done as a single
    ssh call, so use that method, otherwise set owner/group after creation."""

```

PACKAGE OPERATIONS
------------------

```
def package_upgrade(distupgrade=False):
    """Updates every package present on the system."""

def package_update(package=None):
    """Updates the package database (when no argument) or update the package
    or list of packages given as argument."""

def package_install(package, update=False):
    """Installs the given package/list of package, optionally updating
    the package database."""

def package_ensure(package, update=False):
    """Tests if the given package is installed, and installs it in
    case it's not already there. If `update` is true, then the
    package will be updated if it already exists."""

def package_clean(package=None):
    """Clean the repository for un-needed files."""

def package_remove(package, autoclean=False):
    """Remove package and optionally clean unused packages"""
```


SHELL COMMANDS
---------------

```
def command_check(command):
    """Tests if the given command is available on the system."""

def command_ensure(command, package=None):
    """Ensures that the given command is present, if not installs the
```

USER OPERATIONS
---------------
```
def user_passwd(name, passwd, encrypted_passwd=True):
    """Sets the given user password. Password is expected to be encrypted by default."""


def user_create(name, passwd=None, home=None, uid=None, gid=None, shell=None,
    uid_min=None, uid_max=None, encrypted_passwd=True, fullname=None, createhome=True):
    """Creates the user with the given name, optionally giving a


def user_check(name=None, uid=None, need_passwd=True):
    """Checks if there is a user defined with the given name,
    returning its information as a
    '{"name":<str>,"uid":<str>,"gid":<str>,"home":<str>,"shell":<str>}'
    or 'None' if the user does not exists.
    need_passwd (Boolean) indicates if password to be included in result or not.
        If set to True it parses 'getent shadow' and needs sudo access
    """


def user_ensure(name, passwd=None, home=None, uid=None, gid=None, shell=None, fullname=None, encrypted_passwd=True):
    """Ensures that the given users exists, optionally updating their
    passwd/home/uid/gid/shell."""


def user_remove(name, rmhome=None):
    """Removes the user with the given name, optionally
    removing the home directory and mail spool."""
```

GROUP OPERATIONS
----------------

```
def group_create(name, gid=None):
    """Creates a group with the given name, and optionally given gid."""


def group_check(name):
    """Checks if there is a group defined with the given name,
    returning its information as a
    '{"name":<str>,"gid":<str>,"members":<list[str]>}' or 'None' if
    the group does not exists."""


def group_ensure(name, gid=None):
    """Ensures that the group with the given name (and optional gid)
    exists."""


def group_user_check(group, user):
    """Checks if the given user is a member of the given group. It
    will return 'False' if the group does not exist."""


def group_user_add(group, user):
    """Adds the given user/list of users to the given group/groups."""


def group_user_ensure(group, user):
    """Ensure that a given user is a member of a given group."""


def group_user_del(group, user):
    """remove the given user from the given group."""


def group_remove(group=None, wipe=False):
    """ Removes the given group, this implies to take members out the group
    if there are any.  If wipe=True and the group is a primary one,
    deletes its user as well.
    """
```

SSH
---
```
def ssh_keygen(user, keytype="dsa"):
    """Generates a pair of ssh keys in the user's home .ssh directory."""

def ssh_authorize(user, key):
    """Adds the given key to the '.ssh/authorized_keys' for the given
    user."""

def ssh_unauthorize(user, key):
    """Removes the given key to the remote '.ssh/authorized_keys' for the given
    user."""
```

UPSTART
-------

```
def upstart_ensure(name):
    """Ensures that the given upstart service is running, starting
    it if necessary."""

def upstart_reload(name):
    """Reloads the given service, or starts it if it is not running."""

def upstart_restart(name):
    """Tries a `restart` command to the given service, if not successful

def upstart_stop(name):
    """Ensures that the given upstart service is stopped."""
```

SYSTEM
------

```
def system_uuid_alias_add():
    """Adds system UUID alias to /etc/hosts.
    Some tools/processes rely/want the hostname as an alias in
    /etc/hosts e.g. `127.0.0.1 localhost <hostname>`.
    """

def system_uuid():
    """Gets a machines UUID (Universally Unique Identifier)."""
```

RSYNC
-----

```
def rsync(local_path, remote_path, compress=True, progress=False, verbose=True, owner=None, group=None):
    """Rsyncs local to remote, using the connection's host and user."""
```

LOCALE
------

```
def locale_check(locale):

def locale_ensure(locale):

```

modes
-----

```
def sudo_password(password=None):
    """Sets the password for the sudo command."""


class mode_local(__mode_switcher):
    """Sets Cuisine into local mode, where run/sudo won't go through
    Fabric's API, but directly through a popen. This allows you to
    easily test your Cuisine scripts without using Fabric."""
    MODE_KEY   = MODE_LOCAL
    MODE_VALUE = True

class mode_remote(__mode_switcher):
    """Comes back to Fabric's API for run/sudo. This basically reverts
    the effect of calling `mode_local()`."""
    MODE_KEY   = MODE_LOCAL
    MODE_VALUE = False

class mode_user(__mode_switcher):
    """Cuisine functions will be executed as the current user."""
    MODE_KEY   = MODE_SUDO
    MODE_VALUE = False

class mode_sudo(__mode_switcher):
    """Cuisine functions will be executed with sudo."""
    MODE_KEY   = MODE_SUDO
    MODE_VALUE = True

def mode(key):
    """Queries the given Cuisine mode (ie. MODE_LOCAL, MODE_SUDO)"""

def is_local():  return mode(MODE_LOCAL)
def is_remote(): return not mode(MODE_LOCAL)
def is_sudo():   return mode(MODE_SUDO)

def shell_safe( path ):
    """Makes sure that the given path/string is escaped and safe for shell"""
```

options
--------

```
def select_package( selection=None ):
    """Selects the type of package subsystem to use (ex:apt, yum, zypper, pacman, or emerge)."""

def select_python_package( selection=None ):

def select_user( selection=None ):

def select_group( selection=None ):

def select_os_flavour( selection=None ):

def options():
    """Retrieves the list of options as a dictionary."""
```
