#!/bin/bash

PID_FILE=app.pid

if [ -e $PID_FILE ]; then
    kill -9 $(cat $PID_FILE)
    echo "Stop App"
else
    echo "App did not execute."
fi