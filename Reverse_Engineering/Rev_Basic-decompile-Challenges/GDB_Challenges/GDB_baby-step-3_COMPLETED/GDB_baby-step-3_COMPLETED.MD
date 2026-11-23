# <GDB_baby-step-3> — Reversing

> Flag: academy{0x6bc96222}

### Details:

- Compiled binary file: 'debugger0_c'.

- Now for something a little different. 0x2262c96b is loaded into memory in the main function. Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr. The flag is the four bytes as they are stored in memory. If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: academy{0x11223344}. Debug this

Hints:
1. You'll need to breakpoint the instruction after the memory load.
2. Use the gdb command x/4xb addr with the memory location as the address addr to examine. GDB manual page
3. Any registers in addr should be prepended with $ like $rbp.
4. Don't use square brackets for addr
5. What is endianness


## 1. Analysis

- command: `file debugger0_c`

ELF					    Linux executable format
64-bit				  Designed for a 64-bit architecture
LSB					    Little-endian byte order
PIE					    Position Independent Executable
Dynamically     linked	Uses external libraries
Not stripped		Contains symbol and debugging information

This 'not stripped' means the binary retains useful information about its functions and symbols, making it easier to investigate with GDB.


## 2. Static Analysis

- command: `nm debugger0_b`
- return: `401106 T main`


This tells us:
- main is a function in the executable.
- Its address (in the binary's disassembly) is 0x401106.
- T means the symbol is located in the executable's code section.


- command: `objdump -d -M intel debugger0_c`

0000000000401106 <main>:
  401106:       f3 0f 1e fa             endbr64
  40110a:       55                      push   rbp
  40110b:       48 89 e5                mov    rbp,rsp
  40110e:       89 7d ec                mov    DWORD PTR [rbp-0x14],edi
  401111:       48 89 75 e0             mov    QWORD PTR [rbp-0x20],rsi
  401115:       c7 45 fc 6b c9 62 22    mov    DWORD PTR [rbp-0x4],0x2262c96b
  40111c:       8b 45 fc                mov    eax,DWORD PTR [rbp-0x4]
  40111f:       5d                      pop    rbp
  401120:       c3                      ret



- From the objdump, we can already see the assembly instructions mentioned in the hint and how its loaded into eax at address '40111c'


## 3. Dynamic Analysis   

Open the binary:

- `gdb debugger0_c`

Inside GDB:

- `break main`
- `run`

This pauses execution when main() begins.

Next, enter:

- `disassemble main`

This displays the instructions of main() inside GDB.

disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
=> 0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x2262c96b
   0x000000000040111c <+22>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040111f <+25>:    pop    rbp
   0x0000000000401120 <+26>:    ret
End of assembler dump.


Now let's set a breakpoint at the instruction that loads the return value:

- `break *(main+22)`

+22 Because main starts at 0x401106, and the instruction mov [rbp-0x4] into eax.

- continue

- x/4xb $rbp-0x4
This examines 4 (4) consecutive bytes (b) starting at memory address $rbp - 0x4, displaying each byte in hexadecimal (x).

output: 0x6b    0xc9    0x62    0x22

This is now the 4 hex values values mentioned in the flag instruction.

## 4. Script and Explanation 

bytes = [0x6b, 0xc9, 0x62, 0x22]

print(f"academy{{{"0x" + "".join(f"{b:02x}" for b in bytes)}}}")

#f"{b:02x}" formats each number as lowercase hexadecimal, padded with a leading 0 if needed so every byte stays 2 hex digits (for example, 0xa becomes 0a).

#"0x" + "".join() glues the 0x prefix and all four byte digits together into 0x6bc96222.

## 5. Learning
1. I learned about the examine-memory command that works in this format: (examine/<count><format><size> <address>)

2. The Little-endian mentioned in the 5th hint means the least significant byte (the rightmost byte) is stored at the lowest memory address was hinting about the arrangement on combining the 4 hex values.
