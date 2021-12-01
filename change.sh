#!/bin/bash

scp -P 30042 -r /home/vibe/watchdir/* vibe@dev.kjeld.io:~/deiroowmi/
scp -P 30042 -r /home/vibe/watchdir/* vibe@dev.kjeld.io:~/src/programming/python-quiz/
./watch.sh
