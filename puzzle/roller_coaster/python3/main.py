places, rides, n = [int(i) for i in input().split()]
groups = [int(input()) for i in range(n)]

s = sum(groups)
if s <= places:
    print(rides * s)
else:
    i = 0
    l = []
    g = []
    loop = True
    gain = 0
    
    while rides and loop:
        if i in l:
            z = l.index(i)
            l = l[z:]
            g = g[z:]
            loop = False
        else:
            l.append(i)
            
            c = groups[i]
            x = 0
            
            while x + c <= places:
                x += c
                i = (i + 1) % n
                c = groups[i]
            
            g.append(x)
            
            gain += x
            rides -= 1
    
    gain += rides // len(l) * sum(g)
    gain += sum([g[k] for k in range(rides % len(l))])
    print(gain)
