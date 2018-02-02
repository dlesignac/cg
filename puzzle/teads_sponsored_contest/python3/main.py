def buildGraphFromInput():
    n = int(input())
    graph = []

    for i in range(n):
        x, y = [int(j) for j in input().split()]
        graph.append((x,y))

    return graph


def computeNumberOfNeighbors(graph):
    numberOfNeighbors = {}
    
    for x,y in graph:
        if not x in numberOfNeighbors:
            numberOfNeighbors[x] = 1
        else:
            numberOfNeighbors[x] += 1
        
        if not y in numberOfNeighbors:
            numberOfNeighbors[y] = 1
        else:
            numberOfNeighbors[y] += 1
    
    return numberOfNeighbors


def computeMinHeight(graph):
    minHeight = 0
    
    while graph:  
        i = 0
        numberOfNeighbors = computeNumberOfNeighbors(graph)
        numberOfVertices = len(graph)
        
        while i < numberOfVertices:
            x, y = graph[i]
            
            if numberOfNeighbors[x] == 1 or numberOfNeighbors[y] == 1:
                graph.pop(i)
                numberOfVertices -= 1
            else:
                i += 1
    
        minHeight += 1
    
    return minHeight


print(computeMinHeight(buildGraphFromInput()))
