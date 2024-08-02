import heapq
class Minheap:
    
    def __init__(self):
        self.heap = []

    def push(self,data):
        heapq.heappush(self.heap,data)
    
    def pop(self):
         return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]
    
    def __str__(self):
        return str(self.heap)


min_heap = Minheap()
min_heap.push(10)
min_heap.push(5)
min_heap.push(20)
print(min_heap)       
print(min_heap.pop()) 
print(min_heap)

class Maxheap:
    
        
    def __init__(self):
        self.heap = []

    def push(self,data):
        heapq.heappush(self.heap,-data)
    
    def pop(self):
         return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0]
    
    def __str__(self):
        return str(self.heap)
    

max_heap = Maxheap()
max_heap.push(10)
max_heap.push(5)
max_heap.push(20)
print(max_heap)       
print(max_heap.pop()) 
print(max_heap)       