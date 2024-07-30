class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
    
    def enqueue(self,data):
        if self.head == None:
            self.data = Node(data)
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def peek(self):
        return self.head.data

    def max(self):
        current =  self.head
        ma = current.data
        while current:
            if current.data > ma:
                ma = current.data
            current = current.next
        return ma

my = Queue()
my.enqueue(23)
my.enqueue(3)
my.enqueue(100)
my.enqueue(34)
my.peek()
print(my.max())