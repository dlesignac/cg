class Node:
    def __init__(self):
        self.parent = []
        self.depth  = 0

def depth(node):
    if not node.parent:
        node.depth = 1
    else:
        max_d = 0
        
        for p in node.parent:
            d = depth(p)
                
            if d > max_d :
                max_d = d
        
        node.depth = max_d + 1

    return node.depth

n = int(input())
d = {}

max_d = 0

for i in range(n):
    x, y = [int(j) for j in input().split()]

    if not x in d:
        d[x] = Node()
    
    if not y in d:
        d[y] = Node()
    
    d[y].parent.append(d[x])

for i in d:
    d_ = depth(d[i])
    
    if d_ > max_d:
        max_d = d_

print(max_d)
