#!/bin/sh

PROCESS_NUM=`ps aux | grep CENTER | grep -v grep | awk '{print $2}'`
kill -9 ${PROCESS_NUM}

nohup python3 ./CENTER.pyc 0.0.0.0 9000 &

