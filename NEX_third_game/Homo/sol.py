from Crypto.Util.number import *
from pwn import *

io =  remote('219.216.65.41', 38900)
p = getPrime(512)
e = 65537
d = inverse(e, p - 1)
io.recvlines(2)
io.sendlineafter(b'Encryption (use x, e.g.: x+1):\n',f'pow(x, {e}, {p})')
io.sendlineafter(b'Decryption (inverse, e.g.: x-1):\n',f'pow(x, {d}, {p})')
io.recvlines(4)
print(io.recvline())
