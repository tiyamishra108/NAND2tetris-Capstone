# Hack Computer Box Capstone (ETCCNT301)

* **Student:** Tiya Mishra
* **Roll Number:** 2501730026 (`K = 26`)

## Overview
This project builds a working 16-bit Hack system, a two-pass Python translator, and an interactive assembly program that renders a black rectangle while a key is held down.

## Personal Parameters (`K = 26`)
* **Assembler rule (`26 mod 3 = 2`):** Displays a warning when a label is defined twice and keeps the first ROM address.
* **Screen start:** Row `26` (`16384 + 32 * 26 = 17216`), left edge.
* **Dimensions:** `48` pixels wide (`3` words) by `20` rows tall.

## Project Parts
1. **Part A (Hardware):** `CPU.hdl`, `Memory.hdl`, and `Computer.hdl` verified with course `.tst` scripts.
2. **Part B (Assembler):** `assembler.py` converts `.asm` source into 16-bit `.hack` binary, resolves symbols from RAM `16`, and passes unit tests.
3. **Part C (Box Program):** `Box.asm` polls `@KBD` (`24576`) to fill or clear the `48 x 20` region, compiled into `Box.hack` with `assembler.py`.

## Usage
```bash
python Part-B-Assembler/assembler.py Part-C-Box-Program/Box.asm
python -m unittest discover -s Part-B-Assembler/tests -v
```
