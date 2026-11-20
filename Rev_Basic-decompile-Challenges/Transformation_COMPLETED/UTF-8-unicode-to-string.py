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
