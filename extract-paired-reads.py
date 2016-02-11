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
		if m.group(1) in segs:
			seqs[m.group(1)]["r2"] = record.format("fastq")
		else:
			seqs[m.group(1)] = dict()
			seqs[m.group(1)]["r2"] = record.format("fastq")
			seqs[m.group(1)]["r1"] = "None"
			

with open(sys.argv[3], "w") as r1, open(sys.argv[3], "w") as r2, open(sys.argv[3], "w") as se:
	for name in segs:
		if segs[name]["r1"] == "None":
			se.write(segs[name]["r1"])
		elif segs[name]["r2"] == "None":
			se.write(segs[name]["r2"])
		else:
			r1.write(segs[name]["r1"])
			r2.write(segs[name]["r2"])