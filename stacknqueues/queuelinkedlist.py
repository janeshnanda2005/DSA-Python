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

    def max(self):
        c = self.head.data
        while self.head:
            if self.head.data > c:
                c = self.head.data
            self.head = self.head.next
        return c
     
    def dequeue(self):
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            return removed_data
        

        current = self.head
        while current.next and current.next.next:
            current = current.next
        removed_data = current.next.data
        current.next = None
        return removed_data
    
    def min(self):
        c = self.head.data
        if self.head is None:
            print('The queue is empty ')
        while self.head:
            if self.head.data < c:
                c = self.head.data
            self.head = self.head.next
        return c

my = Queue()
my.enqueue(23)
my.enqueue(3)
my.enqueue(100)
my.enqueue(34)
my.peek()
my.length()
my.dequeue()
my.display()