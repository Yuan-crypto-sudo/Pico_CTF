## Repository Structure

pico_ctf/
├── README.md
├── File-Run-Challenges/
│   └── Flag_Hunters-1_COMPLETED/
├── Vault-Door-Challenges/
│   ├── Vault-Door-Training_COMPLETED/
│   ├── Vault-Door-1_COMPLETED/
│   ├── Vault-Door-3_COMPLETED/
│   ├── Vault-Door-4_COMPLETED/
│   ├── Vault-Door-5_COMPLETED/
│   ├── Vault-Door-6_COMPLETED/
│   ├── Vault-Door-7_COMPLETED/
│   └── Vault-Door-8_COMPLETED/
├── Rev_Basic-Real-Binaries/
│   ├── ASCII_FTW_COMPLETED/
│   └── Transformation_COMPLETED/
└── GDB-Challenges/
    ├── GDB_Test_Drive_COMPLETED/
    ├── GDB_baby-step-1_COMPLETED/
    ├── GDB_baby-step-2_COMPLETED/
    ├── GDB_baby-step-3_COMPLETED/
    └── GDB_baby-step-4_COMPLETED/

## Progress Tracker

| Challenge | Category | Status | Technique |
|---|---|---|---|
| Vault Door Training | Reverse Engineering  | Completed              | Hardcoded password 
| Vault Door 1        | Reverse Engineering  | Completed              | Character comparison 
| Vault Door 3        | Reverse Engineering  | Completed              | Character permutation 
| Vault Door 4        | Reverse Engineering  | Completed              | ASCII conversions 
| Vault Door 5        | Reverse Engineering  | Completed              | Base64 and URL decoding 
| Vault Door 6        | Reverse Engineering  | Completed              | XOR 
| Vault Door 7        | Reverse Engineering  | Completed              | Bitwise operations 
| Vault Door 8        | Reverse Engineering  | In Progress            | Bit manipulation 
| Flag Hunters 1      | File Run             | Completed              | Python source analysis 
| ASCII FTW           | Reverse Engineering  | Completed              | Stack string, hex to ASCII (objdump) |
| Transformation      | Reverse Engineering  | Completed              | 16-bit character packing, shift and mask |
| GDB Test Drive      | Reverse Engineering  | Completed              | Basic gdb workflow |
| GDB baby step 1     | Reverse Engineering  | Completed              | Reading (objdump + gdb) |
| GDB baby step 2     | Reverse Engineering  | Completed              | Loop result in `eax` (gdb) |
| GDB baby step 3     | Reverse Engineering  | Completed              | Examining memory byte by byte (gdb) |
| GDB baby step 4     | Reverse Engineering  | Completed              | gdb register and call analysis |

## Skills Practiced So Far

- Reading source and disassembly (objdump, Ghidra) to find the check
- Reversing encodings and transforms: ASCII, Base64, URL, XOR, shifts, bit swaps
- Writing small Python scripts to invert a transformation, with round-trip tests
- gdb basics: breakpoints, stepping, reading registers and memory
