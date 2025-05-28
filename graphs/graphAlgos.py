# Dijkstra’s Algorithm (Shortest Path)
# Approach:

# Use Min-Heap to always expand the shortest known path first.
# Keep track of minimum distance to each node.
# Works for positive weight graphs.
import heapq

def dijkstra(graph, start):
    min_heap = [(0, start)] #(distance, node)
    distances = { node : float('inf') for node in graph}
    distances[start] = 0

    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)
        





