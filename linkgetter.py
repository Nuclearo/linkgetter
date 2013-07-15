#! /usr/bin/env python
import os
import sys
import re
import webbrowser

def makelink(link):
	if link.endswith('%5C') or link.endswith('%5c'):
		link = link[:-3]
	elif link.endswith('\\'):
		link = link[:-1]
	return '<a href="'+link+'">'+link+'</a>'

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
if(".app/Contents" in os.path.abspath(sys.argv[0])):
	os.chdir("../../..")
files = [f for f in os.listdir(".") if os.path.isfile(f) and ".log" in f]
out = open('links.html','w')
out.write('<html>\n<body>\n<h1>Link List:</h1>')
for filename in files:
	f=open(filename)
	contents = f.read()
	out.write('\n<h2>'+f.name+'</h2>')
	for s in re.findall("(http[s]?://[\S]*)",contents):
		out.write('\n'+makelink(s)+'<br>')
	f.close()
out.write('\n</body>\n</html>')
out.close()

webbrowser.open("file://"+os.path.realpath('links.html'))
