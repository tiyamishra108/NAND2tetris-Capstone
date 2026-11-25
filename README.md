💻 Nand2Tetris Capstone Project
Student: Tiya Mishra
Roll Number: 2501730026
Project: Nand2Tetris Capstone
📌 About the Project
This repository contains my Nand2Tetris Capstone Project. The
project helped me understand the basic working of the Hack computer, how
assembly instructions are translated into machine code, and how a
program can use screen memory.

The work is organised into three parts:
- Part A -- Computer: Hack computer HDL files, program files, and
  test files.
- Part B -- Assembler: A Python-based Hack assembler that
  translates assembly instructions into binary machine code.
- Part C -- Box Program: A Hack assembly program that draws and
  clears a rectangular area on the screen based on keyboard input.
📂 Project Structure
Nand2tetris_Capstone/
│
├── README.md
│
├── Documentation/
│   └── Capstone_Report.docx
│
├── Part-A-Computer/
│   ├── HDL/
│   │   ├── Computer.hdl
│   │   ├── CPU.hdl
│   │   └── Memory.hdl
│   │
│   ├── Programs/
│   │   ├── Add.hack
│   │   ├── Max.hack
│   │   └── Rect.hack
│   │
│   └── TestFiles/
│       └── Hardware Simulator .tst and .cmp files
│
├── Part-B-Assembler/
│   ├── assembler.py
│   ├── symbols.txt
│   ├── programs/
│   │   ├── DuplicateLabel.asm
│   │   └── DuplicateLabel.hack
│   └── tests/
│       └── test_assembler.py
│
└── Part-C-Box-Program/
    ├── Box.asm
    └── Box.hack
🧩 Part A -- Hack Computer
This part contains the main HDL files of the Hack computer:
- Computer.hdl
- CPU.hdl
- Memory.hdl
The Programs folder contains the machine-code files for Add, Max,
and Rect. The TestFiles folder contains .tst and .cmp files
related to the Computer, CPU, and Memory tests.
⚙️ Part B -- Hack Assembler
The assembler is implemented in Python. It takes a Hack assembly
(.asm) file as input and converts the instructions into 16-bit binary
machine code. The generated output is saved in a .hack file.
How the assembler works
1. It reads the assembly file and removes comments and blank lines.
2. In the first pass, it identifies labels and stores their ROM
   addresses in the symbol table.
3. In the second pass, it translates A-instructions and
   C-instructions into binary.
4. It resolves predefined symbols, labels, and variable addresses.
5. It writes the generated machine code into a .hack file.
The symbols.txt file stores the symbols and their corresponding
addresses.
Run the assembler
Run this command from the project root folder:
python Part-B-Assembler/assembler.py Part-B-Assembler/programs/DuplicateLabel.asm
To specify a custom output file:
python Part-B-Assembler/assembler.py Part-B-Assembler/programs/DuplicateLabel.asm -o Part-B-Assembler/programs/CustomOutput.hack
Run the unit tests
python -m unittest discover -s Part-B-Assembler/tests -v
The test file contains four unit tests covering different assembler
operations. The test run completed with all four tests passing.
🖥️ Part C -- Box Program
This part contains the Box.asm program and its generated machine-code
file, Box.hack.

The program checks keyboard input and uses screen memory locations to
draw or clear a rectangular area. It uses K = 26 and loops to update
screen memory across multiple rows.

To assemble the Box program, run:
python Part-B-Assembler/assembler.py Part-C-Box-Program/Box.asm
The assembler generated 60 instructions for this program.
🛠️ Tools and Technologies
- Python 3
- Hack Assembly Language
- Hack HDL
- Nand2Tetris test files
- Git and GitHub
🎯 What I Learned
While working on this project, I got a better understanding of:
- The basic organisation of the Hack computer.
- The role of the CPU and memory.
- How assembly instructions are converted into machine code.
- How a two-pass assembler works.
- How labels and variables are stored in a symbol table.
- How to write and run basic Python unit tests.
👩‍💻 Author
Tiya Mishra
Roll Number: 2501730026

Nand2Tetris Capstone Project