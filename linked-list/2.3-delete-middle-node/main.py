# Implement an algorithm to delete a node in the middle. ( i.e. any node but the first and the last node, not necessarily the exact 
# middle) of a singly linked list, given only access to that node.v

class Node:
    next = None
    def __init__(self, value):
        self.value = value

class LinkedList:
    tail = None
    head = None

    def insert(self,value):
        node = Node(value)
        if (self.tail is None) and (self.head is None):
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node

    def removeInTheMiddle(self, value):
        current = self.head
        previous = None
        while current:
            if current.value != value:
                previous = current
            else: break
            current = current.next

        previous.next = current.next

list = LinkedList()
list.insert("A")
list.insert("B")
list.insert("B")
list.insert("C")
list.insert("X")
list.insert("Z")
list.insert("C")
list.insert("C")
list.insert("C")
list.insert("D")

list.removeInTheMiddle("X")


current = list.head 

while current:
    print(current.value)
    current = current.next

current = list.head 

print("*************************************")
list.removeInTheMiddle("Z")

while current:
    print(current.value)
    current = current.next