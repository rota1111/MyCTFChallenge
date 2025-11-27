from quantcrypt.kem import MLKEM_1024
from quantcrypt.cipher import KryptonKEM
from Crypto.Util.number import *
from pathlib import *
from os import urandom

flag=b'nex{xxxxxxxxxx}'
quant=MLKEM_1024()

for b in x:
	if b == '1':
		pkey,skey=quant.keygen()
	else:
		pkey, skey = urandom(quant.param_sizes.pk_size), urandom(quant.param_sizes.sk_size)
	f.write(skey)