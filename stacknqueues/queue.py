class Queue:
    def __init__(self):
        self.q=[]

    def enqueue(self,data):
        self.q.append(data)

    def dequeue(self,data):
        self.q.pop(self.q.pop(data))
    
    def display(self):
        print(self.q)
    
    def peek(self):
        print(self.q[-1])
    
    def is_empty(self):
        if len(self.q) == 0:
            return True
        
my = Queue()
my.enqueue([23,45,6,7])
my.enqueue([23,54,65,43])
my.display()