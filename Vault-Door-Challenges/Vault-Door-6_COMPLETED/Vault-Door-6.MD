# vault-door-6 — Reversing

> Flag: academy{n0t_mUcH_h4rD3r_tH4n_x0r_0cb705e}

### Details:

"This vault uses an XOR encryption scheme."
Hint: if X ^ Y = Z, then Z ^ Y = X.
Source: `VaultDoor6.java`.

## 1. Analysis

The program checks that the password is 32 characters, then compares each byte, after XOR, to a stored array:

java
if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) return false;


Subtracting and comparing to 0 is the same as `(passBytes[i] ^ 0x55) == myBytes[i]`.
The key is one fixed value, `0x55`, for every byte.

## 2. The stored array

32 bytes in hex (`0x3b, 0x65, 0x21, 0xa, ...`).
Values like `0xa` are just `0x0a` without the leading zero.
All values are below `0x80`, so nothing is negative.

## 3. Script and Explanation

XOR undoes itself, so I XOR the stored bytes with the same key to get the password back.

python

my_bytes = [
    0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
    0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
    0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
    0xa , 0x65, 0x36, 0x37, 0x62, 0x65, 0x60, 0x30,
]
key = 0x55

result = "".join(chr(b ^ key) for b in my_bytes)
print(len(result))   # 32
print("academy{" + result + "}")


academy{n0t_mUcH_h4rD3r_tH4n_x0r_0cb705e}


## 4. Learning

1. XOR is its own inverse: if `a ^ k = b`, then `b ^ k = a`.
2. A loop like `buf[i] ^= key` in a decompiler means: run the same loop over the stored data.
