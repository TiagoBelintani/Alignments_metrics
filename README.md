# alignment-metrics

**A universal Python tool for quantifying multi-species alignments in FASTA format.**  
Quickly assess which species are present in which alignments, get global stats, and produce summary tables for downstream analyses.

---

##  Features

- **Counts the number of alignment files**
- **Identifies all unique species across all alignments**
- **Counts in how many alignments each species appears**
- **Reports in which files each species is found**
- **Counts total number of sequences per species (accounts for duplicates)**
- **Computes the mean alignment size (number of sequences per alignment)**
- **Lists, for each alignment:**
  - Total number of sequences
  - Which species are present and which are missing
- **Highlights alignments that include all species (“complete alignments”)**

---

##  Usage

### **Basic command**

```bash
python alignment_metrics.py --dir /path/to/your/alignments --out results.tsv

--dir: Directory containing your alignment files (.fa, .fasta, or .aln accepted)

--out: Output file name (will also create an extra file named <your_out_file>_alignments.tsv)

python alignment_metrics.py --dir ./alignments --out align_stats.tsv

📦 Output
Main table (align_stats.tsv):
species	n_alignments	proportion	total_sequences	files
Nemesia	185	0.926	210	gene1.fa,gene2.fa...
Pionothele	90	0.451	98	gene3.fa,gene7.fa...
...	...	...	...	...

species: Name of the species (parsed from the FASTA header)

n_alignments: In how many alignments this species appears

proportion: Fraction of total alignments in which the species appears

total_sequences: Total number of sequences (including duplicates)

files: List of alignment files where the species appears

Per-alignment table (align_stats_alignments.tsv):
alignment	n_sequences	species_present	species_absent
gene1.fa	15	Nemesia,Pionothele,...	Sinopesa
...	...	...	...

alignment: Name of the alignment file

n_sequences: Number of sequences in that file

species_present: Species present in that alignment

species_absent: Species missing from that alignment

Terminal output:
Total alignments

Total unique species

Mean alignment size (number of sequences)

List of “complete” alignments (with all species present), if any

 How species are parsed
By default, the script assumes the species name is the first word in each FASTA header.
Examples:

>SpeciesName_sequenceID
>SpeciesName|sequenceID

If your headers are different, you can easily adapt this line in the script:

name = line[1:].strip().split()[0].split('|')[0]
Just change the parsing logic to match your naming convention.

 Requirements
Python 3.x

No extra dependencies are required—just plain Python.


