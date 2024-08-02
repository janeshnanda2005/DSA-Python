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
min_heap.push(10)
min_heap.push(5)
min_heap.push(20)
print(min_heap)       # Output: [5, 10, 20]
print(min_heap.pop()) # Output: 5
print(min_heap)       # Output: [10, 20]

class MaxHeap:
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
max_heap = MaxHeap()
max_heap.push(10)
max_heap.push(5)
max_heap.push(20)
print(max_heap)       # Output: [20, 10, 5]
print(max_heap.pop()) # Output: 20
print(max_heap)       # Output: [10, 5]