from Crypto.Util.number import *
from secret import flag

class ComComComComplex:
    def __init__(self, value=[0,0,0,0]):
        self.value = value
    def __str__(self):
        s = str(self.value[0])
        for k,i in enumerate(self.value[1:]):
            if i >= 0:
                s += '+'
            s += str(i) +'ijk'[k]
        return s
    def __add__(self,x):
        return ComComComComplex([i+j for i,j in zip(self.value,x.value)])
    def __mul__(self,x):
        a = self.value[0]*x.value[0]-self.value[1]*x.value[1]-self.value[2]*x.value[2]-self.value[3]*x.value[3]
        b = self.value[0]*x.value[1]+self.value[1]*x.value[0]+self.value[2]*x.value[3]-self.value[3]*x.value[2]
        c = self.value[0]*x.value[2]-self.value[1]*x.value[3]+self.value[2]*x.value[0]+self.value[3]*x.value[1]
        d = self.value[0]*x.value[3]+self.value[1]*x.value[2]-self.value[2]*x.value[1]+self.value[3]*x.value[0]
        return ComComComComplex([a,b,c,d])
    def __mod__(self,x):
        return ComComComComplex([i % x for i in self.value])
    def __pow__(self, x, n=None):
        tmp = ComComComComplex(self.value)
        a = ComComComComplex([1,0,0,0])
        while x:
            if x & 1:
                a *= tmp
            tmp *= tmp
            if n:
                a %= n
                tmp %= n
            x >>= 1
        return a

p = getPrime(256)
m = ComComComComplex([bytes_to_long(flag[i:i+len(flag)//4+1]) for i in range(0,len(flag),len(flag)//4+1)])
e = 40716873
c = pow(m, e, p)

print(f"c = {c}")
print(f"p = {p}")

"""
c = 27433389502395453725899338833004533886973035074136307407390094566911519798866+61569532542060261432143754809950005548158824698595807553935486806698931022648i+17936840409307100393467976341375653546372779107111111673721565775819780552166j+87685620526500044941824099984199162386702300192762777453002915151143238662203k
p = 91518581093691360767792784582630168525478221031706879077746392024796315797173
"""