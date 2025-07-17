# alignment-metrics

**A universal Python tool for quantifying multi-species alignments in FASTA format.**  
Quickly assess which species are present in which alignments, get global stats, and produce summary tables for downstream analyses.

## Features

- **Counts the number of alignment files**
- **Identifies all unique species across all alignments**
- **Counts in how many alignments each species appears**
- **Reports in which files each species is found**
- **Counts total number of sequences per species (accounts for duplicates)**
- **Computes the mean alignment size (number of sequences per alignment)**
- **Lists, for each alignment:**
  - Total number of sequences
  - Which species are present and which are missing
- **Highlights alignments that include all species ("complete alignments")**

## Usage

```bash
python alignment_metrics.py --dir /path/to/your/alignments --out results.tsv
