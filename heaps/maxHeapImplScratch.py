class maxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        self.heap.append(val)
        self.heapify_upwards()

    def pop(self):
        if len(self.heap) == 0:
            return None
        self.swap(0, -1)
        maximum = self.heap.pop()
        self.heapify_downwards()
        return maximum
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def heapify_upwards(self):
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1)//2
            if self.heap[i] > self.heap[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def heapify_downwards(self):
        i = 0
        while 2*i + 1 < len(self.heap):
            left, right, maximum = 2*i + 1, 2*i + 2, i
            if self.heap[left] > self.heap[maximum]:
                maximum = left
            if right < len(self.heap) and self.heap[right] > self.heap[maximum]:
                maximum = right
            if i != maximum:
                self.swap(i, maximum)
                i = maximum

            else:
                break

maxheap = maxHeap()

maxheap.push(1)
maxheap.push(10)
maxheap.push(100)
maxheap.push(17)
maxheap.push(1000)
maxheap.push(198)

print("Max Heap after 6 pushes: ", maxheap.heap)

print("Maximum: ", maxheap.peek())

while maxheap.heap:
    print("Popped in decreasing order: ", maxheap.pop())

print("After all the pop ops: ", maxheap.heap)

