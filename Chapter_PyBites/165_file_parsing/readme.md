# Bite 165. Parse an /etc/passwd file output

## Description 

The /etc/passwd file is a text-based database of information about users that may log into the system or other operating system user identities that own running processes. (Wikipedia).

In this Bite you complete the function get_users_for_shell that takes a /etc/passwd multiline string and a shell to filter on (default bash). Parse the output returning a list of usernames that match the shell.

So for this truncated /etc/passwd string:

avahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
postfix:x:108:112::/var/spool/postfix:/bin/false
ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash"""

. the resulting user list would be: ['artagnon', 'ssh-rsa']
Good luck and keep calm and code in Python!