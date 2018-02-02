n = int(input())

if n == 0:
    print(0)

temps = [int(i) for i in input().split()]

ind = 0
clt = abs(temps[0])

for i in range(1, n):
    t = abs(temps[i])
    
    if t < clt or (t == clt and temps[i] > temps[ind]):
        ind = i
        clt = t

print(temps[ind])
