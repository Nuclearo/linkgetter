#! /usr/bin/env python
import os
import sys
import re
import webbrowser
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter


os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
if(".app/Contents" in os.path.abspath(sys.argv[0])):
	os.chdir("../../..")
files = [f for f in os.listdir(".") if os.path.isfile(f) and ".rtf" in f]
out = open('links.html','w')
out.write('<html>\n<body>\n<h1>Link List:</h1>')
for filename in files:
	f=open(filename, "rb")
	contents = PlaintextWriter.write(Rtf15Reader.read(f)).getvalue()
	out.write('\n<h2>'+f.name+'</h2>')
	for link in re.findall(r"(?i)(http[s]?://\S+?)(?:\\|%5C)?(?:\s|$)",contents):
		out.write('\n<a href="'+link+'">'+link+'</a><br>')
	f.close()
out.write('\n</body>\n</html>')
out.close()

webbrowser.open("file://"+os.path.realpath('links.html'))
