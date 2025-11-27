from Crypto.Util.number import *

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

c0 = 27433389502395453725899338833004533886973035074136307407390094566911519798866
c1 = 61569532542060261432143754809950005548158824698595807553935486806698931022648
c2 = 17936840409307100393467976341375653546372779107111111673721565775819780552166
c3 = 87685620526500044941824099984199162386702300192762777453002915151143238662203
e = 40716873
p = 91518581093691360767792784582630168525478221031706879077746392024796315797173

c = ComComComComplex([c0,c1,c2,c3])
d = inverse_mod(e // 3, (p**2 - 1) // 3)
enc_ = pow(c, d, int(p))
PR.<a,b,c,d> = Zmod(p)[]
c0 = -2*a*b^2 - 2*a*c^2 - 2*a*d^2 + (a^2 - b^2 - c^2 - d^2)*a - enc_.value[0]
c1 = 2*a^2*b + (a^2 - b^2 - c^2 - d^2)*b - enc_.value[1]
c2 = 2*a^2*c + (a^2 - b^2 - c^2 - d^2)*c - enc_.value[2]
c3 = 2*a^2*d + (a^2 - b^2 - c^2 - d^2)*d - enc_.value[3]

from sage.matrix.matrix2 import Matrix
def resultant(f1, f2, var):
    return Matrix.determinant(f1.sylvester_matrix(f2, var))

h0 = resultant(c0, c1, d)
h1 = resultant(c0, c2, d)
h2 = resultant(c0, c3, d)

t0 = resultant(h0, h1, c)
t1 = resultant(h1, h2, c)

for r in resultant(t0, t1, b).univariate_polynomial().roots():
    a_ = r[0]
    if int(a_).bit_length() < 100:
        print(long_to_bytes(int(a_)).decode(),end="")
        break

for r in t0(a = a_).univariate_polynomial().roots():
    b_ = r[0]
    if int(b_).bit_length() < 100:
        print(long_to_bytes(int(b_)).decode(),end="")
        break
for r in h1(a = a_, b = b_).univariate_polynomial().roots():
    c_ = r[0]
    if int(c_).bit_length() < 100:
        print(long_to_bytes(int(c_)).decode(),end="")
        break

for r in c0(a = a_, b = b_, c = c_).univariate_polynomial().roots():
    d_ = r[0]
    if int(d_).bit_length() < 100:
        print(long_to_bytes(int(d_)).decode(),end="")
        break