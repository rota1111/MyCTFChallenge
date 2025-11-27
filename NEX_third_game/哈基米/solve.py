from Crypto.Util.number import *

hash_str = '哈基米蛤集咪'

char_to_digit = {char: i for i, char in enumerate(hash_str)}
def decrypt(enc_str):
    digits = [str(char_to_digit[c]) for c in enc_str]
    print(''.join(digits))
    n = int(''.join(digits), 6)
    print(n)
    return long_to_bytes(n)

c = "蛤咪基哈集咪集咪咪集集基集集米哈基基蛤哈咪哈基蛤蛤咪咪基集蛤米哈蛤米米集蛤哈基基米哈集米哈哈米哈米咪基集蛤哈米基基米咪咪集米咪哈基米集集基蛤集哈集米集哈蛤哈米集蛤米蛤基蛤米咪哈咪蛤米蛤集咪基蛤哈基哈蛤哈蛤米米基"
print(decrypt(c))
