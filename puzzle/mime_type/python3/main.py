n = int(input())
q = int(input())
m = {}

for i in range(n):
    ext, mt = input().split()
    m[ext.lower()] = mt
    
for i in range(q):
    fname = input()
    size = len(fname)
    dot = -1
    
    for j in range(size):
        if fname[j] == '.':
            dot = j
        
    fext = fname[dot + 1:].lower()
    
    if dot == -1 or not(fext in m):
        print("UNKNOWN")
    else:
        print(m[fext])
