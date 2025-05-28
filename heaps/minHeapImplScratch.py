class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self.heapify_upwards()

    def pop(self):
        if len(self.heap) == 0: return None
        self.swap(0, -1)
        min_val = self.heap.pop()
        self.heapify_downwards()
        return min_val

    def peek(self):
        return self.heap[0] if self.heap else None
    
    def heapify_upwards(self):
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1)//2
            if self.heap[i] < self.heap[parent]:
                self.swap(i,parent)
                i = parent
            else:
                break

    def heapify_downwards(self):
        i = 0
        while 2*i + 1 < len(self.heap):
            left, right, smallest = 2*i + 1, 2*i + 2, i
            if self.heap[left] < self.heap[smallest]: 
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != i:
                self.swap(i, smallest)
                i = smallest
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


minHeap = MinHeap()
minHeap.push(1)
minHeap.push(2)
minHeap.push(3)
minHeap.push(10)
minHeap.push(-1)
minHeap.push(91)

print("Heap after 6 pushes:", minHeap.heap)

print("Smallest element:", minHeap.peek())

while minHeap.heap:
    print("Popped:", minHeap.pop())

print("Heap after all the pops: ", minHeap.heap)
