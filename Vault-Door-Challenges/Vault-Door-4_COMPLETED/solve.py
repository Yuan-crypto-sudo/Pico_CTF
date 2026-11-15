decimal = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98]
hexa = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
octal = [0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o62 , 0o141]
chars = "84ec9f20"

decimal_string = "".join(chr(n) for n in decimal)
hexa_string = "".join(chr(n) for n in hexa)
octal_string = "".join(chr(n) for n in octal)

print("academy{" + decimal_string + hexa_string + octal_string + chars +"}")