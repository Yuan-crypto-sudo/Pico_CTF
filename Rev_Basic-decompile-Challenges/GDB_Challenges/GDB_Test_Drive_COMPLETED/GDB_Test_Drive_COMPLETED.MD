# <GDB_Test_Drive> — Reversing

> Flag: <academy{d3bugg3r_dr1v3_4cc75120}>

### Details:

- The challenge provides a compiled binary 'gdbme' and set commands to type for using GDB to find the flag.

## 1. Analysis
Since the source code is not provided, GDB (GNU Debugger) was used to inspect and control the program as it runs.

`
main+94:  mov $0x186a0,%edi
main+99:  call sleep@plt
main+104: lea -0x30(%rbp),%rax
`

mov $0x186a0,%edi was written righth before call sleep@plt, which can indicate that
'100,000' is the argument to be used in 'sleep()'

It's discovered that there is a 'sleep' function that delays execution through GDB on call sleep@plt at main+99, and when 0x186a0 as the argument because the instruction immediately before it was mov $0x186a0,%edi, and %edi holds the first integer argument passed to a function.

the hex '0x186a0' represented '100,000' in seconds because the called function was sleep(), whose C function definition is unsigned int sleep(unsigned int seconds).

## 2. Commands Given
1. `layout asm` 			displays the program's assembly instructions.
2. `break *(main+99)` 		sets a breakpoint 99 bytes after the beginning of main.
3. `run` 					starts the program.
4. `jump *(main+104)` 	 	redirects execution to the specified address.

## 3. Dynamic Analysis   

1. `chmod +x gdbme` - to add permission to the file
2. `gdb -nx gdbme` - opens the binary in GNU debugger
3. `layout asm` - displays the assembly instructions
4. `break *(main+99)` - set a breakpoint where 'sleep()' gets called to pause te execution.
5. `run` - runs te program until te breakpoint.
6. `jump *(main+104)` - skips past the 'sleep()' call and continues with the remaining functions up until it gives up the flag.


## 4. Script and Explanation (None was used)

## 5. Learning
1. I learned to use te basic GDB commands for dynamic analysis on the assembly istructions.
2. I learned the benefits of using breakpoints. It's to avoid running unintended or unnecesary instructions, while jump to skip to a different address and continue execution.
3. In using Dynamic Analysis, a debugger can be used to observe its behavior and modify it execution process.
