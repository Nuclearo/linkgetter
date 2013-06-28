#! /usr/bin/env python
import os
import re

def makelink(link):
	return '<a href="'+link+'">'+link+'</a>'

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
os.chdir("../../..")
files = [open(f) for f in os.listdir(".") if os.path.isfile(f) and ".log" in f]
out = open('links.html','w')
out.write('<html>\n<body>\n<h1>Link List:</h1>')
for f in files:
	contents = f.read()
	out.write('\n<h2>'+f.name+'</h2>')
	for s in re.findall("http[s]?://[\S]*",contents):
		if re.s
		out.write('\n'+makelink(s)+'<br>')
	f.close()
out.write('\n</body>\n</html>')
out.close()