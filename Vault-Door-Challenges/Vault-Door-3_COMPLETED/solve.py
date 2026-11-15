target = "jU5t_a_sna_3lpm15ge42_u_4_mbr248"
password = ["?"] * 32

#loop 1
for i in range(0,8):
	password[i] = target[i]

#loop 2
for i in reversed(range(8,16)):
	src = 23 - i
	password[src] = target[i]

#loop 3
for i in reversed(range(16,32,2)):
	src = 46 - i
	password[src] = target[i]

#loop 4
for i in reversed(range(17,31 + 1, 2)):
	password[i] = target[i]

print("academy{" + "".join(password) + "}")