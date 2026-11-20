# <ascii-FTW> — Reversing

> Flag: <academy{ASCII_IS_EASY_6A73FC58}>

### Details:

This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program. 

Hint:

The combined range of hex-ascii for English alphabets and numerical digits is from 30 to 7A.

Online hex-ascii converters can be helpful.

## 1. Analysis

The challenge gives an ELF binary, 'asciiFTW', with no source code.

# command: ./asciiftw

return: The flag starts with 61

- 61 is the hex ASCII value of 'a', the first letter of the flag.
- It doesn't ask for an input, much less a password, so the flag must be in the binary.

## 2. The stack string in main

# command: objdump -d -M intel --disassemble=main asciiftw

'main' stores one byte at a time into a local buffer on the stack:

mov BYTE PTR [rbp-0x30], 0x61
mov BYTE PTR [rbp-0x2f], 0x63
mov BYTE PTR [rbp-0x2e], 0x61
mov BYTE PTR [rbp-0x2d], 0x64
...
mov BYTE PTR [rbp-0x12], 0x7d

- The offsets go up by one each time, so these 31 bytes are consecutive characters of one string, which can hold the flag.

- After that, 'printf' is called with only the first byte ('[rbp-0x30]'), which explains the output: 'The flag starts with 61'.

- The 'fs:0x28' instructions before and after 'main' are the stack canary from the compiler to prevent stack overflow. 


## 3. Dynamic Analysis   

For verfication, the results obtained through static analysis, GDB was used to inspect the program's memory during execution.

- Launching the debugger:
# command: gdb -q ./asciiftw

- A breakpoint was placed at main+0x97(address 0x1200), exactly after the instructions for storing the finals character in the stack.
# command: break *main+97
# command: run

- After that execution reached the breakpoint, the memory region containing the character array was examined using:
# command: x/s $rbp-0x30

- The /s format displays the contents of the specified memory address as a null-terminated string. 
- The address $rbp-0x30 corresponds to the beginning of the character array.

- The resulting memory contents confirmed the reconstructed string, demonstrating that the hex values identified in the disassembly correspond to the actual ASCII characters stored at runtime.

- For further verification, the individual bytes can be inspected using:
# command: x/31xb $rbp-0x30

- This displays 31 consecutive bytes in hex format, allowing direct comparison with the values.
## 4. Script and Explanation

# hex values stored in the consecutive storage of values in stack.
hex_values = [
    0x61, 0x63, 0x61, 0x64, 0x65, 0x6d, 0x79, 0x7b,
    0x41, 0x53, 0x43, 0x49, 0x49, 0x5f, 0x49, 0x53,
    0x5f, 0x45, 0x41, 0x53, 0x59, 0x5f, 0x36, 0x41,
    0x37, 0x33, 0x46, 0x43, 0x35, 0x38, 0x7d
]

flag = ""

# converts to string each hex value and stores a string in 'flag'.

for value in hex_values:
	flag += chr(value)

print(flag)


## 5. Learning
1. A flag can be built on the stack on byte at a time, so 'strings' may find nothing.
2. Constants in disassembly are hex.
3. I learned what stack canary instructions ('fs:0x28') are.
