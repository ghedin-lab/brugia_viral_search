#!/bin/bash
#PBS -l nodes=1:ppn=20,mem=62gb,walltime=72:00:00
#PBS -j oe
#PBS -M twaddlac@gmail.com
#PBS -m ae
#PBS -N all-idba

module load idba

cd $path

idba_id --pre_correction --num_threads 20 -l $fasta -o $fasta.idba.d

cd $fasta.idba.d

blastn -db /scratch/at120/shared/db/blast/nt/nt -query contig-100.fa -out contig-100.blastn.xml -outfmt 5 -culling_limit 2 -max_target_seqs 1 -num_threads 20 -evalue 0.00005