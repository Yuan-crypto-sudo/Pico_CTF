nums = [1096770097, 1952395366, 1600270708, 1601398833
        , 1716808014, 1734293602, 895574369, 909534257]
result = ""
for n in nums:
	result += chr((n >> 24) & 0XFF)
	result += chr((n >> 16) & 0XFF)
	result += chr((n >> 8) & 0XFF)
	result += chr(n & 0XFF)

print("academy{" + result + "}")