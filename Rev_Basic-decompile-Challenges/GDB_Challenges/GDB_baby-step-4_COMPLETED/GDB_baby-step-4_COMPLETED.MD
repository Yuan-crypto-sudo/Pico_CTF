# <GDB_baby-step-4> — Reversing

> Flag: academy{12905}

### Details:

- Compiled binary file: 'debugger0_d'.

- main calls a function that multiplies eax by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is 0x1000, the flag will be academy{4096}.

Hints:
1. A function can be referenced by either its name or its starting address in gdb.

## 1. Analysis

- command: `file debugger0_d`

ELF					       Linux executable format
64-bit				       Designed for a 64-bit architecture
LSB					       Little-endian byte order
PIE					       Position Independent Executable
Dynamically linked	    Uses external libraries
Not stripped		       Contains symbol and debugging information

This 'not stripped' means the binary retains useful information about its functions and symbols, making it easier to investigate with GDB.


## 2. Static Analysis

- command: `nm debugger0_d`
- return: `40111c T main` , `401106 T func1`


This tells us:
- main and func1 are functions in the executable.
- T means the symbol is located in the executable's code section.


- command: `objdump -d -M intel debugger0_d`

0000000000401106 <func1>:
  401106:       f3 0f 1e fa             endbr64
  40110a:       55                      push   rbp
  40110b:       48 89 e5                mov    rbp,rsp
  40110e:       89 7d fc                mov    DWORD PTR [rbp-0x4],edi
  401111:       8b 45 fc                mov    eax,DWORD PTR [rbp-0x4]
  401114:       69 c0 69 32 00 00       imul   eax,eax,0x3269
  40111a:       5d                      pop    rbp
  40111b:       c3                      ret

000000000040111c <main>:
  40111c:       f3 0f 1e fa             endbr64
  401120:       55                      push   rbp
  401121:       48 89 e5                mov    rbp,rsp
  401124:       48 83 ec 20             sub    rsp,0x20
  401128:       89 7d ec                mov    DWORD PTR [rbp-0x14],edi
  40112b:       48 89 75 e0             mov    QWORD PTR [rbp-0x20],rsi
  40112f:       c7 45 fc 8e 02 00 00    mov    DWORD PTR [rbp-0x4],0x28e
  401136:       c7 45 f8 00 00 00 00    mov    DWORD PTR [rbp-0x8],0x0
  40113d:       8b 45 fc                mov    eax,DWORD PTR [rbp-0x4]
  401140:       89 c7                   mov    edi,eax
  401142:       e8 bf ff ff ff          call   401106 <func1>
  401147:       89 45 f8                mov    DWORD PTR [rbp-0x8],eax
  40114a:       8b 45 fc                mov    eax,DWORD PTR [rbp-0x4]
  40114d:       c9                      leave
  40114e:       c3                      ret



- From the objdump, we can already see the assembly instructions of main and func1, and when main calls the func1 att address '401142' along with the edi argument.

- And from here still, we can already see that in func1, the edi argument was moved into a local variable, and into eax, and was operated with `imul`, which is a three-operand form that means: destination = source1 * sourceb.

- So we can say that 0x3269 is the value we're looking for and the flag itself.


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

Dump of assembler code for function main:
   0x000000000040111c <+0>:     endbr64
   0x0000000000401120 <+4>:     push   rbp
   0x0000000000401121 <+5>:     mov    rbp,rsp
   0x0000000000401124 <+8>:     sub    rsp,0x20
=> 0x0000000000401128 <+12>:    mov    DWORD PTR [rbp-0x14],edi
   0x000000000040112b <+15>:    mov    QWORD PTR [rbp-0x20],rsi
   0x000000000040112f <+19>:    mov    DWORD PTR [rbp-0x4],0x28e
   0x0000000000401136 <+26>:    mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040113d <+33>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401140 <+36>:    mov    edi,eax
   0x0000000000401142 <+38>:    call   0x401106 <func1>
   0x0000000000401147 <+43>:    mov    DWORD PTR [rbp-0x8],eax
   0x000000000040114a <+46>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040114d <+49>:    leave
   0x000000000040114e <+50>:    ret
End of assembler dump.

- `disassemble func1`

Dump of assembler code for function func1:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000401111 <+11>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401114 <+14>:    imul   eax,eax,0x3269
   0x000000000040111a <+20>:    pop    rbp
   0x000000000040111b <+21>:    ret
End of assembler dump.

- We can again see that the hec: '0x3269' is the value being multiplied with the original argument from main, which tells us that it is the flag.

## 4. Script and Explanation 

python3 -c 'print("academy{" + str(0x3269) + "}")' 

#hex to integer to string

## 5. Learning
1. I learned about the 'imul' instruction in assemble and its format of multiplying bytes: destination = source1 * sourceb

2. I learned on how to navigate to another function other than main by following the edi or argument being called.
