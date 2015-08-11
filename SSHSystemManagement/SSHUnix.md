
## SSH tools for generic Unix

### to init

```
c=j.ssh.connect("localhost",verbose=True) #this returns a cuisine object (like above) which is verbose in output, if you don't want that put on False
u=j.ssh.unix.get(c) #use the generic unix sal, feed it the cuisine connection

```

### to change passwd


```
u.changePasswd(self, passwd, login='recovery')
```
find
----

```
find(self,path,recursive=True,pattern="",findstatement="",type="",contentsearch="",extendinfo=False):

"""
@param findstatement can be used if you want to use your own find arguments
for help on find see http://www.gnu.org/software/findutils/manual/html_mono/find.html
@param pattern e.g. */config/j* 

    *   Matches any zero or more characters.
    ?   Matches any one character.
    [string] Matches exactly one character that is a member of the string string. 
        This is called a character class. As a shorthand, string may contain ranges, which consist of two characters with a dash between them. 
        For example, the class ‘[a-z0-9_]’ matches a lowercase letter, a number, or an underscore. 
        You can negate a class by placing a ‘!’ or ‘^’ immediately after the opening bracket. 
        Thus, ‘[^A-Z@]’ matches any character except an uppercase letter or an at sign.
    \ Removes the special meaning of the character that follows it. This works even in character classes. 

@param type

    b    block (buffered) special
    c    character (unbuffered) special
    d    directory
    p    named pipe (FIFO)
    f    regular file
    l    symbolic link

@param contentsearch
    looks for this content inside the files

@param extendinfo   : this will return [[$path,$sizeinkb,$epochmod]]

"""

### example

c=j.ssh.connect("localhost",verbose=True)
u=j.ssh.unix.get(c)

```
execute bash script
-------------------
```
def something(self):
    CMDS="""
        #make sure user is in sudo group
        usermod -a -G sudo recovery

        #sed -i -e '/texttofind/ s/texttoreplace/newvalue/' /path/to/file
        sed -i -e '/.*PermitRootLogin.*/ s/.*/PermitRootLogin without-password/' /etc/ssh/sshd_config
        sed -i -e '/.*UsePAM.*/ s/.*/UsePAM no/' /etc/ssh/sshd_config
        sed -i -e '/.*Protocol.*/ s/.*/Protocol 2/' /etc/ssh/sshd_config
    """
    c=j.ssh.connect("localhost",verbose=True)
    u=j.ssh.unix.executeBashScript(c)

```

### secure the remote environment

* actions
    * will set recovery passwd for user recovery
    * will create a recovery user account
    * will disable all other users to use ssh (so only user 'recovery' can login & do sudo -s)
    * will authorize key identified with sshkeypath
    * will do some tricks to secure sshdaemon e.g. no pam, no root access.
* locked down server where only the specified key can access and through the recovery created user


```
c=j.ssh.connect("localhost",verbose=True)
u=j.ssh.unix.secureSSH(self,sshkeypath,recoverypasswd=""):
    
```

### tmux

* executeRemoteTmuxCmd(cmd) #execute a cmd in tmux session
* executeRemoteTmuxJumpscript(script) #execute a jumpscript remote 
    * @param script is the content of the script

### other useful cmds

* changePasswd(passwd,login="recovery")
