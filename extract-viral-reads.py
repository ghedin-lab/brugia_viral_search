#!/usr/bin/python

import sys
from Bio import SeqIO

v = dict()

with open("kraken.translate.out", "rb") as kraken:
	for line in kraken:
		l = line.split("\t")
		if 'Viruses' in l[1] and 'phiX' not in l[1]:
			v[l[0]] = "v"
		else:
			v[l[0]] = "nv"

with open