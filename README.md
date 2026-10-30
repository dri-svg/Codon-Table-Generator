# Codon-Table-Generator
Python program for DNA and RNA codon translation using the standard genetic code.

## Project Overview

The Codon Table Generator is a Python-based bioinformatics application designed to translate DNA and RNA nucleotide sequences into their corresponding amino acid sequences using the standard genetic code.

A codon is a sequence of three nucleotides that specifies an amino acid or a translation termination signal during protein synthesis.

This project demonstrates the application of Python programming and basic bioinformatics concepts in genetic code analysis.

## Objectives

- Develop a dictionary containing all 64 possible codons.
- Accept DNA and RNA sequence input.
- Validate nucleotide sequences.
- Divide sequences into triplets (codons).
- Translate codons into their corresponding amino acids.
- Identify start and stop codons.
- Handle incomplete codons.
- Verify the implementation using automated tests.

## Features

1. Complete Genetic Code: Includes all 64 standard DNA codons.
2. DNA Translation: Converts DNA codons into amino acids.
3. RNA Support: Accepts RNA sequences by converting uracil (U) into thymine (T) internally.
4. Sequence Validation: Detects invalid nucleotide characters.
5. Start Codon Identification: Identifies ATG.
6. Stop Codon Identification: Identifies TAA, TAG and TGA.
7. GC content calculation: Calculates the percentage of guanine (G) and cytosine (C) in a DNA sequence.
8. Incomplete Codon Handling: Detects leftover nucleotides that cannot form a complete triplet.
9. Tabular Output:Displays codon positions, codons, amino acids and start/stop status.

## Technologies Used

- Programming language: Python
- Modules: itertools, unittest
- Development environment: Visual Studio Code
- Version control: Git and GitHub
- Reference database: NCBI Standard Genetic Code

## Project Structure

```text
Codon-Table-Generator/
│
├── codon_generator.py
├── test_codon_generator.py
├── codon_comparison.md
└── README.md
```

## How to Run

### Requirements

- Python 3.x
- Visual Studio Code or another Python-supported environment

### Execution

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Execute:

```bash
python codon_generator.py
```

5. Enter a DNA or RNA sequence when prompted.

## Example

**Input:**

```text
ATGGCTTTTTAA
```

**Codon division:**

```text
ATG - GCT - TTT - TAA
```

**Translation:**

```text
Methionine - Alanine - Phenylalanine - Stop
```

**Start codon:** ATG

**Stop codon:** TAA

## Automated Testing

The project includes a test suite developed using Python's unittest framework.

Run the tests using:

```bash
python -m unittest test_codon_generator.py -v
```

The test suite currently includes 11 tests covering:

- Codon dictionary completeness
- DNA translation
- RNA translation
- Start codon identification
- Stop codon identification
- Incomplete codon handling
- Invalid nucleotide detection
- Empty sequence handling
- Whitespace handling
- Representative amino acid assignments

## Genetic Code Validation

The codon dictionary is compared with the NCBI Standard Genetic Code (Translation Table 1).

Reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi

Refer to `codon_comparison.md` for the comparison methodology and results.

## Limitations

- The program uses the standard genetic code and does not currently support organism-specific alternative genetic codes.
- ATG is used as the only start codon in this implementation.
- Translation is performed in a single reading frame.
- The program does not currently predict open reading frames or perform protein sequence analysis.

## Future Scope

- Support for alternative genetic codes.
- Identification of multiple reading frames.
- Open reading frame prediction.
- FASTA file input.
- Graphical user interface for sequence translation.

## Conclusion

The Codon Table Generator demonstrates how Python can be applied to basic bioinformatics tasks. It provides a simple and systematic approach to nucleotide sequence validation, codon identification and amino acid translation, supported by automated testing and comparison with an established genetic code reference.
