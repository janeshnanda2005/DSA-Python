class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
    
    def insertBeg(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print()

    
    def delete(self, data):
        temp = self.head
        
        # If the head node itself holds the data to be deleted
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        # Search for the data to be deleted, keep track of the previous node
        prev = None
        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next

        # If data was not present in the linked list
        if temp is None:
            return 'Data not found'

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

if __name__ == "__main__":
    llist = Linked()
    llist.insertBeg(10)
    llist.insertBeg(20)
    llist.insertBeg(30)
    llist.insertBeg(20)
    llist.display()  
    llist.delete(20)
    llist.display() 