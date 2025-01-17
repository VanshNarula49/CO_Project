# RISC-V Assembler and Simulator

## Overview
This project is a comprehensive RISC-V assembler and simulator, designed to translate RISC-V assembly code into machine code and emulate its execution. The tool supports various types of RISC-V instructions, manages memory and registers, and enables real-time code execution for testing and analysis.

### Key Features
- **Assembler:** Translates RISC-V assembly code into machine code.
- **Simulator:** Executes instructions and manages registers and memory operations.
- **Instruction Support:** Implements all major RISC-V instruction types, including R-type, I-type, S-type, B-type, U-type, and J-type.
- **Error Handling:** Identifies invalid instructions and provides detailed error messages for debugging.
- **Real-Time Testing:** Simulates the execution of code with immediate feedback.

## Prerequisites

- **Python 3.8 or higher**
- Basic understanding of the RISC-V instruction set architecture (ISA).

## Setup

1. Clone the repository to your local machine.
2. Install the required Python libraries (if any).
3. Ensure your assembly code input file is named `main.txt` and placed in the root directory of the project.

## Usage

### Input File Structure
The input file (`main.txt`) should contain RISC-V assembly instructions, one per line. For example:
```
addi x1, x0, 5
beq x1, x2, label
jalr x0, x1, 0
```

### Running the Simulator

To run the simulator:

```bash
python main.py main.txt output.txt
```

- `main.txt`: Input file containing assembly code.
- `output.txt`: Output file where the machine code and errors (if any) are written.

### Output
- Machine code for each instruction in the input file is written to `output.txt`.
- If an error is encountered, an error message is logged with the line number.

## Instruction Types and Parsers
The project supports the following RISC-V instruction types:

1. **R-Type Instructions**
   - Operations: `add`, `sub`, `sll`, `slt`, `sltu`, `xor`, `srl`, `or`, `and`
   - Parser: `R_parser.py`

2. **I-Type Instructions**
   - Operations: `lw`, `addi`, `sltiu`, `jalr`
   - Parser: `I_parser.py`

3. **S-Type Instructions**
   - Operations: `sw`
   - Parser: `S_parser.py`

4. **B-Type Instructions**
   - Operations: `beq`, `bne`, `bge`, `bgeu`, `blt`, `bltu`
   - Parser: `B_parser.py`

5. **U-Type Instructions**
   - Operations: `auipc`, `lui`
   - Parser: `U_parser.py`

6. **J-Type Instructions**
   - Operations: `jal`
   - Parser: `J_parser.py`

## Error Handling
The simulator includes robust error handling:
- Invalid instruction formats are flagged with descriptive error messages.
- Errors are logged in the output file with the line number for easier debugging.

Example error message:
```
Error in line 3: Unknown operation
```

## Example Workflow

### Input (`main.txt`):
```
addi x1, x0, 10
sw x1, 0(x2)
beq x1, x2, label
jal x0, 16
```

### Output (`output.txt`):
```
0000000000010100
1111111111111111
Error in line 3: Unknown operation
0000000000100000
```

## Contributions

Contributors: Vansh Narula, Vaishnavi Srivastava, Manya Grover

### Future Enhancements
- Support for additional RISC-V instruction formats.
- Integration with a graphical interface for visualizing memory and register states.
- Optimization of parsing and simulation performance.

## References
- RISC-V ISA Documentation: [https://riscv.org/](https://riscv.org/)
- Python Documentation: [https://docs.python.org/3/](https://docs.python.org/3/)

---

