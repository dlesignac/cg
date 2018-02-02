def conway(l):
    i = 0
    x = l[0]
    r = []
    
    while l:
        c = l.pop(0)
        
        if c == x:
            i += 1
        else:
            r.append(i)
            r.append(x)
            
            x = c
            i = 1
        
    r.append(i)
    r.append(x)

    return r
        
def nconway(r, n):
    l = [r]
    
    for i in range(n - 1):
        tmp = conway(l)
        l   = tmp

    return l


r = int(input())
n = int(input())

result = nconway(r, n)
print(" ".join(map(str, result)))
