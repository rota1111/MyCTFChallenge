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
c = rcfour(key, random.randbytes(50000))
with open('cipher.txt','w') as f:
    f.write(bytes.hex(c))

N = nextprime(random.getrandbits(1024))
C = pow(flag,65537,N)
print(f"C = {C}")
"""
14723607368799001304654229394701074892602143770252793136897817353115641245557053373500216501582808157921671808596760438680320066539691097502487722359530500393197517064403381517351689962154929070981676797380735944094878278248021938331844835413142667587361817907845305429039937095327424442337495914745003362905
"""