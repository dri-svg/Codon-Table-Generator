# Comparison of the Generated Codon Table with NCBI Standard Genetic Code

## 1. Objective

The objective of this comparison is to verify whether the codon-to-amino acid assignments in the Python-based Codon Table Generator agree with the internationally recognised Standard Genetic Code provided by the National Center for Biotechnology Information (NCBI).

## 2. Reference Database

- Database: NCBI (National Center for Biotechnology Information)
- Reference: Standard Genetic Code
- Translation table: Table 1
- Reference link: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi

The NCBI Standard Genetic Code describes how nucleotide triplets (codons) correspond to amino acids during protein synthesis.

## 3. Methodology

The following steps were used for comparison:

1. A dictionary containing all 64 possible DNA codons was created in Python.
2. Each codon was assigned its corresponding amino acid.
3. The generated dictionary was checked against the NCBI Standard Genetic Code (Translation Table 1).
4. Amino acid assignments, start codon and stop codons were examined.
5. The results were evaluated to identify any differences.

## 4. Comparison Results

| Parameter | Python Codon Generator | NCBI Standard Code |
|---|---|---|
| Total possible codons | 64 | 64 |
| Amino acid coding codons | 61 | 61 |
| Stop codons | 3 | 3 |
| Start codon used in this project | ATG | AUG (RNA) |
| Stop codons | TAA, TAG, TGA | UAA, UAG, UGA (RNA) |
| Codon assignments | Standard genetic code | Standard genetic code |

**Note:** NCBI presents the standard code using RNA notation in its codon chart, whereas this project uses DNA notation. Therefore, U in the NCBI RNA codons corresponds to T in the Python DNA dictionary.

## 5. Verification of Codon Assignments

The following representative codons were checked:

| DNA Codon | Amino Acid in Python | NCBI Assignment | Result |
|---|---|---|---|
| TTT | Phenylalanine | Phenylalanine | Match |
| ATG | Methionine | Methionine | Match |
| GCT | Alanine | Alanine | Match |
| TGG | Tryptophan | Tryptophan | Match |
| AAA | Lysine | Lysine | Match |
| CGT | Arginine | Arginine | Match |
| TAA | Stop | Stop | Match |
| TAG | Stop | Stop | Match |
| TGA | Stop | Stop | Match |

The representative codons show agreement between the Python dictionary and the NCBI Standard Genetic Code.

## 6. Observations

- The Python dictionary contains all 64 possible combinations of the four DNA nucleotides.
- Out of these, 61 codons specify amino acids, while three codons function as termination signals.
- AUG in RNA (ATG in DNA) codes for methionine and serves as the conventional initiation codon.
- UAA, UAG and UGA act as stop codons.
- The genetic code is degenerate because multiple codons can specify the same amino acid.
- The Python implementation uses ATG as its start codon for this project.

## 7. Conclusion

The generated Python codon table is consistent with the NCBI Standard Genetic Code (Translation Table 1) for the codon-to-amino acid assignments examined. The implementation successfully represents the 64 possible codons, including 61 amino acid-coding codons and three stop codons.

This comparison supports the accuracy of the codon dictionary used in the project. It also demonstrates how a computational implementation of the genetic code can be validated against an established biological reference database.

## 8. References

1. National Center for Biotechnology Information (NCBI). The Genetic Codes. https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
2. NCBI. Genetic Codes Documentation. https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/taxonomy-processing/genetic-codes/
3. Standard Genetic Code Reference. https://www.ncbi.nlm.nih.gov/books/NBK2327/bin/stdcode.pdf
