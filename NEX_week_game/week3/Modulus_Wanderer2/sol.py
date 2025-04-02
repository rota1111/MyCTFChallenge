from Crypto.Util.number import *
C = ... 

k1m = (C[23]-C[22])**2-(C[24]-C[23])*(C[22]-C[21])
k2m = (C[36]-C[34])**2-(C[38]-C[36])*(C[34]-C[32])
m = gcd(k1m,k2m)
a = inverse_mod((C[23]-C[22]) % m,m)*(C[24]-C[23]) % m
b = (C[24]-a*C[23]) % m

seed = inverse_mod(a,m)*(C[0]-b) % m
flag = ""
for i in range(len(C)):
    seed = (a*seed + b) % m
    if C[i] == seed:
        flag += "0"
    else:
        flag += "1"
print(long_to_bytes(int(flag,2)))
