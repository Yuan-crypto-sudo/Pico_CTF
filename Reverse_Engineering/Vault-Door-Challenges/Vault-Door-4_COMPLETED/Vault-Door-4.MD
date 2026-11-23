# vault-door-4 — Reversing

> Flag: academy{jU5t_4_bUnCh_0f_bYt3s_2a84ec9f20}

### Details:

"This vault uses ASCII encoding for the password."
Hints: use an ASCII table, and know the difference between octal, decimal and hexadecimal.
Source: `VaultDoor4.java`.

## 1. Analysis

The password is stored as a 32-byte array. The check compares my input's bytes to this array directly:

java
if (passBytes[i] != myBytes[i]) return false;


No transformation happens, so the password is just these bytes read as ASCII text.

## 2. The array

The bytes are written in four different notations, one row each:

- Row 1: decimal (`106, 85, 53, ...`)
- Row 2: hex (`0x55, 0x6e, ...`)
- Row 3: octal, with a leading 0 (`0142, 0131, ...`)
- Row 4: character literals (`'8', '4', 'e', ...`)

They are all disguises for ASCII values.

## 3. Script and Explanation

python
decimal = [106, 85, 53, 116, 95, 52, 95, 98]
hexa    = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
octal   = [0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o62, 0o141]
chars   = "84ec9f20"

result = "".join(chr(n) for n in decimal + hexa + octal) + chars
print(len(result))   # 32
print("academy{" + result + "}")

Java octal `0142` must be written `0o142` in Python.
My first answer was only 24 characters because I forgot the fourth row (already characters).
Checking `len(result)` against the loop bound (`i<32`) caught it.

## 4. Learning

1. Decimal, hex and octal are just different ways of writing the same byte.
2. `chr()` turns a number into its ASCII character.
3. Always compare the length of my result to the loop bound in the code.
