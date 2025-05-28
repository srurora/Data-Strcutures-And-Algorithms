#  Usually, a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary.
#  defaultdict allows that if a key is not found in the dictionary, then instead of a KeyError being thrown, 
#  a new entry is created. The type of this new entry is given by the argument of defaultdict

# import dictionary for graph 
from collections import defaultdict
from collections import deque

graph = defaultdict(list)

#for adjancency list
def addEdge(graph, v, u):
    graph[u].append(v)

def generateEdges(graph):
    edges =[]
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges


addEdge(graph, 'a' , 'b')
addEdge(graph, 'a' , 'c')
addEdge(graph, 'a' , 'd')
addEdge(graph, 'b' , 'c')
addEdge(graph, 'c' , 'd')
addEdge(graph, 'c' , 'b')
addEdge(graph, 'c' , 'd')
addEdge(graph, 'd' , 'a')
addEdge(graph, 'd' , 'c')

print("Adjancency List:")
print(generateEdges(graph))

# Undirected graph
def create_adjacency_matrix(V, edges):
    # Initialize an empty V x V matrix with all zeros
    matrix = [[0] * V for _ in range(V)]
    
    # Populate the matrix based on the edges
    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1  
    
    return matrix

print("Adjancency Matrix:")
# Example 1: Undirected graph
V1 = 3
edges1 = [(0, 1), (1, 2), (2, 0)]
adj_matrix1 = create_adjacency_matrix(V1, edges1)
for row in adj_matrix1:
    print(row)
print()


def DFS_recusrsive(graph, node, visited = None):
    if visited is None: visited = set()
    visited.add(node)
    print(node, end = " ") #process the node

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            DFS_recusrsive(graph, neighbor, visited)

def DFS_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end = " ")
            visited.add(node)
            stack.extend(graph[node])

def BFS(graph, start):
    visited = set()
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end = " ")
            visited.add(node)
            q.extend(graph.get(node, []))

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}
    #     A
    #    / \
    #   B   C
    #  / \  / \
    # D   E F  G
    #    |
    #    H

print("DFS Recursive:")
DFS_recusrsive(graph, 'A')
print()
print("DFS Iterative with Stack LIFO:")
DFS_iterative(graph, 'A')
print()
print("BFS with Queue FIFO:")
BFS(graph, 'A')