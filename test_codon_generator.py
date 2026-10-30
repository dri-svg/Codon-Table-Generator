
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


if __name__ == "__main__":
    unittest.main()
