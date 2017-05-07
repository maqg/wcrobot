#!/bin/sh

PROCESS_NUM=`ps aux | grep CENTER | grep -v grep | awk '{print $2}'`
kill -9 ${PROCESS_NUM}

PROCESS_NUM=`ps aux | grep SERVER | grep -v grep | awk '{print $2}'`
kill -9 ${PROCESS_NUM}

nohup python3 ./CENTER.pyc 0.0.0.0 9000 &
nohup python3 ./SERVER.pyc 0.0.0.0 9010 &

