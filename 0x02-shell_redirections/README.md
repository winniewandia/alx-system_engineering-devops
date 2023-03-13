"echo "Hello, World"" prints “Hello, World”, followed by a new line to the standard output
"echo \"\(Ôo\)\'"  a script that displays a confused smiley "(Ôo)'
"cat /etc/passwd" Display the content of the /etc/passwd file
"cat /etc/passwd /etc/hosts" Display the content of /etc/passwd and /etc/hosts
"cat /etc/passwd | tail" Display the last 10 lines of /etc/passwd
"cat /etc/passwd | head" Display the first 10 lines of /etc/passwd
"cat iacta | head -n 3 | tail -n 1" Write a script that displays the third line of the file iacta
"echo "Best School" > '\*\\'\''"Best School"\'\''\\*$\?\*\*\*\*\*:)'" creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
"ls -la > ls_cwd_content" writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it
"tail -n 1 iacta >> iacta" duplicates the last line of the file iacta
"find -name "*.js" -type f -delete" deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
"find -mindepth 1 -type d | wc -l"  script that counts the number of directories and sub-directories in the current directory
"ls -1t | head" a script that displays the 10 newest files in the current directory. One file per line
Sorted from the newest to the oldest
"sort | uniq -u" takes a list of words as input and prints only words that appear exactly once.Words should be sorted
"grep root /etc/passwd" Display lines containing the pattern “root” from the file /etc/passwd
"grep -c bin /etc/passwd" Display the number of lines that contain the pattern “bin” in the file /etc/passwd
"grep root /etc/passwd -A 3" Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
"grep -v bin /etc/passwd" Display all the lines in the file /etc/passwd that do not contain the pattern “bin"
"grep '^[[:alpha:]]' /etc/ssh/sshd_config" Display all lines of the file /etc/ssh/sshd_config starting with a letter.

include capital letters as well


