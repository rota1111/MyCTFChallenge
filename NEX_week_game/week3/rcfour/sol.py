from sage.all import *
from Crypto.Util.number import *
from tqdm import *
import random
import time
import copy

# Quick hack
import sys

import sys
sys.path.append('./MT19937-Symbolic-Execution-and-Solver/source')

# Import symbolic execution
from MT19937 import MT19937, MT19937_symbolic

# Import XorSolver
from XorSolver import XorSolver

with open('cipher.txt') as f:
    c = f.readlines()
c = bytes.fromhex(c[0])
n_test = []
C = 1836184682169748070989133840042351952294695964110407163899271185441343825945147993536644513381704679641476812132479929805459665176655835013432635869984651


for k in trange(256):
    try:
        n_test = [i ^ k for i in c[-2496:]]
        rng_clone = MT19937(state_from_data = (n_test, 8))
        for _ in n_test: rng_clone()
        s = ''
        for i in range(512//32):
            s = bin(rng_clone())[2:].zfill(32) + s
        N = next_prime(int(s,2))
        d = inverse_mod(65537, N - 1)
        flag = long_to_bytes(int(pow(C,d,N)))
        if b'nex{' in flag:
            print(flag)
            break
    except:
        continue
