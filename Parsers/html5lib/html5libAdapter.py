from contextlib import closing
from urllib2 import urlopen
import sys
from html5lib import html5parser
import html5lib

def convert(stripChars):
    def convertData(data):
        """convert the output of str(document) to the format used in the testcases"""
        data = data.split("\n")
        rv = []
        for line in data:
            if line.startswith("|"):
                rv.append("|"+line[stripChars:])
            else:
                rv.append(line)
        return "\n".join(rv)
    return convertData

def convertTreeDump(data):
	return "\n".join(convert(2)(data).split("\n")[1:])

#def format(data):
#	a = []
#	a = data.split("\n")
#	b = []
	
#	for line in a:
#		if line[0] == "|":
#			line = "| "+line[1:]
#			b.append(line)
	
#	return "\n".join(b)
import codecs

p = html5parser.HTMLParser(tree=html5lib.getTreeBuilder("dom"), namespaceHTMLElements=False)

if len(sys.argv) == 3:
	if sys.argv[1] == '-f':		
		fp = codecs.open(sys.argv[2], 'rb', 'utf-8')
		document = p.parse(fp.read())
	if sys.argv[1] == '-s':
		document = p.parse(sys.argv[2])
	if sys.argv[1] == '-u':
		with closing(urlopen(sys.argv[2])) as f:
			document = p.parse(f)
	output = p.tree.testSerializer(document)
	
	print convertTreeDump(output.encode('utf-8'))
	
	

	
	

