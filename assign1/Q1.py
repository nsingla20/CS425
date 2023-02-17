import random

# Run script : python3 Q1.py OR python Q1.py

# returns a random bit string of length k
def random_message(k):
    tmp=""
    for i in range(k):
        tmp += str(random.randint(0,1))
    return tmp

#gives the crc remainder on DATA using CRC_bits as divisor
def encode_rem(Data, CRC_bits):
    l = len(Data)
    initial_padding = (len(CRC_bits) - 1) * '0'
    input_padded_array = list(Data + initial_padding)
    while '1' in input_padded_array[:l]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(CRC_bits)):
            input_padded_array[cur_shift + i] = str(int(CRC_bits[i] != input_padded_array[cur_shift + i]))
    return ''.join(input_padded_array[l:])

def crc_check(Data, CRC_bits):
    """Calculate the CRC check of a string of bits using a chosen polynomial."""
    ans = encode_rem(Data,CRC_bits)
    return ('1' not in ans)

# inverts bits in string randomly
# chances that a bit is inverted in 25%
# So, it is possible that no error are introduced
def add_error(s):
    l = len(s)
    ls = list(s)
    el = random.choices([True,False],weights=[1,3],k=l)
    for i in range(l):
        if el[i]:
            ls[i] = str(1-int(ls[i]))
    print("Error pattern:\t\t\t",''.join(['1' if e else '0' for e in el]))
    return ''.join(ls)

k=10
print('k:',k)
P='110101'
print('P:',P)
mssg = random_message(k)
print('Message:\t\t\t',mssg)
crc_r = encode_rem(mssg,P)
print("CRC:\t\t\t\t",crc_r)
mssg_t = mssg+crc_r
print("Transmission message:\t\t",mssg_t)
mssg_e = add_error(mssg_t)
print("Message after adding errors:\t",mssg_e)
if crc_check(mssg_e,P):
    print("Frame accepted")
else:
    print("Frame rejected")

