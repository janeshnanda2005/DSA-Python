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

    def display(self):
        current = self.head
        while current:
            print(current.data,end = " ")
            current = current.next
    
    def dequeue(self,data):
        if self.is_empty() == True:
            print("No items to delete")
        
    
    def is_empty(self):
        if self.data is None:
            return True
        
    def length(self):
        c = 0
        current = self.head
        while current:
            c+=1
            current = current.next
        print(c)

    def peek(self):
        print(self.head.data)
        
my = Queue()
my.enqueue(23)
my.enqueue(3)
my.enqueue(33)
my.peek()
my.display()
my.length()
my.is_empty()
