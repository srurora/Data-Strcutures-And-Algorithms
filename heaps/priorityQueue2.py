from queue import PriorityQueue
#Thread Safe

pq = PriorityQueue()

pq.put((2, "eat"))
pq.put((1, "code"))
pq.put((3, "sleep"))

# Get elements in priority order
while not pq.empty():
    priority, task = pq.get()
    print(f"Priority: {priority}, Task: {task}")
