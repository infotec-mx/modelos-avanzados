from collections import OrderedDict

W = {
    ("A", "B"):10, ("A", "C"):4, ("A", "D"):1, ("A", "E"):10, 
    ("B", "D"):1,
    ("C", "D"):4, ("C", "G"):3,
    ("D", "E"):7, ("D", "F"):10, ("D", "G"):7,
    ("E", "F"):8, ("E", "G"):5,
    ("F", "G"):3
}

sorted_E = sorted(W.items(), key=lambda x: x[1])

A = set()
V = ["A","B","C","D","E","F","G"]
S = {x:set([x]) for x in V}

def find_set(x):
    for k,v in S.items():
        if x in v:
            return k

def union(x,y):
    kx = find_set(x)
    ky = find_set(y)
    S[kx] = S[kx].union(S[ky])
    del S[ky]

for e, w in sorted_E:
    u, v = e
    if find_set(u)!=find_set(v):
        A.add(e)
        union(u,v)

print(A)
costo = sum(W[e] for e in A)
print(costo)    
