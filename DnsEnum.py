#!usr/bin/python

import socket
import sys

search = open('bin/list/dnsenum-list.txt', 'r')

for line in search:
	line = line.strip('\n')
	prep = line
	DNS = prep + "." + sys.argv[1]
	try:
		print(DNS + ": " + socket.gethostbyname(DNS))
	except socket.gaierror:
		pass
search.close()
