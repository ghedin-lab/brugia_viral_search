#!/bin/bash
#PBS -l nodes=1:ppn=20,mem=62gb,walltime=72:00:00
#PBS -j oe
#PBS -M twaddlac@gmail.com
#PBS -m ae
#PBS -N all-idba

module load idba

cd $path

idba_id --pre_correction --num_threads 20 -r $fasta -o $fasta.idba.d