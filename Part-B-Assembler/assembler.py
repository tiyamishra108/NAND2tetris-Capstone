# Nand2Tetris Capstone Project
# Student: Tiya Mishra
# Roll Number: 2501730026
# Personalised Feature: Duplicate Label Detection

import sys
import re
import os
import argparse


# Predefined symbols
SYMBOLS = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576
}

for i in range(16):
    SYMBOLS[f"R{i}"] = i


# Computation codes
COMP = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "M": "1110000",
    "!D": "0001101",
    "!A": "0110001",
    "!M": "1110001",
    "-D": "0001111",
    "-A": "0110011",
    "-M": "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101"
}


# Destination codes
DEST = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}


# Jump codes
JUMP = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}


# Reset predefined symbols
def reset_symbols():
    global SYMBOLS

    SYMBOLS = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576
    }

    for i in range(16):
        SYMBOLS[f"R{i}"] = i


# Remove comments and blank lines
def clean_lines(filename):

    with open(filename, "r") as file:

        lines = []

        for line in file:

            line = line.split("//")[0].strip()

            if line:
                lines.append(line)

        return lines


# First Pass: Build Symbol Table
def first_pass(lines):

    rom_address = 0

    for line in lines:

        if line.startswith("(") and line.endswith(")"):

            label = line[1:-1].strip()

            # Personalised Feature: Duplicate Label Detection
            if label in SYMBOLS:
                print(f"Warning: Duplicate label detected: {label}")
                continue

            if not re.fullmatch(
                r"[A-Za-z_.$:][A-Za-z0-9_.$:]*",
                label
            ):
                raise ValueError(f"Invalid label: {label}")

            SYMBOLS[label] = rom_address

        else:
            rom_address += 1


# Second Pass: Generate Machine Code
def second_pass(lines):

    machine_code = []
    next_variable = 16

    for line in lines:

        if line.startswith("(") and line.endswith(")"):
            continue

        # A-instruction
        if line.startswith("@"):

            symbol = line[1:].strip()

            if symbol.isdigit():

                address = int(symbol)

            else:

                if symbol not in SYMBOLS:

                    SYMBOLS[symbol] = next_variable
                    next_variable += 1

                address = SYMBOLS[symbol]

            if address < 0 or address > 32767:
                raise ValueError(f"Invalid address: {line}")

            machine_code.append(format(address, "016b"))

        # C-instruction
        else:

            dest = ""
            jump = ""

            if "=" in line:
                dest, line = line.split("=", 1)

            if ";" in line:
                line, jump = line.split(";", 1)

            comp = line.strip()
            dest = dest.strip()
            jump = jump.strip()

            if comp not in COMP:
                raise ValueError(f"Invalid computation: {comp}")

            if dest not in DEST:
                raise ValueError(f"Invalid destination: {dest}")

            if jump not in JUMP:
                raise ValueError(f"Invalid jump: {jump}")

            instruction = (
                "111" +
                COMP[comp] +
                DEST[dest] +
                JUMP[jump]
            )

            machine_code.append(instruction)

    return machine_code


# Save Symbol Table
def save_symbol_table():

    symbol_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "symbols.txt"
    )

    with open(symbol_file, "w") as file:

        for symbol, address in sorted(SYMBOLS.items()):

            file.write(f"{symbol} = {address}\n")


# Main Assembler Function
def assemble(input_file, output_file=None):

    reset_symbols()

    lines = clean_lines(input_file)

    # First Pass
    first_pass(lines)

    # Second Pass
    machine_code = second_pass(lines)

    # Default output location
    if output_file is None:

        output_file = input_file.rsplit(".", 1)[0] + ".hack"

    # Generate HACK file
    with open(output_file, "w") as file:

        for instruction in machine_code:

            file.write(instruction + "\n")

    # Generate Symbol Table
    save_symbol_table()

    print("\nAssembly completed successfully!")
    print("Input file:", input_file)
    print("Output file:", output_file)
    print("Total instructions:", len(machine_code))


# Command Line Interface
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Hack Assembly Language Assembler"
    )

    parser.add_argument(
        "input_file",
        help="Input ASM file"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Custom output HACK file"
    )

    args = parser.parse_args()

    try:

        assemble(args.input_file, args.output)

    except (ValueError, KeyError) as error:

        print("Assembly Error:", error)

    except FileNotFoundError as error:

        print("File Error:", error)