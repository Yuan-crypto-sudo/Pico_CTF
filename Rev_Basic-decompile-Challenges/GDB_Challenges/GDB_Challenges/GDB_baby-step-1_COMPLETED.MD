# <GDB_baby-step-1> — Reversing

> Flag: <academy{549698}>

### Details:

- The challenge provides a compiled binary 'debugger0_a'.

- Can you figure out what is in the eax register at the end of the main function? Put your answer in the academy flag format: academy{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be academy{17}.

Hints:
1. gdb is a very good debugger to use for this problem and many others!
2. main is actually a recognized symbol that can be used with gdb commands.

## 1. Analysis

- command: `file debugger0_a`

ELF					Linux executable format
64-bit				Designed for a 64-bit architecture
LSB					Little-endian byte order
PIE					Position Independent Executable
Dynamically linked	Uses external libraries
Not stripped		Contains symbol and debugging information

This 'not stripped' means the binary retains useful information about its functions and symbols, making it easier to investigate with GDB.

- command: `strings debugger0_a`
The only importnat thing strings gave up is 'main', since it only finds readable character sequences.	

## 2. Static Analysis

- command: `nm debugger0_a`

nm displays the symbols contained in an executable, including function names and their addresses.

- 0000000000001129 T main

This tells us:
- main is a function in the executable.
- Its address (in the binary's disassembly) is 0x1129.
- T means the symbol is located in the executable's code section.


- command: `objdump -d -M intel debugger0_a`

0000000000001129 <main>:
    1129: endbr64
    112d: push   rbp
    112e: mov    rbp,rsp
    1131: mov    DWORD PTR [rbp-0x4],edi
    1134: mov    QWORD PTR [rbp-0x10],rsi
    1138: mov    eax,0x86342
    113d: pop    rbp
    113e: ret

The program puts 0x86342 into the EAX register.
In x86-64, EAX is used to hold the return value of a function.
So main() appears to return the value 0x86342.

## 3. Dynamic Analysis   

Open the binary:

- `gdb debugger0_a`

Inside GDB:

- `break main`
- `run`

This pauses execution when main() begins.

Next, enter:

- `disassemble main`

This displays the instructions of main() inside GDB.

Now let's set a breakpoint at the instruction that loads the return value:

- `break *(main+15)`

+15 Because main starts at 0x1129, and the instruction mov eax,0x86342 is located at 0x1138.

The difference is:

0x1138 - 0x1129 = 0xF = 15

- continue

- nexti
This executes one assembly instruction.

- info registers eax
This displays the EAX register.

output: eax            0x86342             0x86342

since this is the value what main returns, I tested if this is in fact the flag, and it is.

## 4. Script and Explanation 

python3 -c 'print("academy{" + str(0x86342) + "}")'

## 5. Learning
1. I learned to use the objdump more in analyzizng the assembly instructions of compiled binary programs, expecially the main function.
2. I learned the 'nm' tool which shows the main functions, addresses, and other executables.
3. I learned to use the nexti tool in GDB to execute one assembly instruction, and also the 'info registers eax' to extract the value i the register.
