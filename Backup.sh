#!/bin/bash

CURRENT_DIR=${PWD##*/}
MONTH=`date +%B`
DATE=`date +%b-%d-%y`
TIME=`date +%I:%M`
FILES=*
if [ ! -d ~/backups ]
then
	mkdir ~/backups
elif [ ! -d ~/backups/"$CURRENT_DIR" ]
then
	mkdir ~/backups/"$CURRENT_DIR"
elif [ ! -d ~/backups/"$CURRENT_DIR"/"$MONTH" ]
then
	mkdir ~/backups/"$CURRENT_DIR"/"$MONTH"
else
	echo "Directory already exists, updating backup files... "
fi
mkdir ~/backups/"$CURRENT_DIR"/"$MONTH"/"$DATE"_"$TIME"
for FILE in $FILES
do
	cp $FILE ~/backups/"$CURRENT_DIR"/"$MONTH"/"$DATE"_"$TIME"/"$FILE".ts
done

echo "Updating backup files..."
