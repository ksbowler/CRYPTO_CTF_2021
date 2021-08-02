
import string, base64, math


ALPHABET = string.printable[:62] + '\\='

F = list(GF(64))

def keygen(l):
    key = [F[randint(1, 63)] for _ in range(l)] 
    #key = math.prod(key) # Optimization the key length :D
    return key

def maptofarm(c):
	assert c in ALPHABET
	return F[ALPHABET.index(c)]

def decrypt(msg, key):
    m64 = base64.b64encode(msg)
    for pkey in key:
        enct = ''
        for m in m64:
            enct += ALPHABET[F.index(pkey * maptofarm(chr(m)))]
        if enct[:4] == "805c":
            print(pkey)
            return pkey
            

# KEEP IT SECRET 
key = keygen(14) # I think 64**14 > 2**64 is not brute-forcible :P
print(key)

pkey = decrypt(b"CCTF{", key)
print("pkey=",pkey)
enc = "805c9GMYuD5RefTmabUNfS9N9YrkwbAbdZE0df91uCEytcoy9FDSbZ8Ay8jj"
base64_enc = b""
for i in range(len(enc)):
    for m in ALPHABET:
        if enc[i] == ALPHABET[F.index(pkey * maptofarm(m))]:
            base64_enc += m.encode()
            break
print(base64.b64decode(base64_enc))
        

