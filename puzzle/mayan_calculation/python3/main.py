def tenbase(s, alpha, w, h):
    l = []
    
    while s != "":
        l.append(s[:(w+1) * h - 1])
        s = s[(w+1) * h:]
    
    l = l[::-1]
    x = 0
    
    for i in range(len(l) - 1, -1, -1):
        x += alpha.index(l[i]) * 20**i

    return x

def maybase(x, alpha):
    l = []
    
    if x == 0:
        l.append(alpha[0])
    
    while x != 0:
        a = x // 20
        b = x %  20
        
        l.append(alpha[b])
        x = a
    
    return "\n".join(l[::-1])
        

w, h = [int(i) for i in input().split()]
line = []
for i in range(h):
    line.append(input())

alpha = []
for i in range(len(line[0]) // w):
    s = ""
    f = True
    
    for j in range(w):
        if f:
            f = False
        else:
            s += "\n"
            
        s += line[j][i * w: i * w + w]

    alpha.append(s)

s1 = "\n".join([input() for i in range(int(input()))])
s2 = "\n".join([input() for i in range(int(input()))])

x1 = tenbase(s1, alpha, w ,h)
x2 = tenbase(s2, alpha, w, h)

o = input()
if   o == "+": print(maybase(x1 +  x2, alpha))
elif o == "-": print(maybase(x1 -  x2, alpha))
elif o == "*": print(maybase(x1 *  x2, alpha))
elif o == "/": print(maybase(x1 // x2, alpha))
