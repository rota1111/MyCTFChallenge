from Crypto.Cipher import AES
from secret import flag
import re

N = 49
p = 3
q = 128  
d = 3

assert q > (6 * d + 1) * p
R.<x> = ZZ[]
def generate_T(d1, d2):
    assert N >= d1 + d2
    s = [1] * d1 + [-1] * d2 + [0] * (N - d1 - d2)
    shuffle(s)
    return R(s)

def invert_mod_prime(f, p):
    Rp = R.change_ring(Integers(p)).quotient(x^N - 1)
    return R(lift(1 / Rp(f)))

def convolution(f, g):
    return (f * g) % (x^N - 1)

def lift_mod(f, q):
    return R([((f[i] + q // 2) % q) - q // 2 for i in range(N)])

def poly_mod(f, q):
    return R([f[i] % q for i in range(N)])

def invert_mod_pow2(f, q):
    assert q.is_power_of(2)
    g = invert_mod_prime(f, 2)
    while True:
        r = lift_mod(convolution(g, f), q)
        if r == 1:
            return g
        g = lift_mod(convolution(g, 2 - r), q)

def generate_message():
    flag = b'nex{ntru_is_OK_but_noooooo_ntr}'

    return R([randrange(p) - 1 for _ in range(N)])

def generate_key():
    while True:
        try:
            f = generate_T(d + 1, d)
            g = generate_T(d, d)
            Fp = poly_mod(invert_mod_prime(f, p), p)
            Fq = poly_mod(invert_mod_pow2(f, q), q)
            break
        except:
            continue
    h = poly_mod(convolution(Fq, g), q)
    return h, (f, g)

def encrypt_message(m, h):
    e = lift_mod(p * convolution(h, generate_T(d, d)) + m, q)
    return e

def save_ntru_keys():
    h, secret = generate_key()
    with open("pub_key.txt", "w") as f:
        f.write(str(h))
    m = generate_message()
    with open("priv.txt", "w") as f:
        f.write(str(m))
    e = encrypt_message(m, h)
    with open("enc.txt", "w") as f:
        f.write(str(e))

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

save_ntru_keys()

with open('priv.txt', 'r') as f:
    m = f.readline()

key = bytes.fromhex(gen_key(terms(m)))
aes = AES.new(key = key, nonce=b'20250410', mode=AES.MODE_CTR)
c = aes.encrypt(flag)
print(f"c = {c}")

"""
c = b't\xf5\x17?\xc8\xc2\x87\xc4\xa5\xcc\xe3\x03\xc2\xb0\xa4\x1b\x07s\xb3\x9e\x96\x16v@\xbb\xbdc\x85\x9cY\xca'
"""