min = float('Inf')
l = []

n = int(input())
for i in range(n):
    l.append(int(input()))

l.sort()

for i in range(n-1):
    d = l[i+1] - l[i]
    
    if d < min:
        min = d
        
print(min)
