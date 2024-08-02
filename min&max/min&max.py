import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)

# Example usage:
min_heap = MinHeap()
while True:
    print('\n1.push \n2.pop \n3.peek \n4.display \n5.exit')
    n = int(input('entr:'))

    if n > 4:
        break

    if n == 1:
        ert = int(input('enter a number:'))
        min_heap.push(ert)
    if n == 2:
        min_heap.pop()
    if n == 3:
        print(min_heap.peek())
    if n == 4:
        print(min_heap)




class rootHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, -item)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0] if self.heap else None

    def __str__(self):
        return str([-x for x in self.heap])

# Example usage:
root_heap = rootHeap()
root_heap.push(10)
root_heap.push(5)
root_heap.push(20)
print(root_heap)       # Output: [20, 10, 5]
print(root_heap.pop()) # Output: 20
print(root_heap)       # Output: [10, 5]