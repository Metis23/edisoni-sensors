#!/bin/bash
#script to load data into rrd archive on edison.
python /home/root/edisoni-sensors/photocell-rrd-update.py
sleep 5
rrdtool dump /home/root/edisoni-sensors/photocell.rrd /home/root/edisoni-sensors/photocell.xml
