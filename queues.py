# represent a Queue
# implement a Queue
# Generate Binary numbers from 1 to n using a Queue

from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())

# Generate Binary numbers from 1 to n using a Queue
def generateBinaryNumbers(n):
    q = deque()
    q.append('1')
    result = []
    if n == 1: return 1
    for i in range(n):
        x = q.popleft()
        q.append(x+('0'))
        q.append(x+('1'))
        result.append(x)
    return result

print("\nGenerating first n Binary Numbers for given n")
print(generateBinaryNumbers(7))



