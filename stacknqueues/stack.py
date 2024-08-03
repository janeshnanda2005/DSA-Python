class Stack:
     def __init__(self):
          self.stack = []
     
     def push(self,data):
          self.stack.append(data)


     def pop(self):
          self.stack.pop(self.stack.index(self.stack[0]))
     
     def pop_an_element(self,data):
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
simple_stack.push(23)
simple_stack.push(43)
simple_stack.push(44)
simple_stack.pop()
simple_stack.peek()
simple_stack.display()

'''print("USING VARIABLE TOP STACK")
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

     def display(self):
          print(self.s)

top = Stack_top()
top.push(34)
top.push(90)
top.push(911)
top.pop(34)
top.peek()
top.display()
'''
