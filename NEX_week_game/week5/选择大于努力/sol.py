def f(x):
    x ^^= ((x >> 11) & 0xb451411bb451411b)
    x ^^= ((x << 13) & 0x451411cc451411cc)
    x ^^= ((x >> 17) & 0xaa191981aa191981)
    x ^^= ((x >> 19) & 0xb1919810b1919810)
    x ^^= ((x << 23) & 0x451411cd451411cd)
    x ^^= ((x >> 29) & 0xb451411ab451411a)
    x ^^= ((x << 31) & 0x451411cb451411cb)
    x ^^= ((x << 37) & 0xaa19198caa19198c)
    x ^^= ((x >> 41) & 0xb191981db191981d)
    x ^^= ((x << 43) & 0x451411ce451411ce)

    x ^^= ((x >> 10) & 0xb451411bb451411b)
    x ^^= ((x << 12) & 0x451411cc451411cc)
    x ^^= ((x >> 14) & 0xaa191981aa191981)
    x ^^= ((x >> 16) & 0xb1919810b1919810)
    x ^^= ((x << 20) & 0x451411cd451411cd)
    x ^^= ((x >> 24) & 0xb451411ab451411a)
    x ^^= ((x << 26) & 0x451411cb451411cb)
    x ^^= ((x << 28) & 0xaa19198caa19198c)
    x ^^= ((x >> 30) & 0xb191981db191981d)
    x ^^= ((x << 32) & 0x451411ce451411ce)

    return x 

def calc(n):
    x = 0x1122334455667788
    for _ in range(n):
        x = f(x)
    return x

T = []
for i in range(128):
    x = 1<<(127-i)
    x = f(x)
    T.append(Integer(x).digits(2,padto = 128)[::-1])
    
T = matrix(GF(2),T)
x = 0x1122334455667788
b = matrix(ZZ,[ int(i) for i in bin(x)[2:].rjust(128,'0')])
c = int(''.join([str(int(i)) for i in (b*T**11111111111111111111111111111111111111111111111)[0]]),2)
print('nex{%s}' % hex(c)[2:])
#nex{9b23fb81eaae279d}