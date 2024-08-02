print("Stack in linked lists")

class Node:
     def __init__(self, data):
          self.data = data
          self.next = None

class Stackll:
     def __init__(self):
          self.head = None
          
     def push(self,data):
          node = Node(data)
          if self.head is None:
               self.data = node
          new_node = Node(data)
          new_node.next = self.head
          self.head = new_node

     def pop(self):
          if self.is_empty():
            return "Stack is empty, cannot pop."
          removed_data = self.head.data  
          self.head = self.head.next      
          return removed_data
     
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
          return f'\n{self.head.data}'     
     
     def display(self):
          current = self.head
          while current:
               print(current.data,end = " ")
               current = current.next
          print()
               
               
simple_stack1 = Stackll()
simple_stack1.is_empty()
simple_stack1.push(13)
simple_stack1.push(23)
simple_stack1.push(34)
simple_stack1.display()