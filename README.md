##
##VIBE

# Instructions
## For script "Auto_run.sh"

This script uses inotify-tools, so if its not installed 
on your machine, this script will not work as intended
- Run the script in tmux or somthing like it for best result
- The script will keep watch of the directory you're currently working in
- When anything is saved, moved to the directory and/or created, it will run the script: "Backup.sh"

## For script "Backup.sh"

This script will create several directories,
All of them inside your home directory, 
if you already have a 'backups' directory,
all that will happen is that new files will be appended:
(Files will look like this: "Nov-30-21_04:52")
 
- One directory named backups to store all the backups in
- Inside that, a directory with the same name as the directory you're currently working in
- Inside that, a directory with the name of the current month
- And finally, a directory with the month and the time the backup was created containing the 
	files in the current directory

## For "vibe.py"

This is the real homework. This file is made to add employees to a company.
It will create a new directory named "My_company", if you have such a directory,
it could mess things up

- You'll be prompted for a name, date of birth and a password
	(The password is only for an extra funciton, DO NOT ENTER YOUR REAL PASSWORD)
- It will create a tree of directories and files that will not affect the rest of the system

## For "push.sh"

This is only a automated push script for github 
