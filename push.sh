#!/bin/bash

git add .

echo "Write a commit message: "
read answ
git commit -a -m "@answ"

echo "Branch to push: "
read branch
git push -u origin @branch
