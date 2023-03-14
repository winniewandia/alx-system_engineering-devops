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
"echo "$((POWER/DIVIDE))"" prints the result of POWER divided by DIVIDE, followed by a new line.

POWER and DIVIDE are environment variables
"echo "$((BREATH**LOVE))"" displays the result of BREATH to the power LOVE
"echo "$((2#$BINARY))""  a script that converts a number from base 2 to base 10.

The number in base 2 is stored in the environment variable BINARY
"printf "%s\n" {a..z}{a..z} | grep -v "oo"" a script that prints all possible combinations of two letters, except oo.

Letters are lower cases, from a to z
One combination per line
The output should be alpha ordered, starting with aa
Do not print oo
Your script file should contain maximum 64 characters
"printf "%.2f\n" $NUM" prints a number with two decimal places, followed by a new line.

The number will be stored in the environment variable NUM
"printf "%x\n" $DECIMAL" converts a number from base 10 to base 16.

The number in base 10 is stored in the environment variable DECIMAL
"tr '[A-Za-z]' '[N-ZA-Mn-za-m]'" a script that encodes and decodes text using the rot13 encryption. Assume ASCII
"paste - - | cut -f 1" prints every other line from the input, starting with the first line
printf "%o\n" $((5#$(echo $WATER | tr 'water' '01234') + 5#$(echo $STIR | tr 'stir.' '01234'))) | tr '01234567' 'bestchol' - script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.

WATER is in base water
STIR is in base stir.
The result should be in base bestchol

