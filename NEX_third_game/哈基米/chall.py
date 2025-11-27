from Crypto.Util.number import *

hash = '哈基米蛤集咪'
def to_base(n, base):
    digits = []
    while n:
        digits.append(hash[n % base])
        n //= base
    return digits[::-1]

def encrypt(s):
    s_int = bytes_to_long(s)
    return ''.join(to_base(s_int, 6))
print(encrypt(''))