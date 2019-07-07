# Write code to remove deplicates from an unsorted linked list

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

    def removeDuplicate(self):
        hashTable = dict()
        list = LinkedList()
        current = self.head

        while current:

            if not hashTable.__contains__(current.value):
                hashTable[current.value] = True
                list.insert(current.value)
            current = current.next
        
        return list


list = LinkedList()
list.insert("A")
list.insert("B")
list.insert("B")
list.insert("C")
list.insert("C")
list.insert("C")
list.insert("C")
list.insert("D")

newList = list.removeDuplicate()
current = newList.head

while current:
    print(current.value)
    current = current.next