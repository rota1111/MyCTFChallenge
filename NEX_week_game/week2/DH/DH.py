from Crypto.Util.number import *
import random
import os

flag = os.getenv('FLAG')
m = bytes_to_long(flag.encode())

def generate_key_pair(p, g=2):

    private_key = random.randint(2, p - 1)
    public_key = pow(g, private_key, p)
    return private_key, public_key

def DH(p, g=2):

    A_priv, A_pub = generate_key_pair(p, g)
    B_priv, B_pub = generate_key_pair(p, g)

    shared_key_A = pow(B_pub, A_priv, p)
    shared_key_B = pow(A_pub, B_priv, p)

    assert shared_key_A == shared_key_B, "Key exchange failed: shared keys do not match!"

    return shared_key_A, A_pub, B_pub

try:
    p = int(input("Enter a number p: "))

    shared_key, A_pub, B_pub = DH(p)

    ciphertext = m * shared_key % p

    print(f"C = {ciphertext}")
    print(f"A_pub = {A_pub}")
    print(f"B_pub = {B_pub}")
except Exception as e:
    print(f"An error occurred: {e}")
