# vault-door-3 — Reversing

> Flag: academy{jU5t_a_s1mpl3_an4gr4m_4_u_2be258}

### Details:

"This vault uses for-loops and byte arrays."
Hint: make a table of each loop variable and the buffer index it writes to.
Source: `VaultDoor3.java`.

## 1. Analysis

The program does not compare my password directly. It first copies the characters into a `buffer` in a scrambled order, then compares the buffer to a fixed string:

java:
return s.equals("jU5t_a_sna_3lpm15ge42_u_4_mbr248");

So that string is the *scrambled* password, not the password itself.

## 2. The four loops

java:
for (i=0; i<8; i++)   buffer[i] = password.charAt(i);
for (; i<16; i++)     buffer[i] = password.charAt(23-i);
for (; i<32; i+=2)    buffer[i] = password.charAt(46-i);
for (i=31; i>=17; i-=2) buffer[i] = password.charAt(i);


- Loop 1 leaves positions 0-7 unchanged.
- Loop 2 reverses positions 8-15 (`i=8` reads 15, `i=9` reads 14, ...).
- Loop 3 fills the even positions 16-30 from the mirrored positions.
- Loop 4 fills the odd positions 17-31 unchanged.

Together they write every buffer slot exactly once, so the scramble is a permutation of positions and can be reversed.

## 3. Script and Explanation

If `buffer[i] = password[src]` and the buffer must equal the target, then `password[src] = target[i]`.

python:
target = "jU5t_a_sna_3lpm15ge42_u_4_mbr248"
password = ["?"] * 32

for i in range(0, 8):
    password[i] = target[i]
for i in range(8, 16):
    password[23 - i] = target[i]
for i in range(16, 32, 2):
    password[46 - i] = target[i]
for i in range(31, 16, -2):
    password[i] = target[i]

print("academy{" + "".join(password) + "}")

academy{jU5t_a_s1mpl3_an4gr4m_4_u_2be258}


## 4. Learning

1. A scramble that only moves characters can be undone.
2. Instead of reasoning backwards, replay the loops and record where each character came from.
3. Checking that no `?` remains and the length is 32 catches mistakes.
