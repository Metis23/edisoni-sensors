#!/bin/bash

#This script is called by crontab (server) every 5 minutes:
# */5 * * * *  /usr/local/bin/rrdtranslate.sh
#photocell.xml is a translation of Edisoni's photocell.rrd file. Server cannot
#use Edisoni's .rrd because Edisoni is 32-bit.  Edisoni dumps it rrd into
#an .xml file every 5 minutes.  Edisoni home directory is mounted
# on server by: #sshfs root@192.168.1.20:/home/edisoni/ edroot
#The following command converts the .xml into an .rrd file that the server can use.
scp root@192.168.1.20:/home/root/edisoni-sensors/photocell.xml /home/edisoni
sleep 1
rrdtool restore -f /home/edisoni/photocell.xml /var/log/photocell2.rrd
