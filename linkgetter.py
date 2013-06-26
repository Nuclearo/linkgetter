#! /usr/bin/env python
import os
import re

def makelink(link):
	return '<a href="'+link+'">'+link+'</a>'


files = [open(f) for f in os.listdir(".") if os.path.isfile(f) and ".log" in f]
out = open('links.html','w')
out.write('<html>\n<body>\n<h1>Link List:</h1><br>')
for f in files:
	contents = f.read()
	out.write('\n<h2>'+f.name+'</h2><br>')
	for s in re.findall("(http[s]?://[\S]*)",contents):
		out.write('\n'+makelink(s)+'<br>')
	f.close()
out.write('\n</body>\n</html>')
out.close()