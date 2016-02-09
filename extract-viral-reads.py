#!/usr/bin/python

import sys
from Bio import SeqIO

v = dict()

with open("kraken.translate.out", "rb") as kraken:
	for line in kraken:
		l = line.split("\t")
		if 'Viruses' in l[1] and 'phiX' not in l[1]:
			v[l[0]] = "v"
			
with open("kraken.translate.out", "rb") as kraken:
	for line in kraken:
		l = line.split("\t")
		v[l[1]] = "u"
		

with open("all-unmapped.r1.fastq", "rb") as f:
	with open("all-unmapped.r1.viral.fastq", "w") as out:
		for record in SeqIO.parse(f, "fastq"):
			if record.id in v:
				out.write(record.format("fastq"))

with open("all-unmapped.r2.fastq", "rb") as f:
	with open("all-unmapped.r2.viral.fastq", "w") as out:
		for record in SeqIO.parse(f, "fastq"):
			if record.id in v:
				out.write(record.format("fastq"))