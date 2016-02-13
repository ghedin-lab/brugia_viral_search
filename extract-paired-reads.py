#!/usr/bin/python

from Bio import SeqIO
import sys
import re

seqs = dict()

with open(sys.argv[1],"rb") as r1:
	for record in SeqIO.parse(r1,'fastq'):
		m = re.search('(^.+)/1', record.id)
		seqs[m.group(1)] = dict()
		seqs[m.group(1)]["r1"] = record.format("fastq")
		seqs[m.group(1)]["r2"] = "None"

with open(sys.argv[2],"rb") as r2:
	for record in SeqIO.parse(r2,'fastq'):
		m = re.search('(^.+)/2', record.id)
		if m.group(1) in seqs:
			seqs[m.group(1)]["r2"] = record.format("fastq")
		else:
			seqs[m.group(1)] = dict()
			seqs[m.group(1)]["r2"] = record.format("fastq")
			seqs[m.group(1)]["r1"] = "None"
			

with open(sys.argv[3], "w") as r1, open(sys.argv[4], "w") as r2, open(sys.argv[5], "w") as se:
	for name in seqs:
		if seqs[name]["r1"] == "None":
			se.write(seqs[name]["r1"])
		elif seqs[name]["r2"] == "None":
			se.write(seqs[name]["r2"])
		else:
			r1.write(seqs[name]["r1"])
			r2.write(seqs[name]["r2"])
