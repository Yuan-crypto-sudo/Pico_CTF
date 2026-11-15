# vault-door-1 — Reversing

> Flag: academy{d35cr4mbl3_tH3_cH4r4cT3r5_45ebc3}

### Details:

"This vault uses some complicated arrays!" Source: `VaultDoor1.java`.

Hint:
Look up the charAt() method online.

## 1. Analysis

Java source again. `main` strips `academy{` and `}`, then calls `checkPassword`. This time there is no full password string in the code.

## 2. The check

        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == 'b' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == 'c' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == 'e' &&
               password.charAt(26) == '4' &&
               password.charAt(31) == '3';


`charAt(n)` returns the character at position `n`, counting from 0. The password is split into 32 single-character checks, written in shuffled order. Each line still says exactly which character goes in which position, so the password is determined.

## 3. Script and Explanation

python:
import re

src = open("VaultDoor1.java").read()
pairs = re.findall(r"charAt\((\d+)\)\s*==\s*'(.)'", src)

password = ["?"] * 32
for idx, ch in pairs:
    password[int(idx)] = ch

print("academy{" + "".join(password) + "}")


The regex extracts every `(index, character)` pair. The loop puts each character into its numbered slot. So, if a `?` were left in the output, I would know a slot was missed.


academy{d35cr4mbl3_tH3_cH4r4cT3r5_45ebc3}


## 4. Learning

1. `charAt` is zero-indexed.
2. When a check is scattered over many lines, extract the data with a regex and rebuild it with a script instead of doing it manually.
