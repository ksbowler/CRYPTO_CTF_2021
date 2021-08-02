from Crypto.Util.number import *

def nextPrime(n):
    while True:
        n += (n % 2) + 1
        if isPrime(n):
            return n

G = open("g.enc","rb")
GG = G.readlines()
#print(GG)
g = b""
for gt in GG: g += gt
print(g)
H = open("h.enc","rb")
HH = H.readlines()
#print()
#print(HH)
h = b""
for ht in HH: h += ht
print(h)
#print()
G = bytes_to_long(g[:-1])
H = bytes_to_long(h[:-1])
g = []
h = []

while G != 0:
	g = [G%5] + g
	G //= 5

while H != 0:
	h = [H%5] + h
	H //= 5

print(g)
print(h)

lg = len(g)
lh = len(h)

#lg = len(f)*a + c
#lh = len(f)*b + c

import math

for c in range(lg):
	if isPrime(c):
		lf = math.gcd(lg-c,lh-c)
		a = (lg-c)//lf
		b = (lh-c)//lf
		if lf > 50 and isPrime(a) and isPrime(b):
			print("len(f)=",lf)
			print("a=",a)
			print("b=",b)
			print("c=",c)
			if nextPrime(lf) == a and nextPrime(a) == b and nextPrime(lf>>2) == c:
				print("Perfect!!!")
				break

#g,hを逆に
for i in range(len(g)-c-1,-1,-1):
	g[i] -= g[i+c]
	assert g[i] >= 0
for i in range(len(h)-c-1,-1,-1):

	h[i] -= h[i+c]
	assert h[i] >= 0
g = g[c:]
h = h[c:]
f = []
for i in range(0,len(g),a): f.append(g[i])
for i in range(len(f)-2,-1,-1):
	f[i] -= f[i+1]
	assert f[i] >= 0
flag = ''.join(str(v) for v in f)
print(flag)
print(long_to_bytes(int(flag,2)))




