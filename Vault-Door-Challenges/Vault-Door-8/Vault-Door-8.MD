# <Vault-Door-8> — Reversing

> Flag: <flag>

### Details:

This vault provides the java file source again itself. The password is scrambled through a bit_switching program.

Hint:

Draw a diagram to illustrate which bits are being switched in the scramble() method, then figure out a sequence of bit switches to undo it. You should be able to reuse the switchBits() method as is.

## 1. Analysis
The java source code is divided into 3 functions: input and check handling, scrambling sequence, and the bit_switching algorythm.

the scrambled password is given in the 'expected' array and each value is in hex 0xFF format, but python already recognizes it as an integer value and processes its binary 8-bit format when processed through bitwise operations.

## 2. <The 3 functions:>

# The main function as usual processes the input and the bool checkPassword.

System.out.print("Enter vault password: ");

if (a.checkPassword(f)) {
	System.out.println("Access granted."); 
} else {
	System.out.println("Access denied!");
}

# The scramble function contains a set of 8 bit exchanges for each binary value of each character in the password. This scrambles sequence appears to be the only algorythm that needs reversing.

c = switchBits(c,1,2);
c = switchBits(c,0,3); 
c = switchBits(c,5,6);
c = switchBits(c,4,7);
c = switchBits(c,0,1); 
c = switchBits(c,3,4);
c = switchBits(c,2,5);
c = switchBits(c,6,7);

# The author coded a function known as swicthBits which contains the logic of exchanging bits positions whenever it is called in scramble function. According to the hint given, the switchbit program doesn't require reversing and shall be reused in the solving process.

char mask1 = (char)(1 << p1);
char mask2 = (char)(1 << p2);
char bit1 = (char)(c & mask1);
char bit2 = (char)(c & mask2);
char rest = (char)(c & ~(mask1 | mask2));
char shift = (char)(p2 - p1);
char result = (char)((bit1<<shift) | (bit2>>shift) | rest);


## 3. Dynamic Analysis   (not used)

## 4. Script and Explanation

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

## 5. Learning

#Python stores the numerical values as integers. When you print a list directly, Python displays its integer elements in decimal notation.

# Representation     Python syntax   Data type
# Decimal                 244          int
# Hexadecimal             0xF4         int
# Binary               0b11110100      int
# Binary as text        "11110100"     str
# Hexadecimal as text     "F4"         str

You don't need to convert hexadecimal into decimal before converting it into binary.

Python already understands 0xF4 as the integer 244. You can directly use:

binary = format(0xF4, '08b')
