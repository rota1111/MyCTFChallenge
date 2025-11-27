import random
from sympy import nextprime
from Crypto.Util.number import bytes_to_long
from secret import flag

def rcfour(key, data):
    S = list([i % 255 for i in range(256)])
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    i = j = 0
    result = bytearray()
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i] = S[j]
        S[j] = S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(char ^ k)
    
    return bytes(result)

key = random.randbytes(256)
c = rcfour(key, bytes([random.getrandbits(8) for _ in range(50000)]))
with open('cipher.txt','w') as f:
    f.write(bytes.hex(c))

N = nextprime(random.getrandbits(512))
C = pow(flag,65537,N)
print(f"C = {C}")
"""
C = 1836184682169748070989133840042351952294695964110407163899271185441343825945147993536644513381704679641476812132479929805459665176655835013432635869984651
"""