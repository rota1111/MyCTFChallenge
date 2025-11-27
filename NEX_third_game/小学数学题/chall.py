from os import getenv
from decimal import Decimal, getcontext

getcontext().prec = 2000

flag = getenv('FLAG')

def read_xyz():
    while True:
        try:
            raw = input("Enter 🍎, 🍌, 🍍 (like 1, 2, 3): ").strip()
            x_str, y_str, z_str = [s.strip() for s in raw.split(',')]
            x = int(x_str)
            y = int(y_str)
            z = int(z_str)
            if x <= 0 or y <= 0 or z <= 0:
                print("❌ x, y, z must be positive integers.")
                continue
            return x, y, z
        except Exception as e:
            print(f"Invalid input format. Please try again. (Error: {e})")

def check_bit_length(x, y, z):
    return x.bit_length() > 256 and y.bit_length() > 256 and z.bit_length() > 256

def nearly_equal(a, b, eps=Decimal('1e-30')):
    return abs(a - b) < eps

def check_formula1(x, y, z):
    x, y, z = map(Decimal, (x, y, z))
    val = x / (y + z) + y / (x + z) + z / (x + y)
    return nearly_equal(val, Decimal(4))

def check_formula2(x, y, z):
    x, y, z = map(Decimal, (x, y, z))
    val = x / (y + z) + y / (x + z) + z / (x + y)
    return nearly_equal(val, Decimal(6))

def input_and_validate(n, used_x, formula_checker):
    for i in range(1, n + 1):
        print(f"\nRound {i}/{n}")
        x, y, z = read_xyz()

        if x in used_x:
            print("❌ Duplicate x detected. Exiting.")
            return False
        used_x.add(x)

        if not check_bit_length(x, y, z):
            print("❌ All numbers must have bit length > 256.")
            return False

        try:
            if not formula_checker(x, y, z):
                print("❌ Formula validation failed.")
                return False
        except Exception as e:
            print(f"❌ Error during formula check: {e}")
            return False

        print("✅ Passed validation.")
    return True

def main():
    used_x = set()
    if not input_and_validate(5, used_x, check_formula1):
        return
    if not input_and_validate(5, used_x, check_formula2):
        return

    print(f'🎉 Flag: {flag}')

if __name__ == "__main__":
    main()
