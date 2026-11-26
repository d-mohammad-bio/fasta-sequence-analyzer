

# FASTA Sequence Analyzer

A beginner-friendly Python bioinformatics project for reading FASTA files and analyzing DNA sequences.

## Overview

The FASTA Sequence Analyzer is a command-line tool written in Python. It reads DNA sequences from a user-specified FASTA file and calculates basic sequence statistics.

The project was developed to practice Python programming while exploring fundamental bioinformatics concepts.

## Features

- **FASTA file reader:** Reads DNA sequences from FASTA-formatted files.
- **Multiple sequence support:** Processes multiple sequences in a single FASTA file.
- **Sequence length:** Calculates the length of each DNA sequence in base pairs (bp).
- **GC content:** Calculates the percentage of guanine (G) and cytosine (C) in each sequence.
- **Nucleotide counting:** Counts the occurrences of A, T, G, C, and N.
- **Combined summary:** Calculates the total number of sequences, total sequence length, nucleotide counts, and overall GC content.
- **User-specified input:** Allows users to specify the FASTA file directly when running the program.

## Requirements

- Python 3.x
- No external Python packages required.

The project uses Python's built-in modules.

## Installation

Clone the repository:

```bash
git clone https://github.com/d-mohammad-bio/fasta-sequence-analyzer.git
```

Navigate to the project directory:

```bash
cd fasta-sequence-analyzer
```

## Usage

Run the program from your terminal by specifying the FASTA file you want to analyze.

```bash
py main.py example.fasta
```

You can also analyze a different FASTA file:

```bash
py main.py sequences.fasta
```

To specify a file inside another directory:

```bash
py main.py data/sequences.fasta
```

The program accepts a filename or file path as a command-line argument.

### Help

To display the available command-line instructions:

```bash
py main.py --help
```

## Example Input

An example FASTA file (`example.fasta`):

```text
>Sequence_1
ATGCGCATTAAGCG
>Sequence_2
ATGGGCCCAATT
>Sequence_3
ATGCNNAT
```

## Example Output

```text
================================
Sequence: Sequence_1
================================
Length: 14 bp
GC content: 50.00%

Nucleotide counts:
A: 4
T: 3
G: 4
C: 3
N: 0

================================
Sequence: Sequence_2
================================
Length: 12 bp
GC content: 50.00%

Nucleotide counts:
A: 3
T: 3
G: 3
C: 3
N: 0

================================
Sequence: Sequence_3
================================
Length: 8 bp
GC content: 25.00%

Nucleotide counts:
A: 2
T: 2
G: 1
C: 1
N: 2

================================
TOTAL SUMMARY
================================
Number of sequences: 3
Total length: 34 bp

Total nucleotide counts:
A: 9
T: 8
G: 8
C: 7
N: 2

Overall GC content: 44.12%
```

*Note: GC content is calculated as (G + C) / total sequence length × 100. Ambiguous bases such as N are included in the total length.*

## Project Structure

```text
fasta-sequence-analyzer/
│
├── main.py
├── example.fasta
├── README.md
└── .gitignore
```

| File | Description |
|---|---|
| `main.py` | Contains the FASTA reader and sequence analysis functions. |
| `example.fasta` | Example FASTA input file. |
| `README.md` | Project documentation. |
| `.gitignore` | Specifies files Git should ignore. |

## Main Functions

| Function | Description |
|---|---|
| `read_fasta(filename)` | Reads sequences from a FASTA file and stores them in a dictionary. |
| `calculate_sequence_length(sequence)` | Returns the length of a DNA sequence. |
| `calculate_gc_content(sequence)` | Calculates the GC percentage of a DNA sequence. |
| `count_nucleotides(sequence)` | Counts A, T, G, C, and N in a sequence. |

## Learning Objectives

Through this project, I am practicing:

- Python functions and dictionaries.
- File handling and reading external files.
- String manipulation and sequence processing.
- Loops and conditional statements.
- Command-line arguments using `argparse`.
- Git and GitHub version control.
- Feature branches and pull requests.

## Future Improvements

Possible future features include:

- Input validation for FASTA files and DNA sequences.
- Improved error handling for missing or invalid files.
- Support for additional nucleotide ambiguity codes.
- Exporting analysis results to CSV.
- Unit testing with `pytest`.
- Separating the code into reusable Python modules.

## Author

**Doha Mohammad**

GitHub: [@d-mohammad-bio](https://github.com/d-mohammad-bio)

