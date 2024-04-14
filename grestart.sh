#!/bin/bash
kill -9 $(ps -ef|grep getOcrFromRemote | grep -v grep | awk -F ' ' '{print $2}')
python /home/pine/workspace/pythontool/getOcrFromRemote.py
