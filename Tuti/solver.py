import gmpy2
from Crypto.Util.number import *

k = 246389259423689900229483388850933720271363907782961941639413620688310657308991195363798484778005049234253341752674411282663124201840620584781830032437353134292733496201534415265400175632719346764031781179041636
k2, ch = gmpy2.iroot(k,2)
#print(k2)
fac = [2,3,11,11,19,47,71,3449,11953,5485619,2035395403834744453,17258104558019725087,1357459302115148222329561139218955500171643099]
tt = 1
for h in fac: tt *= h
assert tt == int(k2)
s = pow(2,len(fac))
for i in range(s):
	tmp = bin(i)[2:]
	while len(tmp) < len(fac):
		tmp = "0"+tmp
	X = 1
	#Y = 1
	for j in range(len(tmp)):
		if tmp[j] == "1": X *= fac[j]
		#else: Y *= fac[j]
	x = X-1
	m1 = long_to_bytes(x)
	if b"CCTF" in m1:
		Y = 2*int(k2)//X
		y = Y+1
		m2 = long_to_bytes(y)
		print(m1+m2)
