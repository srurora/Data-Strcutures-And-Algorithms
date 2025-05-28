import heapq

# Create an empty list to use as a heap
min_heap = []

# Push elements
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)

print("MinHeap (as list):", min_heap)

# Peek the smallest
print("Peek:", min_heap[0])

# Pop elements in ascending order
while min_heap:
    print("Popped:", heapq.heappop(min_heap))
