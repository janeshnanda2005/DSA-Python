print("Stack in linked lists")

class Node:
     def __init__(self, data):
          self.data = data
          self.next = None

class Stackll:
     def __init__(self):
          self.head = None
          
     def push(self,data):
          if self.head == None:
               self.head = Node(data)
          new_node = Node(data)
          new_node.next = self.head
          self.head = new_node
     
     def is_empty(self):
          if self.head is None:
               return True
     
     def size(self):
          c = 0
          current = self.head
          while current:
               current = current.next
               c+=1
          return c
     
     def peek(self):
          return self.head.data
     
     def display(self):
          current = self.head
          while current:
               print(current.data,end = " ")
               current = current.next
          print()
               
               
simple_stack1 = Stackll()
simple_stack1.is_empty()
simple_stack1.push(23)
simple_stack1.push(43)
simple_stack1.push(44)
simple_stack1.peek()
simple_stack1.display()