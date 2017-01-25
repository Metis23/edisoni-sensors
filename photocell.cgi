#!/usr/bin/rrdcgi
<!--This file is called from index.html with the following line:
<li class="w3-hide-small"><a href="/cgi-bin/photocell.cgi" class="w3-hover-white">Photocell Chart</a></li>-->
<html>
<head>
<title>photocell2</title>
</head>
<body>
<h1>photocell</h1>
<h2>Light Intensity 24 Hours Past </h2>
<p>

<RRD::GRAPH /var/www/html/photocell/daily-intensity.png
	--imginfo '<img src=/photocell/%s width=%lu height=%lu>'
	-a PNG	
	-h 250 -w 800
	--lazy
	-v "Photocell (V)"
	-t "Photocell Voltage Reading"
	-x 'HOUR:1:HOUR:3:HOUR:3:0:%b %d %H:00'
	-s -1d -l 0
	DEF:intensity=/var/log/photocell2.rrd:photocell:AVERAGE
	LINE1:intensity#edd628:"photocell">
</p>
<h2>Light Intensity 1 Week Past </h2>
<p>
<RRD::GRAPH /var/www/html/photocell/weekly-intensity.png
	--imginfo '<img src=/photocell/%s width=%lu height=%lu>'
	-a PNG	
	-h 250 -w 800
	--lazy
	-v "Photocell (V)"
	-t "Photocell Voltage Reading"
	-x 'HOUR:6:DAY:1:DAY:1:86400:%a %b %d'
	-s -1w -l 0
	DEF:intensity=/var/log/photocell2.rrd:photocell:AVERAGE
	LINE1:intensity#edd628:"photocell">
</p>
</body>
</html>
