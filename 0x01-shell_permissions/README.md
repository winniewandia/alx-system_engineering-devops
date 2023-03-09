"su betty" script that switches the current user to the user betty
"whoami" prints the effective username of the current user.
"groups" prints all the groups the current user is part of
"sudo chown betty hello" changes the owner of the file hello to the user betty
"touch hello" creates an empty file hello
"chmod 744 hello" adds execute permission to the owner of the file hello
"chmod 754 hello" adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
"chmod a+x hello" adds execution permission to the owner, the group owner and the other users, to the file hello
"chmod 007 hello" sets the permission to the file hello as follows:

Owner: no permission at all
Group: no permission at all
Other users: all the permissions
"chmod 753 hello" sets the mode of hello to -rwxr-x-wx