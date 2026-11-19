expected = [
    0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4,
    0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86,
    0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xE1,
    0xD0, 0xC0, 0xC2, 0xE1, 0xC2, 0x94, 0xA4, 0x94,
]

#scrambled_swaps = [(1,2), (0,3), (5,6), (4,7), (0,1), (3,4), (2,5), (6,7)]

#for binary visualization only:
#for value in expected:
#    binary = format(value, '08b')  #0 for empty spaces, 8 for minimum digits, b for binary

def switch_bits(value, p1, p2):

    #masks create a 8-bit binary with a 1 on the positions set
    mask1 = 1 << p1
    mask2 = 1 << p2 

    #extracts the 2 bits
    bit1 = value & mask1
    bit2 = value & mask2 

    #remove original bits
    rest = value & ~(mask1 | mask2) 

    #calculate distance between positions
    shift = p2 - p1 

    #move extracted bits
    bit1_shifted = bit1 << shift
    bit2_shifted = bit2 >> shift 

    #combine the bits
    result = bit1_shifted | bit2_shifted | rest 

    return result

#reversed scramble sequence
def unscramble(value):
    reverse = [(6,7), (2,5), (3,4), (0,1), (4,7), (5,6), (0,3), (1,2)]

    #calls teh switch_bit function and inputs the reversed_sequence algorithm
    for p1, p2 in reverse:
        value = switch_bits(value, p1, p2)

    return value

password = ""

#calls the scrambled array and value for each values.
for value in expected:

    #creates a list of int value of the unscrabled password
    original = unscramble(value)

    #converts ilist into string
    password += chr(original)

#prints the given format according to the main function checking password
print("academy{" + password +"}")
