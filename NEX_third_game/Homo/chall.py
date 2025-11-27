import random
from os import getenv

flag = getenv('FLAG')

def main():
    a, b, c = [random.randint(1, 2**128) for _ in range(3)]
    
    print("Calculate product of three data points securely")
    print("Provide encryption/decryption functions")
    
    f_enc = input('Encryption (use x, e.g.: x+1):\n')
    f_dec = input('Decryption (inverse, e.g.: x-1):\n')
    
    safe = 'powx0123456789+-*/=()%, '
    if any(c not in safe for c in f_enc) or any(c not in safe for c in f_dec):
        print('Unsafe characters')
        return
    print('1. Safe')
    
    try:
        enc = lambda x: eval(f_enc)
        dec = lambda x: eval(f_dec)
    except:
        print('Invalid function syntax')
        return
    
    test = 114514
    try:
        if enc(test) == test or enc(test) == -test:
            print('Encryption must change value')
            return
    except:
        print('Encryption failed')
        return
    print('2. Encryption ok')
    
    try:
        if dec(enc(test)) != test:
            print('Decryption must reverse encryption')
            return
    except:
        print('Decryption failed')
        return
    print('3. Inverse ok')
    
    try:
        encrypted_prod = enc(a) * enc(b) * enc(c)
        if dec(encrypted_prod) != a * b * c:
            print("Product mismatch")
            return
    except:
        print('Product calculation failed')
        return
    
    print('4. All checks passed!')
    print(f'Flag: {flag}')

if __name__ == "__main__":
    main()
