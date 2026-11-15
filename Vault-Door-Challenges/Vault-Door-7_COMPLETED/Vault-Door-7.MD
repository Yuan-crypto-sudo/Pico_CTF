# vault-door-7 — Reversing

> Flag: academy{A_b1t_0f_b1t_sh1fTiNg_8b5aaa66d1}

### Details:

"This vault uses bit shifts to convert a password string into an array of integers."
Hints: use a decimal/hex converter and an ASCII table.
Source: `VaultDoor7.java`.

## 1. Analysis

The password is 32 characters. `passwordToIntArray` packs every 4 characters into one 32-bit integer, producing 8 integers. `checkPassword` compares those 8 integers to stored values (`x[0] == 1096770097`, ...).

## 2. The packing

java

x[i] = hexBytes[i*4]   << 24
     | hexBytes[i*4+1] << 16
     | hexBytes[i*4+2] << 8
     | hexBytes[i*4+3];


Each character is one byte. The shifts move the 1st character into the top byte, the 2nd into the next, and so on,
and `|` glues them together.

Converting a stored number to hex shows the bytes clearly:


hex(1096770097) = 0x415f6231  ->  41 5f 62 31  ->  A _ b 1


All characters are plain ASCII, so there are no negative-byte problems.

## 3. Script and Explanation

To reverse the packing, I extract each byte with a shift and a mask:

python

nums = [1096770097, 1952395366, 1600270708, 1601398833,
        1716808014, 1734293602, 895574369, 909534257]

result = ""
for n in nums:
    for shift in (24, 16, 8, 0):
        result += chr((n >> shift) & 0xFF)

print(len(result))   # 32
print("academy{" + result + "}")


academy{A_b1t_0f_b1t_sh1fTiNg_8b5aaa66d1}


## 4. Learning

1. Packing is `(a << 24) | (b << 16) | (c << 8) | d`, and unpacking is `(n >> shift) & 0xFF`.
2. Two hex digits are exactly one byte, so hex is the natural way to read packed data.
