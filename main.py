
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


sequences = read_fasta("example.fasta")

for name, sequence in sequences.items():
    length = calculate_sequence_length(sequence)

    print("Sequence:", name)
    print("Length:", length, "bp")
    print()
