#!/usr/bin/python

import sys

with open(sys.argv[1], "rb") as r1, open(sys.argv[2],"rb") as r2:
	while(True):
		line = r1.readline()
		if line.strip() == "":
			break
		print line.strip()
		print r1.readline().strip()
		
		for i in xrange(2):
			r1.readline().strip()
		
		
		for i in xrange(2):
			print r2.readline().strip()
			
		for i in xrange(2):
			r2.readline().strip()