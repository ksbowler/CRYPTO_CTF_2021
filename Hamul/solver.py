from Crypto.Util.number import *
n = 98027132963374134222724984677805364225505454302688777506193468362969111927940238887522916586024601699661401871147674624868439577416387122924526713690754043
c = 42066148309824022259115963832631631482979698275547113127526245628391950322648581438233116362337008919903556068981108710136599590349195987128718867420453399

primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71']
#print(pri.split())
#first 15~20 second 18~23
"""
ns = []
for i in range(15,20):
	for j in range(18,23):
		N = int(str(n)[:i]+str(n)[-j:])
		ch = True
		for p in primes:
			if N%int(p) == 0:
				ch = False
				break
		if ch:
			ns.append(N)
			print(N)
		for k in range(10):
			N = int(str(n)[:i]+str(k)+str(n)[-j:])
			ch = True
			for p in primes:
				if N%int(p) == 0:
					ch = False
					break
			if ch:
				ns.append(N)
				print(N)
		
print(ns)
#print(str(n)[18:]+str(n)[-21:])
#print(str(n)[17:]+str(n)[-22:])
#print(str(n)[19:]+str(n)[-20:])
"""

#tmp = [[6090827736891389,160942218689982828887],[19854645847343,493723905815686535686901],[518732143751265211,18897447197792828427013313],[25507980372892769,384299860397992093147],[142006095667351199,69030228950877125130862424357],[117040100660729969,8375516802359075095164469547],[1239524076733,79084492833526212988016434912482071]]

tmp = [[391111220047,25063748606238954787416469],[465963927380741639,21037493935292470637],[2647727654901734723 , 3702311783536219524841],[9324884768249686093 , 10512422984265378151],[2511932571814542137 , 39024587707209981139]]

for t in tmp:
	p = int(str(t[0])+str(t[1])+str(t[1])+str(t[0]))
	if n%p == 0:
		print("Find!!!")
		print(p)
		print(n//p)
		q = n//p
		phi = (p-1)*(q-1)
		e = 65537
		d = inverse(e,phi)
		m = pow(c,d,n)
		print(long_to_bytes(m))
