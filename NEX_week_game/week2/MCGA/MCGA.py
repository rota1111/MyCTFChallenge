import random
from Crypto.Util.number import *
import os

flag = os.getenv('FLAG')
real = '关于下周就上完所有课了以为可以走了却发现还要多留几周考人文选修这件事'
flag1 = flag[:len(flag)//2]
flag2 = flag[len(flag)//2:]


def get_hex_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input, 16)
        except ValueError:
            print("Invalid input. Please enter a valid hexadecimal number.")


def first_task():
    random.seed(real)
    r = random.getrandbits(128)

    seed = get_hex_input("(TASK1) Give me the seed (hex):")

    if seed == bytes_to_long(real.encode()):
        print("Seed cannot be the same as the 'real' value.")
        exit(1)

    random.seed(seed)
    
    if r != random.getrandbits(128):
        print("Random number mismatch.")
        exit(1)
    
    print(f"flag1 = {flag1}")

def second_task():
    p = getPrime(256)
    print(f"p = {p}")

    m = get_hex_input("(TASK2): Enter your message (hex):")

    if real.encode() not in long_to_bytes(m):
        print("Error: The message does not contain the 'real' value.")
        exit(1)
    
    if pow(2, m, p) != 1:
        print("Error: pow(2, m, p) is not equal to 1.")
        exit(1)

    print(f"flag2 = {flag2}")

def main():
    first_task()
    second_task()

if __name__ == "__main__":
    main()
