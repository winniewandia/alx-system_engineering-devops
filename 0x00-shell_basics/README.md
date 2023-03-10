"pwd" prints the absolute path name of the current working directory
"ls" display the contents list of your current directory
"cd" changes the working directory to the user’s home directory
"ls -l" Display current directory contents in a long format
"ls -la" Display current directory contents, including hidden files and in long format
"ls -lan" Display current directory contents in Long format with user and group IDs displayed numerically And hidden files
"mkdir /tmp/my_first_directory"  a script that creates a directory named my_first_directory in the /tmp/ directory
"mv /tmp/betty /tmp/my_first_directory" Move the file betty from /tmp/ to /tmp/my_first_directory
"rm /tmp/my_first_directory/betty" Delete the file betty
"rmdir /tmp/my_first_directory" Delete empty directory
"cd -" changes the working directory to the previous one
"ls -la . .. /boot" lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format
"file /tmp/iamafile" prints the type of the file named iamafile
"ln -s /bin/ls __ls__" a symbolic link to /bin/ls, named __ls__
"cp -u *.html .." copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory
"mv [[:upper:]]* /tmp/u" moves all files beginning with an uppercase letter to the directory
"rm *~" deletes all files in the current working directory that end with the character ~
"mkdir -p ./welcome/to/school" creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
"ls -xamp" a command that lists all the files and directories of the current directory, separated by commas (,).

Directory names should end with a slash (/)
Files and directories starting with a dot (.) should be listed
The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
Only digits and letters are used to sort; Digits should come first
You can assume that all the files we will test with will have at least one letter or one digit
The listing should end with a new line
"0 string SCHOOL School data
!:mime School" a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.


