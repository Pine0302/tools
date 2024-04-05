#!/bin/bash
kill -9 $(ps -ef|grep screenshot2word | grep -v grep | awk -F ' ' '{print $2}')
python /home/pine/workspace/pythontool/screenshot2word.py
