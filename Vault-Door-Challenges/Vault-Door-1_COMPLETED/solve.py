import re

src = open("VaultDoor1.java").read()
pairs = re.findall(r"charAt\((\d+)\)\s*==\s*'(.)'", src)

password = ["?"] * 32
for idx, ch in pairs:
	password[int(idx)] = ch

print("academy{" + "".join(password) + "}")