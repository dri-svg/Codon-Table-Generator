
import unittest
from itertools import product
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

import codon_generator


class TestCodonGenerator(unittest.TestCase):

    # Test 1: Verify that all 64 codons are present
    def test_all_64_codons(self):
        expected_codons = {
            "".join(codon)
            for codon in product("TCAG", repeat=3)
        }

        self.assertEqual(set(codon_generator.CODON_TABLE), expected_codons)
        self.assertEqual(len(codon_generator.CODON_TABLE), 64)

    # Test 2: Verify the standard DNA translation
    def test_dna_translation(self):
        output = StringIO()

        with patch("builtins.input", return_value="ATGGCTTTTTAA"):
            with redirect_stdout(output):
                codon_generator.translate_sequence()

        result = output.getvalue()

        self.assertIn("Methionine", result)
        self.assertIn("Alanine", result)
        self.assertIn("Phenylalanine", result)
        self.assertIn("Stop", result)

    # Test 3: Identify the start codon
    def test_start_codon(self):
        output = StringIO()

        with patch("builtins.input", return_value="ATGGCT"):
            with redirect_stdout(output):
                codon_generator.translate_sequence()

        self.assertIn("Start codon positions: [1]", output.getvalue())

    # Test 4: Identify the stop codon
    def test_stop_codon(self):
        output = StringIO()

        with patch("builtins.input", return_value="ATGTAA"):
            with redirect_stdout(output):
                codon_generator.translate_sequence()

        self.assertIn("Stop codon positions: [2]", output.getvalue())

    # Test 5: Verify RNA sequence conversion
    def test_rna_translation(self):
        output = StringIO()

        with patch("builtins.input", return_value="AUGGCUUUUUAA"):
            with redirect_stdout(output):
                codon_generator.translate_sequence()

        result = output.getvalue()

        self.assertIn("Sequence type: RNA", result)
        self.assertIn("Methionine", result)
        self.assertIn("Alanine", result)
        self.assertIn("Phenylalanine", result)

    # Test 6: Handle incomplete codons
    def test_incomplete_codon(self):
        output = StringIO()

        with patch("builtins.input", return_value="ATGGCTA"):
            with redirect_stdout(output):
                codon_generator.translate_sequence()

        self.assertIn("Incomplete codon at end: A", output.getvalue())

    # Test 7: Reject invalid nucleotide sequences
    def test_invalid_sequence(self):
        output = StringIO()

        with patch("builtins.input", return_value="ATGBCT"):
            with redirect_stdout(output):
                codon_generator.translate_sequence()

        self.assertIn("Error: Use only A, T, G, C", output.getvalue())


    # Test 8: Empty sequence handling
    def test_empty_sequence(self):
        output = StringIO()

        with patch("builtins.input", return_value=""):
            with redirect_stdout(output):
                codon_generator.translate_sequence()

        self.assertIn("Sequence cannot be empty", output.getvalue())

    # Test 9: Sequence containing only incomplete codon
    def test_only_incomplete_codon(self):
        output = StringIO()

        with patch("builtins.input", return_value="AT"):
            with redirect_stdout(output):
                codon_generator.translate_sequence()

        result = output.getvalue()

        self.assertIn("No complete codons", result)
        self.assertIn("Incomplete codon: AT", result)

    # Test 10: Sequence containing spaces
    def test_sequence_with_spaces(self):
        output = StringIO()

        with patch("builtins.input", return_value="ATG GCT"):
            with redirect_stdout(output):
                codon_generator.translate_sequence()

        result = output.getvalue()

        self.assertIn("Methionine", result)
        self.assertIn("Alanine", result)

    # Test 11: Verify representative codon assignments
    def test_amino_acid_assignments(self):
        expected = {
            "ATG": "Methionine",
            "GCT": "Alanine",
            "TTT": "Phenylalanine",
            "TGG": "Tryptophan",
            "AAA": "Lysine",
            "TAA": "Stop",
            "TAG": "Stop",
            "TGA": "Stop"
        }

        for codon, amino_acid in expected.items():
            with self.subTest(codon=codon):
                self.assertEqual(
                    codon_generator.CODON_TABLE[codon],
                    amino_acid
                )

    # Test 12: Verify all 64 standard genetic code assignments
    def test_complete_standard_genetic_code(self):
        expected_table = {
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

        self.assertEqual(
            codon_generator.CODON_TABLE,
            expected_table
        ) 
  
    # Test 13: Verify GC content calculation
    def test_gc_content(self):
        result = codon_generator.calculate_gc_content("ATGGCTTTTTAA")
        self.assertAlmostEqual(result, 25.0)
      
    # Test 14: Check sequence with 100% GC content
    def test_gc_content_all_gc(self):
        result = codon_generator.calculate_gc_content("GGCC")
        self.assertEqual(result, 100.0)

    # Test 15: Check sequence with 0% GC content
    def test_gc_content_all_at(self):
        result = codon_generator.calculate_gc_content("AATT")
        self.assertEqual(result, 0.0)

    # Test 16: Reject invalid DNA sequence for GC calculation
    def test_gc_content_invalid_sequence(self):
        with self.assertRaises(ValueError):
            codon_generator.calculate_gc_content("ATGX")

    # Test 17: Reject empty sequence for GC calculation
    def test_gc_content_empty_sequence(self):
        with self.assertRaises(ValueError):
            codon_generator.calculate_gc_content("")

if __name__ == "__main__":
    unittest.main()
