from Crypto.Util.number import *
from secret import flag
import random

class prng:     
    def __init__(self, seed): 
        self.state = seed
        self.p = getPrime(256)
        self.a = random.randint(1,self.p)
        self.b = random.randint(1,self.p)
    def next(self): 
        self.state = (self.state * self.a + self.b) % self.p
        return self.state
    
lcg = prng(seed=bytes_to_long(flag))
print(f"hint1 = {lcg.next()}")

for _ in range(9): 
    lcg.next()
print(f'hint2 = {lcg.next()}')
print(f'a = {lcg.a}')
print(f'p = {lcg.p}')

"""
hint1 = 22126701685602448167153832064764403297274733309207994531721460922137730181263
hint2 = 5876222187265536012720939816304551139744973373899661196587843114977386227647
a = 45050661441957622790575103855445161637213342339326319451297390136793503480151
p = 62520448412578189384348150589336657827821981805797503110824753389166180072583
"""