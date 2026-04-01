class Wheel:
    def __init__(self,string):
        self.string = string
        self.pos = 0
        self.length = len(string)

    def turn(self):
        self.pos +=1 
        if self.pos == self.length:
            self.pos = 0
    
    def get_Bit(self):
        return int(self.string[self.pos])

wheel0 = Wheel("0011")
wheel1 = Wheel("0011")
wheel2 = Wheel("0011")
wheel3 = Wheel("0011")
wheel4 = Wheel("0011")
wheel5 = Wheel("1011")
wheel6 = Wheel("1011")
wheel7 = Wheel("1011")
wheel8 = Wheel("1011")
wheel9 = Wheel("1011")

wheels = [wheel0,wheel1,wheel2,wheel3,wheel4,wheel5,wheel6,wheel7,wheel8,wheel9]

#  2T3O4HNM5LRGIPCVEZDBSYFXAWJ6UQK7
alphabet = {"2":0,
            "T":1,
            "3":2,
            "O":3,
            "4":4,
            "H":5,
            "N":6,
            "M":7,
            "5":8,
            "L":9,
            "R":10,
            "G":11,
            "I":12,
            "P":13,
            "C":14,
            "V":15,
            "E":16,
            "Z":17,
            "D":18,
            "B":19,
            "S":20,
            "Y":21,
            "F":22,
            "X":23,
            "A":24,
            "W":25,
            "J":26,
            "6":27,
            "U":28,
            "Q":29,
            "K":30,
            "7":31
            }


def print_wheel(wheel):
    for i in range(len(wheel.string)):
        print(wheel.get_Bit())
        wheel.turn()

def dec_to_bin(dec):
    bits = [0,0,0,0,0]
    for i in range(5):
        if dec%2 == 1:
            bits[4-i] = 1
        dec=dec>>1
    return bits

def bits_to_char(bits):
    value = 0
    for i in range(5):
        value=value<<1
        if bits[4-i] == 1:
            value+=1
    return list(alphabet)[value]


def handle_wheels():
    bits = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        bits[i] = wheels[i].get_Bit()
        wheels[i].turn()
    return bits


def encrypt_text(text):
    cipher = ""
    for i in range(len(text)):
        c_bits = dec_to_bin(alphabet.get(text[i]))
        b_bits = handle_wheels()

        for j in range(5):
            c_bits[j] = (c_bits[j] + b_bits[j])%2 # XOR bits 0-4
        if b_bits[5] == 1:
            c_bits[0],c_bits[4] = c_bits[4],c_bits[0]
        if b_bits[6] == 1:
            c_bits[0],c_bits[1] = c_bits[1],c_bits[0]
        if b_bits[7] == 1:
            c_bits[1],c_bits[2] = c_bits[2],c_bits[1]
        if b_bits[8] == 1:
            c_bits[2],c_bits[3] = c_bits[3],c_bits[2]
        if b_bits[9] == 1:
            c_bits[3],c_bits[4] = c_bits[4],c_bits[3]
        print(c_bits)
        cipher += bits_to_char(c_bits)
    return cipher



def decrypt_char(symbol):
    bits = dec_to_bin(alphabet.get(symbol))
    bits[0],bits[4] = bits[4],bits[0]
    bits[1],bits[3] = bits[3],bits[1]
    return bits

        
def print_modulus(plain,cipher,ind):
    counter = [0,0,0,0,0]
    all = [0,0,0,0,0]
    #total=0
    for k in range(ind):
        total=0
        for i in range(int(len(plain))):
            if i+k>=len(plain):break
            if (i)%ind == 0:
                #print(i+k)
                total+=1
                plain_bits = dec_to_bin(alphabet.get(plain[i+k]))
                cipher_bits = decrypt_char(cipher[i+k])
                for j in range(5):
                    counter[j] += (plain_bits[j]+cipher_bits[j])%2
        for j in range(5):
            counter[j] /= total
            all[j] += round(abs(counter[j]-0.5),2)
    for i in range(5):
        all[i] = round(all[i]/ind,2)
    for i in range(5):
        if all[i] >=0.0015:
            print(ind)
            print(all)
            print()
            break






c_bits = dec_to_bin(alphabet.get("F"))
#print_wheel(wheel1)

#print(alphabet.get("F"))
#print(c_bits)

#print(encrypt_text("FROM4"))

#print(bits_to_char([1,1,1,1,1]))
total = 0


#for i in range(1024):
#    bits = [(i >> j) & 1 for j in range(10)]
#    if try_encrypt("F","C",bits):
#        print(str(bits[0])+str(bits[1])+str(bits[2])+str(bits[3])+str(bits[4])+str(bits[5])+str(bits[6])+str(bits[7])+str(bits[8])+str(bits[9]))
#        total+=1
#print(total)
plain = open("gskrivin.txt").read()
cipher = open("gskrivut.txt").read()


#print(encrypt_text("A"))
#print(decrypt_char("L"))

#print_modulus("ABCABCABC","XYZXYZXYZ",3)


print_modulus(plain,cipher,47)
print_modulus(plain,cipher,53)
print_modulus(plain,cipher,59)
print_modulus(plain,cipher,61)
print_modulus(plain,cipher,64)
print_modulus(plain,cipher,65)
print_modulus(plain,cipher,67)
print_modulus(plain,cipher,69)
print_modulus(plain,cipher,71)
print_modulus(plain,cipher,73)

print_modulus(plain,cipher,48)
print_modulus(plain,cipher,49)
print_modulus(plain,cipher,55)
print_modulus(plain,cipher,57)
