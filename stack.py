class Stack:
     def __init__(self):
          self.stack = []
     
     def push(self,data):
          self.stack.append(data)
     
     def pop(self,data):
          self.stack.pop(self.stack.index(data))
     
     def peek(self):
          if self.stack_empty():
               print("Underfow")

          print(self.stack[-1])
     
     def size(self):
          print(len(self.stack))
     
     def stack_empty(self):
          if len(self.stack) == 0:
               print(True)
          if len(self.stack) != 0:
               print(False)
     
     
     def display(self):
          print(self.stack)

          
simple_stack = Stack()
simple_stack.stack_empty()
simple_stack.push(23)
simple_stack.push(43)
simple_stack.push(44)
simple_stack.pop(43)
simple_stack.peek()
simple_stack.display()
simple_stack.stack_empty()


print("USING VARIABLE TOP STACK")
#Stack with the help of of top

class Stack_top:
     def __init__(self):
          self.s = []
          self.top = -1
     
     def push(self,data):
          self.top+=1
          self.s.append(data)
     
     def pop(self,data):
          if self.is_empty():
               print("Underflow")
          self.top -=1
          self.s.pop(self.s.index(data))
     
     def is_empty(self):
          if len(self.s) == 0:
               return True
    
     def peek(self):
          print(self.s[self.top])

     def diaplay(self):
          print(self.s)

top = Stack_top()
top.push(34)
top.push(90)
top.pop(34)
top.peek()
top.diaplay()

#Stack in linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None


    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Error: Stack Underflow")
            return None
        popped_element = self.head.data
        self.head = self.head.next
        return popped_element

    def peek(self):
        if self.is_empty():
            print("Error: Stack Underflow")
            return None
        return self.head.data

    def size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size


    def is_empty(self):
        return self.head is None

def main():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack size:", stack.size())
    print("Stack empty?", stack.is_empty())

if __name__ == "__main__":
    main()