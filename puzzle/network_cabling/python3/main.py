def median(l):
    tmp = l
    tmp.sort()
    
    n = len(tmp)
    m = n // 2
    
    if n % 2:
        return tmp[m]
    else:
        return (tmp[m] + tmp[m-1]) // 2
        

n     = int(input())
x_    = []
y_    = []

for i in range(n):
    x, y = [int(j) for j in input().split()]
    x_.append(x)
    y_.append(y)
    
y_cable = median(y_)
cable = max(x_) - min(x_)
cable += sum([abs(y - y_cable) for y in y_])

print(cable)
