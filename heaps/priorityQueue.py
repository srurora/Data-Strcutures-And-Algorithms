import heapq

pq = []

# Push (priority, value)
heapq.heappush(pq, (2, "eat"))
heapq.heappush(pq, (1, "code"))
heapq.heappush(pq, (3, "sleep"))

# Peek
print("Peek:", pq[0])

# Pop in order of priority
while pq:
    priority, task = heapq.heappop(pq)
    print(f"Priority: {priority}, Task: {task}")
