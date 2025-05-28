#A Min Priority Queue (lower number = higher priority)

class PQ:
    def __init__(self):
        self.q = []

    def push(self, val, priority):
        self.q.append((priority, val))
        self.heapify_upwards()

    def pop(self):
        if not self.q: return None
        self.swap(0, -1)
        minimum = self.q.pop()
        self.heapify_downwards()
        return minimum
    
    def peek(self):
        return self.q[0] if self.q else None
    
    def swap(self, i , j):
        self.q[i], self.q[j] = self.q[j], self.q[i]

    def heapify_upwards(self):
        i = len(self.q) - 1
        while i > 0:
            parent = (i - 1)//2
            if self.q[parent][0] > self.q[i][0]:
                self.swap(parent, i)
                i = parent
            else:
                break
    
    def heapify_downwards(self):
        i = 0
        while 2*i + 1 < len(self.q):
            left, right, minimum = 2*i + 1, 2*i + 2, i
            if self.q[left][0] < self.q[minimum][0]:
                minimum = left
            if right < len(self.q) and self.q[right][0] < self.q[minimum][0]:
                minimum = right
            if minimum != i:
                self.swap(i, minimum)
                i = minimum
            else:
                break

pq = PQ()

pq.push(3, "sleep")
pq.push(1, "code")
pq.push(2, "eat")

print("After all pushes: ", pq.q) 
print("Minimum : ", pq.peek())

while pq.q:
    print("Popped min-priority: ", pq.pop())




