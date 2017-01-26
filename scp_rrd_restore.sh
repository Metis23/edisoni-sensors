#!/bin/bash

#This script is called by crontab (server) every 5 minutes:
# */5 * * * *  /usr/local/bin/scp_rrd_restore.sh
#photocell.xml is a translation of Edisoni's photocell.rrd file created
#by the edison. The server cannot use Edisoni's .rrd because Edisoni uses
#a different architecture.  Edisoni dumps it's the rrd database into
#an .xml file every 5 minutes. The server then copies the .xml file
#from the Edison to the server with this line:

scp root@192.168.1.20:/home/root/edisoni-sensors/photocell.xml /home/edisoni
sleep 1

#The following command converts the .xml into an .rrd file that the server can use. This .rrd will be called from the cgi script to make charts of the data.
rrdtool restore -f /home/edisoni/photocell.xml /var/log/photocell2.rrd
