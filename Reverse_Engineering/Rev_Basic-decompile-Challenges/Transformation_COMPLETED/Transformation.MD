# <Transformation> — Reversing

> Flag: <academy{16_bits_inst34d_of_8_790ba37e}>

### Details:

file name: enc

This is a transformation that combines two characters into one Unicode character, which packs two 8-bit characters into one 16-bit character.

given python expression:
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## 1. Analysis

- The given python expression above can be translated into this algebraic formula:
C = (A << 8) + B


- command: file enc
return: enc: Unicode text, UTF-8 text, with no line terminators

- This explain why './' didnt work. It was because this is not a program, rather it is a output of a program.


## 2. Solving

- command: xxd enc
return: 
address     hex bytes                              ASCII text representation

00000000: e685 a3e6 85a4 e695 ade7 a5bb e384 b6e5  ................
00000010: bda2 e6a5 b4e7 8d9f e6a5 aee7 8db4 e38c  ................
00000020: b4e6 919f e6bd a6e5 bcb8 e5bc b7e3 a4b0  ................
00000030: e689 a1e3 8cb7 e695 bd                   .........

- The continuous pattern of e# 8# a# indicates a 3-byte UTF-8 encoding.
- The '...........' means they're non-ASCII bytes.

- To decode the bytes, we would have to convert each bytes into their unicode integer value, and reverse the pyhton logic formula given.

python given: ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
 
- The << 8 and + also tells us that this was originally 2 8-bit characters combined into a 16-bit character.

## 3. Dynamic Analysis

#this command was used to analyze the python script made by me, because there is no program given for analysis.
- command: python3 -m pdb unicode-to-string.py

#To view the python script:
- command: ll

#create a breakpoint for running live python code
- command: b 19

#continue
- command: c
return: 'academy{16_bits_inst34d_of_8_790ba37e}'

#cardinality count
- command: p len(flag)
return: 38

#continue
return: academy{16_bits_inst34d_of_8_790ba37e}

## 4. Script and Explanation

with open("enc", "r", encoding="utf-8") as file:
	encoded = file.read()

print("Number of encoded characters:", len(encoded))

flag = ""

for character in encoded:
	value = ord(character)

	char1 = value >> 8
	char2 = value & 0xFF

	flag += chr(char1)
	flag += chr(char2)

#shortcut: "".join(chr(ord(c) >> 8) + chr(ord(c) & 0xFF) for c in encoded)

print(flag)

## 5. Learning

- pdb can be used for dynamic analysis instead of gdb when the given file is not a program, and the script is intended to be analyzed instead.

- xxd can be used to analyze hex dump files.

- << 8 is necessary for adding 8-bits to prevent collision when using bitwise operations.

Operation	Meaning
ord()		Converts a character into its Unicode integer value
<< 8		Shifts the binary representation 8 bits to the left
+			Adds the second character's integer value
chr()		Converts the resulting integer into a Unicode character
