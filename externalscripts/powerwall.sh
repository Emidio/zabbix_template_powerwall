#!/bin/bash
# use your venv path for python (changes in latest updates)
cd /usr/lib/zabbix/externalscripts
/var/www/scripts/venv/bin/python /usr/lib/zabbix/externalscripts/powerwall.py $1 $2 $3 $4|sed "s/'/\"/g"|sed 's/True/true/g'|sed 's/False/false/g'|sed ':a;$!{N;s/\n/ /;ba;}'
