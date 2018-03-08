#!/bin/bash
ps -ef |grep authx |grep -v 'grep' |awk -F ' ' '{print $2}' |xargs kill -9
