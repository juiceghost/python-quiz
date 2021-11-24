#!/bin/bash

ALL=*
CURRENT_DIR=${PWD##*/}
inotifywait -e close_write,moved_to,create -m `pwd` |
while read -r directory events filename; do
	for FILE in $ALL
	do
		if [ "$filename" = "$FILE" ];
		then
			./Backup.sh
		fi
	done
done
