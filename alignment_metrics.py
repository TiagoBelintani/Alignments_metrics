import os
import argparse
from collections import defaultdict

def parse_fasta_species(fasta_file):
    species = []
    with open(fasta_file) as f:
        for line in f:
            if line.startswith(">"):
                # Adjust this line according to your header format!
                name = line[1:].strip().split()[0].split('|')[0]
                species.append(name)
    return species

def main():
    parser = argparse.ArgumentParser(description="Quantify alignments: species x files + extra metrics")
    parser.add_argument("--dir", required=True, help="Directory containing alignment files (FASTA format)")
    parser.add_argument("--out", required=True, help="Output table file (tsv)")
    args = parser.parse_args()

    aln_dir = args.dir
    out_file = args.out

    species_counts = defaultdict(int)
    species_aln_counts = defaultdict(set)
    species_total_seqs = defaultdict(int)
    aln_species = dict()
    aln_numseqs = dict()

    aln_files = [f for f in os.listdir(aln_dir) if f.endswith(".fa") or f.endswith(".fasta") or f.endswith(".aln")]

    # Gather all possible species
    all_species = set()
    for aln in aln_files:
        path = os.path.join(aln_dir, aln)
        found_species = parse_fasta_species(path)
        aln_species[aln] = set(found_species)
        aln_numseqs[aln] = len(found_species)
        all_species.update(found_species)
        for sp in set(found_species):
            species_counts[sp] += 1
            species_aln_counts[sp].add(aln)
            species_total_seqs[sp] += found_species.count(sp)

    print(f"\n# Alignment quantification in '{aln_dir}'\n")
    print(f"Total number of alignments: {len(aln_files)}")
    print(f"Total number of unique species: {len(all_species)}")
    mean_aln_size = sum(aln_numseqs.values()) / len(aln_files) if aln_files else 0
    print(f"Mean alignment size (number of sequences): {mean_aln_size:.2f}\n")

    with open(out_file, "w") as out:
        out.write("species\tn_alignments\tproportion\ttotal_sequences\tfiles\n")
        for sp in sorted(species_counts.keys()):
            files = ",".join(sorted(species_aln_counts[sp]))
            proportion = species_counts[sp] / len(aln_files) if aln_files else 0
            out.write(f"{sp}\t{species_counts[sp]}\t{proportion:.3f}\t{species_total_seqs[sp]}\t{files}\n")

    print(f"Main results saved to {out_file}")

    # Extra metrics:
    aln_metrics = out_file.replace(".tsv", "_alignments.tsv")
    with open(aln_metrics, "w") as f:
        f.write("alignment\tn_sequences\tspecies_present\tspecies_absent\n")
        for aln in sorted(aln_files):
            present = sorted(aln_species[aln])
            absent = sorted(all_species - aln_species[aln])
            f.write(f"{aln}\t{aln_numseqs[aln]}\t{','.join(present)}\t{','.join(absent)}\n")
    print(f"Per-alignment metrics saved to {aln_metrics}")

    # List of "complete" alignments (all species present)
    complete = [aln for aln in aln_files if len(aln_species[aln]) == len(all_species)]
    if complete:
        print(f"\nAlignments with all species present:")
        for aln in complete:
            print(f" - {aln}")

if __name__ == "__main__":
    main()
