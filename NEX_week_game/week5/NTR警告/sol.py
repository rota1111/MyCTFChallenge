from Crypto.Cipher import AES
import re

n = 49
p = 3
q = 128
d = 3

Zx.<x> = ZZ[]
e = -44*x^48 + 59*x^47 - 47*x^46 + 22*x^45 + 48*x^44 + 30*x^43 - 37*x^42 + 33*x^41 - 15*x^40 - 26*x^39 + 10*x^38 + 54*x^37 + 47*x^36 + 21*x^35 + 49*x^34 + 55*x^33 + 41*x^32 + 46*x^31 - 23*x^30 - 41*x^29 + 63*x^28 - 61*x^27 - 10*x^26 - 52*x^25 - 13*x^24 - 56*x^23 + 33*x^22 + 40*x^21 - 32*x^20 - 7*x^19 - 26*x^18 + 25*x^17 - 36*x^16 + 57*x^15 + 6*x^14 - 32*x^13 + 40*x^12 - 7*x^11 - 15*x^10 - 13*x^9 - 22*x^8 + 34*x^7 - 38*x^6 + 10*x^5 - 11*x^4 + 58*x^3 + 22*x^2 + 21*x
h = 14*x^48 + 92*x^47 + x^46 + 95*x^45 + 115*x^44 + 119*x^43 + 10*x^42 + 48*x^41 + 11*x^40 + 117*x^39 + 19*x^38 + 84*x^37 + 36*x^36 + 3*x^35 + 16*x^34 + 87*x^33 + 58*x^32 + 84*x^31 + 63*x^30 + 84*x^29 + 27*x^28 + 77*x^27 + 7*x^26 + 12*x^25 + 80*x^24 + 127*x^23 + 117*x^22 + 55*x^21 + 13*x^20 + 86*x^19 + 64*x^18 + 118*x^17 + 11*x^16 + 86*x^15 + 12*x^14 + 89*x^13 + 109*x^12 + 28*x^11 + 6*x^10 + 72*x^9 + 68*x^8 + 22*x^7 + 126*x^6 + 121*x^5 + 104*x^4 + 111*x^3 + 40*x^2 + 2*x + 126


def balancedmod(f,q):
    g = list( ((f[i] + q//2) % q) - q//2 for i in range(n) )
    return Zx(g)

def cyclicconvolution(f, g):
    return (f*g) % (x^n-1)

def invertmodprime(f,p):
    T = Zx.change_ring(Integers(p)).quotient(x^n-1)
    return Zx(lift(1 / T(f)))

def invertmodpowerof2(f,q):
    assert q.is_power_of(2)
    g = invertmodprime(f,2)
    while True:
        r = balancedmod(cyclicconvolution(g,f),q)
        if r == 1: return g
        g = balancedmod(cyclicconvolution(g,2 - r),q)

def encrypt(message, publickey):
    r = rpoly()
    return balancedmod(cyclicconvolution(publickey, r) + message, q)

def decrypt(cipher,f,fp):
    # cipher=Zx(cipher)
    a=balancedmod(cyclicconvolution(f, cipher), q)
    m=balancedmod(cyclicconvolution(fp, a),p)
    return m

def attack(publickey):
    recip3 = lift(1/Integers(q)(3))
    publickeyover3 = balancedmod(recip3 * publickey,q)
    M = matrix(2 * n)
    for i in range(n):
        M[i,i] = q
    for i in range(n):
        M[i+n,i+n] = 1
        c = cyclicconvolution(x^i,publickeyover3)
        for j in range(n):
            M[i+n,j] = c[j]
    M = M.LLL()
    for j in range(2 * n):
        try:
            f = Zx(list(M[j][n:]))
            f3 = invertmodprime(f,3)
            return (f,f3)
        except:pass
    return (f,f)
donald = attack(h.coefficients(sparse=False))
m_ = decrypt(e,donald[0],donald[1])

def terms(poly_str):
    terms = []
    pattern = r'([+-]?\s*x\^?\d*|[-+]?\s*\d+)'
    matches = re.finditer(pattern, poly_str.replace(' ', ''))
    
    for match in matches:
        term = match.group()
        if term == '+x' or term == 'x':
            terms.append(1)
        elif term == '-x':
            terms.append(-1)
        elif 'x^' in term:
            coeff_part = term.split('x^')[0]
            exponent = int(term.split('x^')[1])
            if not coeff_part or coeff_part == '+':
                coeff = 1
            elif coeff_part == '-':
                coeff = -1
            else:
                coeff = int(coeff_part)
            terms.append(coeff * exponent)
        elif 'x' in term:
            coeff_part = term.split('x')[0]
            if not coeff_part or coeff_part == '+':
                terms.append(1)
            elif coeff_part == '-':
                terms.append(-1)
            else:
                terms.append(int(coeff_part))
        else:
            if term == '+1' or term == '1':
                terms.append(0)
                terms.append(-0)
    return terms

def gen_key(poly_terms):
    binary = [0] * 128
    for term in poly_terms:
        exponent = abs(term)
        if term > 0 and exponent <= 127:  
            binary[127 - exponent] = 1
    binary_str = ''.join(map(str, binary))
    hex_key = hex(int(binary_str, 2))[2:].upper().zfill(32)
    return hex_key
def gen_key(poly_terms):
    binary = [0] * 128
    for term in poly_terms:
        exponent = abs(term)
        if term > 0 and exponent <= 127:  
            binary[127 - exponent] = 1
    binary_str = ''.join(map(str, binary))
    hex_key = hex(int(binary_str, 2))[2:].upper().zfill(32)
    return hex_key

poly_terms = terms(str(m_))
key = bytes.fromhex(gen_key(poly_terms))
aes = AES.new(key = key, nonce=b'20250410', mode=AES.MODE_CTR)
c = b't\xf5\x17?\xc8\xc2\x87\xc4\xa5\xcc\xe3\x03\xc2\xb0\xa4\x1b\x07s\xb3\x9e\x96\x16v@\xbb\xbdc\x85\x9cY\xca'

print(aes.decrypt(c))