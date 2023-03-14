"alias ls="rm *"" creates an alias.

Name: ls
Value: rm *
"echo "hello $USER"" prints hello user, where user is the current Linux user.
"PATH=$PATH:/action" Add /action to the PATH. 
"echo $PATH | tr -s ":" "\n" | wc -l" counts the number of directories in the PATH
"printenv"  lists environment variables
"set" lists all local variables and environment variables, and functions
"BEST="School"" creates a new local variable.

Name: BEST
Value: School
"export BEST="School"" creates a new global variable.

Name: BEST
Value: School
"echo "$((128+$TRUEKNOWLEDGE))"" prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line"
"echo "$POWER/$DIVIDE"" rints the result of POWER divided by DIVIDE, followed by a new line.

POWER and DIVIDE are environment variables

