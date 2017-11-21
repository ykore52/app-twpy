#!/bin/bash

python app.py &
PID=$!
echo $PID > app.pid

if [ $(ps -ef | grep $(cat app.pid) | wc -l) -ne 0 ]; then
    echo "Start App."
else
    echo "Fail"
fi