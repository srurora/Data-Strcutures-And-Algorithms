import heapq

max_heap = []

# Push elements (store negatives)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)

print("MaxHeap (stored as negated list):", max_heap)

# Peek max (invert back)
print("Peek:", -max_heap[0])

# Pop elements in descending order
while max_heap:
    print("Popped:", -heapq.heappop(max_heap))
