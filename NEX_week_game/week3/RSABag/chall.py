from Crypto.Util.number import *
from secret import flag

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 65537

sum = 0
for idx, chr in flag:
    for _ in range(chr):
        sum += pow(pow(idx + 20250313,e,n))

print(f"n = {n}")
print(f"e = {e}")
print(f"sum = {sum}")
