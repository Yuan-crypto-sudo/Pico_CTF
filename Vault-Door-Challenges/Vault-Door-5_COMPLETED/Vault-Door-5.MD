# vault-door-5 — Reversing

> Flag: academy{c0nv3rt1ng_fr0m_ba5e_64_3cc8a9d6}

### Details:

Source: `VaultDoor5.java`. The password goes through two encodings and is compared to a stored string.

## 1. Analysis

java
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTMzJTYzJTYzJTM4JTYxJTM5JTY0JTM2";
        return base64Encoded.equals(expected);



My input is first URL-encoded, then that result is base64-encoded. `expected` is the final base64 string.

## 2. What each step does

`urlEncode` writes every byte as `%` plus two hex digits (format `%%%2x`), even for letters.
For example, `c` becomes `%63`.

The stored string starts with `JTYz...`, which looks like base64. Decoding it gives `%63%30...`,
which confirms the URL-encoded layer inside.

## 3. Script and Explanation

The Java applies URL encoding, then base64. To undo it, reverse the order: base64-decode first, then URL-decode.

python

import base64
from urllib.parse import unquote

expected = ("JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
            "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
            "JTM0JTVmJTMzJTYzJTYzJTM4JTYxJTM5JTY0JTM2")

step1 = base64.b64decode(expected).decode()
result = unquote(step1)
print(len(result))   # 32
print("academy{" + result + "}")


academy{c0nv3rt1ng_fr0m_ba5e_64_3cc8a9d6}


## 4. Learning

1. With layered encodings, undo the outermost layer first (reverse order).
2. `%XX` is one ASCII byte in hex.
3. Base64 strings are recognizable by their alphabet and usually start with patterns like `JT` when they hold `%` signs.
