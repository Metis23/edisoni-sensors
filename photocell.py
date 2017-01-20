#!/usr/bin/python

# env is a command that manages the environment.
# it's probably not setup on edison, so use the explicit path  
#!/usr/bin/env python  

#These are dependencies  
import mraa  
import time
import datetime
import sys

#Pin A0 receives photocell
pcell_pin=0
pcell_value=0
x=0

photocell = mraa.Aio(pcell_pin)  
  
print "Photocell Data Stream.  Use Ctrl-C to exit."
target = open("pcell_data", 'w')
while x < 200:

    #read photocell value, write to file
    pcell_value=float(photocell.read())
    s = str(pcell_value)
    target.write(now, s)
    target.write("\n")
    time.sleep(0.9)
    x = x + 1
    print  "Now: ", now, "photocell value: ", pcell_value

    
target.close()
