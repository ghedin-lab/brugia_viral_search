#!/bin/bash
#PBS -l walltime=24:00:00,nodes=1:ppn=20,mem=96gb
#PBS -j oe
#PBS -m a
#PBS -M twaddlac@gmail.com

module load kraken
cd /scratch/at120/brugia-rnaseq/viral-search

kraken --db /scratch/at120/db/kraken/standard --threads 20 --fastq-input --output all-unmapped.kraken.out --preload all-unmapped.r1.fastq all-unmapped.r2.fastq
kraken-translate --db /scratch/at120/db/kraken/standard > kraken.translate.out
kraken-mpa-report --db /scratch/at120/db/kraken/standard > kraken.mpa.out