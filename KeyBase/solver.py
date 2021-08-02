from Crypto.Cipher import AES
from Crypto.Util.number import *
import binascii

key_t = "a2824541d7b87474f6c9b43d68d0"
enc_a = "2031e2b4219ea750ba6a27f8dbe76555"
fk = "dca4"
enc = "374fccd3d532f29967b5c7a83972b7279aaf3866fd22298df1e66990fe9a4b1b"

tmp = "0123456789abcdef"
tmp_iv = b"A"*16
pl = b"a"*16
for k1 in tmp:
	print("k1=",k1)
	for k2 in tmp:
		for k3 in tmp:
			for k4 in tmp:
				key = key_t+k1+k2+k3+k4
				#print(key)
				key = binascii.unhexlify(key.encode())
				#print(key)
				cipher = AES.new(key, AES.MODE_CBC, tmp_iv)
				tmp_e = "00"*16+enc_a
				assert len(tmp_e)%32 == 0
				pt = cipher.decrypt(binascii.unhexlify(tmp_e))
				assert len(pt) == 32
				pt2 = pt[16:]
				bx = bytes_to_long(pt2)
				ct1 = bx^bytes_to_long(pl)
				cipher = AES.new(key, AES.MODE_CBC, tmp_iv)
				ct1 = long_to_bytes(ct1)
				while len(ct1)%16 != 0: ct1 = b"\x00"+ct1
				pt1 = cipher.decrypt(ct1)
				ax = bytes_to_long(pt1)^bytes_to_long(tmp_iv)
				iv = long_to_bytes(ax^bytes_to_long(pl))
				#print(iv)
				#print(len(iv))
				while len(iv) < 16: iv = b"\x00"+iv
				fipher = AES.new(key, AES.MODE_CBC, iv)
				flag = fipher.decrypt(binascii.unhexlify(enc))
				if b"CCTF" in flag:
					print(flag)

