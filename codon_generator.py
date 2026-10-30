from itertools import product

# Standard genetic code: DNA codons -> amino acids
CODON_TABLE = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}

START_CODONS = {"ATG"}
STOP_CODONS = {"TAA", "TAG", "TGA"}


def generate_codon_table():
    """Generate and verify all 64 codons."""
    bases = "TCAG"
    all_codons = {
        "".join(codon)
        for codon in product(bases, repeat=3)
    }

    if set(CODON_TABLE) != all_codons:
        raise ValueError("Codon table is incomplete or incorrect.")

    return CODON_TABLE


def translate_sequence():
    sequence = input(
        "Enter a DNA or RNA sequence: "
    ).strip().upper().replace(" ", "")

    if not sequence:
        print("Error: Sequence cannot be empty.")
        return

    # Identify sequence type and convert RNA to DNA notation
    if set(sequence) <= set("ACGT"):
        sequence_type = "DNA"
    elif set(sequence) <= set("ACGU"):
        sequence_type = "RNA"
        sequence = sequence.replace("U", "T")
    else:
        print("Error: Use only A, T, G, C for DNA "
              "or A, U, G, C for RNA.")
        return

    table = generate_codon_table()

    # Separate complete codons from leftover nucleotides
    codons = [
        sequence[i:i + 3]
        for i in range(0, len(sequence) - 2, 3)
    ]

    leftover = sequence[len(codons) * 3:]

    print("\nSequence type:", sequence_type)
    print("Sequence length:", len(sequence), "nucleotides")

    if not codons:
        print("No complete codons available for translation.")
        if leftover:
            print("Incomplete codon:", leftover)
        return

    print("\nTRANSLATION TABLE")
    print("-" * 55)
    print(f"{'Position':<10}{'Codon':<10}{'Amino acid':<22}{'Status'}")
    print("-" * 55)

    amino_acids = []
    start_positions = []
    stop_positions = []

    for position, codon in enumerate(codons, start=1):
        amino_acid = table[codon]
        status = ""

        if codon in START_CODONS:
            status = "Start"
            start_positions.append(position)

        if codon in STOP_CODONS:
            status = "Stop"
            stop_positions.append(position)

        amino_acids.append(amino_acid)

        print(f"{position:<10}{codon:<10}"
              f"{amino_acid:<22}{status}")

    print("-" * 55)
    print("Codons:", " - ".join(codons))
    print("Amino acids:", " - ".join(amino_acids))

    print("Start codon positions:", start_positions or "None")
    print("Stop codon positions:", stop_positions or "None")

    if leftover:
        print("Incomplete codon at end:", leftover,
              "(not translated)")
    else:
        print("Incomplete codon at end: None")

 
def calculate_gc_content(sequence):
    """Calculate the GC content percentage of a DNA sequence."""

    sequence = sequence.upper().replace(" ", "")

    if not sequence:
        raise ValueError("Sequence cannot be empty.")

    if any(base not in "ATGC" for base in sequence):
        raise ValueError("Invalid DNA sequence. Use only A, T, G and C.")

    gc_count = sequence.count("G") + sequence.count("C")

    gc_percentage = (gc_count / len(sequence)) * 100

    return gc_percentage
       

def display_codon_table():
    """Display all 64 codons in the dictionary."""
    print("\nCOMPLETE STANDARD CODON TABLE")
    print("-" * 35)

    for codon in sorted(CODON_TABLE):
        print(f"{codon} : {CODON_TABLE[codon]}")


if __name__ == "__main__":
    generate_codon_table()
    display_codon_table()

    translate_sequence()

    sequence = input("\nEnter a DNA sequence to calculate GC content: ")

    try:
        gc_content = calculate_gc_content(sequence)
        print(f"GC content: {gc_content:.2f}%")
    except ValueError as error:
        print("Error:", error)
