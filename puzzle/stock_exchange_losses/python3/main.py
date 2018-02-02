n = int(input())
l = [int(i) for i in input().split()]

v = l[0]
min = 0
tmp = 0

for i in range(1,n):
    now = l[i] - v
    tmp += now
    
    if tmp < min:
        min = tmp
    elif tmp >= 0:
        tmp = 0
    
    v = l[i]

print(min)
