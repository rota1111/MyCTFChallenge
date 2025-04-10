from sage.all import *
from Crypto.Util.number import *

p = 1693439189518226515119909025159836330583087622812188262879681776022531175345970863471558496694775985630815286786448928921
c = 209092369546870863493275734428957506356934671602159935711999755878840242877164144842923011716301342725793261770759825596
n = 62 - 5
pre = b'nex{'
c -= bytes_to_long(pre)*256**(n+1) + bytes_to_long(b'}')

l = []
c *= inverse_mod(256,p)
for i in range(n):
    c -= 93*256**i
    l.append(256**i)
l.append(-c)
l = matrix(l)
A = block_matrix([
    [matrix.identity(n+1), l.T],
    [0,p]
])
A[-2:-2] = 29
A[:,-1:] *= p
AL = A.LLL()
print(AL[0])
st = ''
for i in AL[0][:-2][::-1]:
    st += chr(93 + i)
print(st)