#!/bin/bash
#PBS -l walltime=72:00:00,nodes=1:ppn=12,mem=32gb
#PBS -m e
#PBS -M twaddlac@gmail.com
#PBS -j oe


module load tophat/intel/2.0.12
module load bowtie2
#module switch samtools/intel/0.1.19 samtools/intel/1.2

#change path to where the fastq files are
cd $path
# tophat command was taken from /scratch/at120/shared/alex/2015-07-24_H55MKBCXX/Replicate_Data/am-new-tophat-out/accepted_hits.bam
# /scratch/at120/shared/alex/2015-07-24_H55MKBCXX/Replicate_Data/brugia_wolbachia_v4.gff3

tophat2 --b2-very-sensitive -o $fastq-tophat-out -p 12 -r 50 --mate-std-dev 100 -G /scratch/at120/shared/db/organism/brugia/b_malayi.PRJNA10729.WS252.annotations.gff3 /scratch/at120/shared/db/organism/brugia/b_malayi.PRJNA10729.WS252.genomic_masked $fastq.r1.fastq $fastq.r2.fastq


