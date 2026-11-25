import sys
import os
import unittest
from contextlib import redirect_stdout
from io import StringIO

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

import assembler


def reset_symbols():
    assembler.SYMBOLS.clear()

    predefined = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576
    }

    for i in range(16):
        predefined[f"R{i}"] = i

    assembler.SYMBOLS.update(predefined)


class TestAssembler(unittest.TestCase):

    def setUp(self):
        reset_symbols()

    def test_a_instruction(self):
        result = assembler.second_pass(["@10"])

        self.assertEqual(
            result,
            ["0000000000001010"]
        )

    def test_c_instruction(self):
        result = assembler.second_pass(["D=A"])

        self.assertEqual(
            result,
            ["1110110000010000"]
        )

    def test_label_address(self):
        lines = [
            "@10",
            "D=A",
            "(LOOP)",
            "@LOOP",
            "0;JMP"
        ]

        assembler.first_pass(lines)

        self.assertEqual(
            assembler.SYMBOLS["LOOP"],
            2
        )

    def test_duplicate_label_detection(self):
        lines = [
            "@10",
            "D=A",
            "(LOOP)",
            "@LOOP",
            "0;JMP",
            "(LOOP)"
        ]

        output = StringIO()

        with redirect_stdout(output):
            assembler.first_pass(lines)

        self.assertIn(
            "Duplicate label detected: LOOP",
            output.getvalue()
        )

        self.assertEqual(
            assembler.SYMBOLS["LOOP"],
            2
        )


if __name__ == "__main__":
    unittest.main()