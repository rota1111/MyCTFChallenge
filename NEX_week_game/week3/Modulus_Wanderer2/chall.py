from Crypto.Util.number import *
from secret import flag
from os import urandom

assert flag[:4] == b'nex{'

class prng:     
    def __init__(self, seed = getPrime(256)): 
        self.state = seed
        self.p = getPrime(256)
        self.a = urandom.randint(1,self.p)
        self.b = urandom.randint(1,self.p)
    def next(self): 
        self.state = (self.state * self.a + self.b) % self.p
        return self.state

flag = [bin(2)[2:].ljust(8,'0') for i in flag]
C = []
pr = prng()
for i in flag:
    if i == 0:
        C.append(pr.next())
    else:
        C.append(urandom.randint(0,2**256))

print(f"C = {C}")