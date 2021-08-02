global p, alphabet
p = 71
alphabet = '=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ$!?_{}<>'

flag = "test_flag_0123456789abcd"
assert len(flag) == 24

def cross(m):
	return alphabet.index(m)

def prepare(msg):
    A = zero_matrix(GF(p), 11, 11)
    for k in range(len(msg)):
        i, j = 5*k // 11, 5*k % 11
        A[i, j] = cross(msg[k])
    #print("A=",A)
    return A

def keygen():
    R = random_matrix(GF(p), 11, 11)
    #print("R=",R)
    while True:
        S = random_matrix(GF(p), 11, 11)
        if S.rank() == 11:
            _, L, U = S.LU()
            return R, L, U

def encrypt(A, key):
	R, L, U = key
	S = L * U
	X = A + R
	Y = S * X
	E = L.inverse() * Y
	return E

A = prepare(flag)
key = keygen()
R, L, U = key
S = L * U

E = encrypt(A, key)

O = [[1,2],[3,4]]
#print(O)

Et = [[25,55,61,28,11,46,19,50,37,5,21],[20,57,39,9,25,37,63,31,70,15,47],[56,31,1,1,50,67,38,14,42,46,14],[42,54,38,22,19,55,7,18,45,53,39],[55,26,42,15,48,6,24,4,17,60,64],[1,38,50,10,19,57,26,48,6,4,14],[13,4,38,54,23,34,54,42,15,56,29],[26,66,8,48,6,70,44,8,67,68,65],[56,67,49,61,18,34,53,21,7,48,32],[15,70,10,34,1,57,70,27,12,33,46],[25,29,20,21,30,55,63,49,11,36,7]]


Kt = [[50,8,21,16,13,33,2,12,35,20,14],[36,55,36,34,27,28,23,21,62,17,8],[56,26,49,39,43,30,35,46,0,58,43],[11,25,25,35,29,0,22,38,53,51,58],[34,14,69,68,5,32,27,4,27,62,15],[46,49,36,42,26,12,28,60,54,66,23],[69,55,30,65,56,13,14,36,26,46,48],[25,48,16,20,34,57,64,62,61,25,62],[68,39,11,40,25,11,7,40,24,43,65],[54,20,40,59,52,60,37,14,32,44,4],[45,20,7,26,45,45,50,17,41,59,50]]


Wt = [[34,12,70,21,36,2,2,43,7,14,2],[1,54,59,12,64,35,9,7,49,11,49],[69,14,10,19,16,27,11,9,26,10,45],[70,17,41,13,35,58,19,29,70,5,30],[68,69,67,37,63,69,15,64,66,28,26],[18,29,64,38,63,67,15,27,64,6,26],[0,12,40,41,48,30,46,52,39,48,58],[22,3,28,35,55,30,15,17,22,49,55],[50,55,55,61,45,23,24,32,10,59,69],[27,21,68,56,67,49,64,53,42,46,14],[42,66,16,29,42,42,23,49,43,3,23]]

Qt = [[51,9,22,61,63,14,2,4,18,18,23],[33,53,31,31,62,21,66,7,66,68,7],[59,19,32,21,13,34,16,43,49,25,7],[44,37,4,29,70,50,46,39,55,4,65],[29,63,29,43,47,28,40,33,0,62,8],[45,62,36,68,10,66,26,48,10,6,61],[43,30,25,18,23,38,61,0,52,46,35],[3,40,6,45,20,55,35,67,25,14,63],[15,30,61,66,25,33,14,20,60,50,50],[29,15,53,22,55,64,69,56,44,40,8],[28,40,69,60,28,41,9,14,29,4,29]]

E = zero_matrix(GF(p), 11, 11)
for i in range(len(Et)):
    for j in range(len(Et[i])):
        E[i,j] = Et[i][j]
#print(E)
K = zero_matrix(GF(p), 11, 11) #LUL
for i in range(len(Kt)):
    for j in range(len(Kt[i])):
        K[i,j] = Kt[i][j]
#print(E)

W = zero_matrix(GF(p), 11, 11) #L^-1SSL
for i in range(len(Wt)):
    for j in range(len(Wt[i])):
        W[i,j] = Wt[i][j]
        
Q = zero_matrix(GF(p), 11, 11) #R^-1S**8
for i in range(len(Qt)):
    for j in range(len(Qt[i])):
        Q[i,j] = Qt[i][j]
        

U = W*(K.inverse())
X = U.inverse()*E
S2 = K*E*(X.inverse())
Rinv = Q*((S2**4).inverse())
R = Rinv.inverse()
A = X-R
print(X)
print()
print(R)
print()
print(A)

print("CCTF{",end="")
for i in range(11):
    for j in range(11):
        if A[i, j] != 0:
            print(alphabet[A[i, j]],end="")
print("}")
