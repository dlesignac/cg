import sys
import math

def children(node, graph):
    return graph[node]

def dijkstra(node_start, node_end, graph):
    vstd    = []
    dist    = []
    path    = []
    
    for i in range(n):
        dist.append(-1)
        vstd.append(0)
        path.append(-1)
    
    dist[node_start] = 0
    
    loop = 1
    while loop:
        min_dist = float('Inf')
        min_node = -1
        found = 0
        for node in range(n):
            if not vstd[node] and dist[node] != -1 and dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node
                found = 1

        if not found:
            return (float('Inf'), [])
            
        node = min_node
        vstd[node] = 1

        for child in children(node, graph):
            if not vstd[child] and (dist[node] + 1 < dist[child] or dist[child] == -1):
                dist[child] = dist[node] + 1
                path[child] = node
        
        if node == node_end:
            loop = 0
    
    return (dist[node_end], path)


graph   = {}
entry   = []

n, l, e = [int(i) for i in input().split()]

for i in range(n):
    graph[i] = []

for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(e):
    entry.append(int(input()))


while True:
    si = int(input())
    
    min_dist = float('Inf')
    min_path = []
    for i in range(e):
        (dist, path) = dijkstra(si, entry[i], graph)
        
        if dist < min_dist:
            min_dist = dist
            min_path = path
            min_entr = entry[i]
    
    last_node = min_path[min_entr]
    
    print("dist : {} -> {}\nnext : {}".format(dist, min_path, last_node), file=sys.stderr)
    
    graph[min_entr].remove(last_node)
    graph[last_node].remove(min_entr)
    
    print("{} {}".format(last_node, min_entr))
