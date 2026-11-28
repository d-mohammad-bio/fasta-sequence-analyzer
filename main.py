import argparse
from pathlib import Path

VALID_NUCLEOTIDES = set("ATGCRYSWKMBDHVN")
IUPAC_AMBIGUITY_CODES = "RYSWKMBDHV"

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
    filename = Path(filename)

    if not filename.exists():
        raise FileNotFoundError(f"File not found: {filename}")

    if not filename.is_file():
        raise ValueError(f"Not a regular file: {filename}")

    if filename.stat().st_size == 0:
        raise ValueError(f"FASTA file is empty: {filename}")

    with open(filename, "r") as file:
        sequence_name = None

        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                sequence_name = line[1:].strip()

                if not sequence_name:
                    raise ValueError(
                        f"Invalid FASTA header at line {line_number}: "
                        "missing sequence identifier."
                    )

                if sequence_name in sequences:
                    raise ValueError(
                        f"Duplicate sequence identifier: {sequence_name}"
                    )

                sequences[sequence_name] = ""

            elif sequence_name is None:
                if not sequences:
                    raise ValueError(
                        "No FASTA records found in the file"
                    )
                
                raise ValueError(
                    f"Invalid FASTA format at line {line_number}: "
                    "sequence data found before the first header."
                )

            else:
                sequences[sequence_name] += line

    if not sequences:
        raise ValueError("No FASTA records found in the file.")

    invalid_sequences = {}
    valid_sequences = {}

    for name, sequence in sequences.items():
        
        if not sequence:
            invalid_sequences[name] = "Empty sequence"
            continue

        invalid_chars = set(sequence.upper()) - VALID_NUCLEOTIDES

        if invalid_chars:
            invalid_sequences[name] = (
                f"Invalid nucleotide characters: {', '.join(sorted(invalid_chars))}"
            )
            continue

        valid_sequences[name] = sequence.upper()
        
    return valid_sequences, invalid_sequences


def calculate_sequence_length(sequence):
    return len(sequence)


def calculate_gc_content(sequence):
    sequence = sequence.upper()

    gc_count = sequence.count("G") + sequence.count("C")

    if len(sequence) == 0:
        return 0.0

    gc_percentage = (gc_count / len(sequence)) * 100

    return gc_percentage

def calculate_ambiguity_content(sequence):
    sequence = sequence.upper()

    ambiguous_count = sequence.count("N") + sum(
        sequence.count(code)
        for code in IUPAC_AMBIGUITY_CODES
    )

    ambiguity_percentage = (ambiguous_count / len(sequence)) * 100

    return ambiguity_percentage

def count_nucleotides(sequence):
    sequence = sequence.upper()

    nucleotide_counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C"),
        "N": sequence.count("N") + sum(
            sequence.count(code)
            for code in IUPAC_AMBIGUITY_CODES
        )
    }

    return nucleotide_counts

def count_iupac_codes(sequence):
    sequence = sequence.upper()

    iupac_counts = {
        "N": sequence.count("N")
    }

    for code in IUPAC_AMBIGUITY_CODES:
        count = sequence.count(code)

        if count > 0:
            iupac_counts[code] = count

    return iupac_counts

# Read FASTA file

try:
    sequences, invalid_sequences = read_fasta(args.filename)

except FileNotFoundError as error:
    print(f"\nERROR: {error}")
    print("Please check the file path and try again.")
    raise SystemExit(1)

except ValueError as error:
    print(f"\nERROR: {error}")
    print("Please provide a valid FASTA file.")
    raise SystemExit(1)

if invalid_sequences:
    print("\nWARNING: Some sequences were skipped.")

    for name, error in invalid_sequences.items():
        print(f"{name}: {error}")

if not sequences:
    print("\nERROR: No valid sequences available for analysis.")
    print("Please check your FASTA file and try again.")
    raise SystemExit(1)

# Initialize total statistics
total_counts = {
    "A": 0,
    "T": 0,
    "G": 0,
    "C": 0,
    "N": 0
}

total_iupac_counts = {
    "N": 0,
    **{code: 0 for code in IUPAC_AMBIGUITY_CODES}
}

total_length = 0

# Analyze individual sequences
for name, sequence in sequences.items():

    length = calculate_sequence_length(sequence)
    gc_content = calculate_gc_content(sequence)
    ambiguity_content = calculate_ambiguity_content(sequence)
    nucleotide_counts = count_nucleotides(sequence)
    iupac_counts = count_iupac_codes(sequence)

    print("=" * 32)
    print("Sequence:", name)
    print("=" * 32)

    print("Length:", length, "bp")
    print(f"GC content: {gc_content:.2f}%")
    print(f"Ambiguity content: {ambiguity_content:.2f}%")

    print("\nNucleotide counts:")

    for nucleotide, count in nucleotide_counts.items():
        print(f"{nucleotide}: {count}")
        
    print("\nIUPAC ambiguity code counts:")

    for code, count in iupac_counts.items():
        print(f"{code}: {count}")

    total_length += length

    for nucleotide in total_counts:
        total_counts[nucleotide] += nucleotide_counts[nucleotide]

    for code, count in iupac_counts.items():
        total_iupac_counts[code] += count

# Display combined summary
print("\n" + "=" * 32)
print("TOTAL SUMMARY")
print("=" * 32)

print("Number of valid sequences:", len(sequences))
print("Number of skipped sequences:", len(invalid_sequences))
print("Total length:", total_length, "bp")

print("\nTotal nucleotide counts:")

for nucleotide, count in total_counts.items():
    print(f"{nucleotide}: {count}")

print("\nTotal IUPAC ambiguity code counts:")

for code, count in total_iupac_counts.items():
    if count > 0:
        print(f"{code}: {count}")

if total_length > 0:
    total_gc = (
        (total_counts["G"] + total_counts["C"])
        / total_length
    ) * 100
else:
    total_gc = 0.0

print(f"\nOverall GC content: {total_gc:.2f}%")
