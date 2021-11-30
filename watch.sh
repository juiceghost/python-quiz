#!/bin/bash

ALL=*
inotifywait -e close_write,moved_to,create `pwd` |
while read -r directory events filename; do
	for FILE in $ALL; do
		if [ "$filename" = "$FILE" ]; then
			./change.sh
		fi
	done
done
