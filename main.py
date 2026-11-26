
import argparse


parser = argparse.ArgumentParser(
    description="Analyze DNA sequences from a FASTA file."
)

parser.add_argument(
    "filename",
    help="Path to the FASTA file you want to analyze"
)

args = parser.parse_args()

def read_fasta(filename):
    sequences = {}

    with open(filename, "r") as file:
        sequence_name = None

        for line in file:
            line = line.strip()

            if line.startswith(">"):
                sequence_name = line[1:]
                sequences[sequence_name] = ""

            elif sequence_name:
                sequences[sequence_name] += line

    return sequences


def calculate_sequence_length(sequence):
    return len(sequence)


def calculate_gc_content(sequence):
    sequence = sequence.upper()

    gc_count = sequence.count("G") + sequence.count("C")

    if len(sequence) == 0:
        return 0.0

    gc_percentage = (gc_count / len(sequence)) * 100

    return gc_percentage


def count_nucleotides(sequence):
    sequence = sequence.upper()

    nucleotide_counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C"),
        "N": sequence.count("N")
    }

    return nucleotide_counts


# Read FASTA file
sequences = read_fasta(args.filename)

# Initialize total statistics
total_counts = {
    "A": 0,
    "T": 0,
    "G": 0,
    "C": 0,
    "N": 0
}

total_length = 0

# Analyze individual sequences
for name, sequence in sequences.items():

    length = calculate_sequence_length(sequence)
    gc_content = calculate_gc_content(sequence)
    nucleotide_counts = count_nucleotides(sequence)

    print("=" * 32)
    print("Sequence:", name)
    print("=" * 32)

    print("Length:", length, "bp")
    print(f"GC content: {gc_content:.2f}%")

    print("\nNucleotide counts:")

    for nucleotide, count in nucleotide_counts.items():
        print(f"{nucleotide}: {count}")

    total_length += length

    for nucleotide in total_counts:
        total_counts[nucleotide] += nucleotide_counts[nucleotide]


# Display combined summary
print("\n" + "=" * 32)
print("TOTAL SUMMARY")
print("=" * 32)

print("Number of sequences:", len(sequences))
print("Total length:", total_length, "bp")

print("\nTotal nucleotide counts:")

for nucleotide, count in total_counts.items():
    print(f"{nucleotide}: {count}")

if total_length > 0:
    total_gc = (
        (total_counts["G"] + total_counts["C"])
        / total_length
    ) * 100
else:
    total_gc = 0.0

print(f"\nOverall GC content: {total_gc:.2f}%")
