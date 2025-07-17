README.md
markdown
Copy
Edit
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
--dir: Directory containing your alignment files (.fa, .fasta, or .aln accepted)

--out: Output file name (will also create an extra file named results_alignments.tsv)

Example
bash
Copy
Edit
python alignment_metrics.py --dir ./alignments --out align_stats.tsv
Output
Main table (results.tsv):

species: Name of the species (taken from FASTA headers; edit the script if you need a different parsing rule)

n_alignments: Number of alignments in which this species appears

proportion: Proportion of alignments in which the species appears

total_sequences: Total count of sequences for the species across all files

files: Names of the alignment files where the species is present

Per-alignment table (results_alignments.tsv):

alignment: Name of the alignment file

n_sequences: Number of sequences in that alignment

species_present: Species present in that alignment

species_absent: Species not present in that alignment

Terminal output:

Total alignments, total species, mean alignment size, list of complete alignments (if any).

How species are parsed
By default, the script assumes that the species name is the first word in each FASTA header:

shell
Copy
Edit
>SpeciesName_sequenceID
or

shell
Copy
Edit
>SpeciesName|sequenceID
You can easily adapt the line

python
Copy
Edit
name = line[1:].strip().split()[0].split('|')[0]
to match your naming convention.

Requirements
Python 3

\

