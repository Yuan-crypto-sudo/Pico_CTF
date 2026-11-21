# <GDB_baby-step-2> — Reversing

> Flag: academy{307019}

### Details:

- Compiled binary file: 'debugger0_b'.

- Can you figure out what is in the eax register at the end of the main function? Put your answer in the academy flag format: academy{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be academy{17}. Debug this

Hints
1. You could calculate eax yourself, or you could set a breakpoint for after the calculcation and inspect eax to let the program do the heavy-lifting for you.

## 1. Analysis

- command: `file debugger0_b`

ELF					Linux executable format
64-bit				Designed for a 64-bit architecture
LSB					Little-endian byte order
PIE					Position Independent Executable
Dynamically linked	Uses external libraries
Not stripped		Contains symbol and debugging information

This 'not stripped' means the binary retains useful information about its functions and symbols, making it easier to investigate with GDB.


## 2. Static Analysis

- command: `nm debugger0_b`
- return: `401020 T _start`


This tells us:
- main is a function in the executable.
- Its address (in the binary's disassembly) is 0x401020.
- T means the symbol is located in the executable's code section.


- command: `objdump -d -M intel debugger0_a`

0000000000401106 <main>:
  401106:       f3 0f 1e fa             endbr64
  40110a:       55                      push   rbp
  40110b:       48 89 e5                mov    rbp,rsp
  40110e:       89 7d ec                mov    DWORD PTR [rbp-0x14],edi
  401111:       48 89 75 e0             mov    QWORD PTR [rbp-0x20],rsi
  401115:       c7 45 fc da e0 01 00    mov    DWORD PTR [rbp-0x4],0x1e0da
  40111c:       c7 45 f4 5f 02 00 00    mov    DWORD PTR [rbp-0xc],0x25f
  401123:       c7 45 f8 00 00 00 00    mov    DWORD PTR [rbp-0x8],0x0
  40112a:       eb 0a                   jmp    401136 <main+0x30>
  40112c:       8b 45 f8                mov    eax,DWORD PTR [rbp-0x8]
  40112f:       01 45 fc                add    DWORD PTR [rbp-0x4],eax
  401132:       83 45 f8 01             add    DWORD PTR [rbp-0x8],0x1
  401136:       8b 45 f8                mov    eax,DWORD PTR [rbp-0x8]
  401139:       3b 45 f4                cmp    eax,DWORD PTR [rbp-0xc]
  40113c:       7c ee                   jl     40112c <main+0x26>
  40113e:       8b 45 fc                mov    eax,DWORD PTR [rbp-0x4]
  401141:       5d                      pop    rbp
  401142:       c3                      ret


- The function has a loop that calculates the value before putting it into eax and returning it:

Notice that in address '0x401123', it initializes a variables to 0, and later at '0x401132', this increases by 1, this appears to be an incrementation.

Notice that in address '0x401136', the variable eralier which we can call 'counter' is assigned to into EAX. then in the following address, EAX is compared to another variable, which in address '40111c' was actually assigned to a hex value '0x25f' or '607' in decimal.

In address '40113c' jl is jump if less, which in this case if EAX is less than the 'rbp-0xc]', then it jumps back to a previous address, namely '40112c'

In x86-64, EAX is used to hold the return value of a function.
So main() appears to return the value 0x86342.

- Pdeudocode representation:

int total = 0x1e0da;
int limit = 0x25f;
int counter = 0;

while (counter < limit)
{
    total += counter;
    counter++;
}

return total;


## 3. Dynamic Analysis   

Open the binary:

- `gdb debugger0_b`

Inside GDB:

- `break main`
- `run`

This pauses execution when main() begins.

Next, enter:

- `disassemble main`

This displays the instructions of main() inside GDB.

Now let's set a breakpoint at the instruction that loads the return value:

- `break *(main+39)`

+39 Because main starts at 0x1129, and the instruction mov eax,0x86342 is located at 0x1138.

- continue

- nexti
This executes one assembly instruction.

- info registers eax
This displays the EAX register.

output: eax            0x4af4b             0x4af4b

since this is the value what main returns, I tested if this is in fact the flag, and it is.

## 4. Script and Explanation 

python3 -c 'print("academy{" + str(0x4af4b) + "}")'

## 5. Learning
1. Since this challenge is very siilar to baby-step-1, I learned to practice my previous tools from then, to be more fluent in it.
2. I learned to read a loop in assembly, first look for incrementation, comparison, and jl back to a previous address.
