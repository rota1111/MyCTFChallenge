from pwn import *

io = remote('219.216.65.41',36429)
res1 = []
res2 = []

def solve1():
  R.<x, y, z> = QQ[]
  f = (x*(x+z)*(x+y) + y*(y+z)*(y+x) + z*(z+y)*(z+x)) - 4*(x+y)*(x+z)*(y+z)
  tran = EllipticCurve_from_cubic(f, None, true)
  tran_inv = tran.inverse()
  EC = tran.codomain()
  g = EC.gens()[0]
  P = g
  cout = 0
  while cout != 5:
    Pinv = tran_inv(P)
    _x = Pinv[0].numerator()
    _y = Pinv[1].numerator()
    _z = Pinv[0].denominator()
    if _x>0 and _y>0:
      if _x.bit_length() > 256 and _y.bit_length() > 256 and _z.bit_length() > 256:
        res1.append((_x, _y, _z))
        cout+=1
    P = P+g
  
def solve2():
  R.<x, y, z> = QQ[]
  f = (x*(x+z)*(x+y) + y*(y+z)*(y+x) + z*(z+y)*(z+x)) - 6*(x+y)*(x+z)*(y+z)
  tran = EllipticCurve_from_cubic(f, None, true)
  tran_inv = tran.inverse()
  EC = tran.codomain()
  g = EC.gens()[0]
  P = g
  cout = 0
  while cout != 5:
    Pinv = tran_inv(P)
    _x = Pinv[0].numerator()
    _y = Pinv[1].numerator()
    _z = Pinv[0].denominator()
    if _x>0 and _y>0:
      if _x.bit_length() > 256 and _y.bit_length() > 256 and _z.bit_length() > 256:
        res2.append((_x, _y, _z))
        cout+=1
    P = P+g
solve1()

for i in res1:
  io.recvline()
  io.recvline()
  io.sendlineafter('Enter 🍎, 🍌, 🍍 (like 1, 2, 3): '.encode(), ','.join(map(str, i)).encode())
  io.recvline()

solve2()

for i in res2:
  io.recvline()
  io.recvline()
  io.sendlineafter('Enter 🍎, 🍌, 🍍 (like 1, 2, 3): '.encode(), ','.join(map(str, i)))
  io.recvline()

io.recvline()
