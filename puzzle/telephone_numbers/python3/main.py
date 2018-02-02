class Node:
    def __init__(self):
        self.child = {}

root  = Node()
nodes = 0

n = int(input())
for i in range(n):
    phone = [i for i in input()]
    
    current = root
    
    for i in phone:
        if not i in current.child:
            current.child[i] = Node()
            nodes += 1
            
        current = current.child[i]

print(nodes)

