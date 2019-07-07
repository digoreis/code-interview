#Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop
class Node:
    next = None
    def __init__(self, value):
        self.value = value

class LinkedList:
    head = None
    tail = None
    size = 0

    def debug(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def insert(self,value):
        if (self.tail is None) and (self.head is None):
            self.tail = value
            self.head = value
        else:
            value.previous = self.tail
            self.tail.next = value
            self.tail = value
        self.size += 1

def detectLoop(list):
    hashTable = dict()
    current = list.head
    while current:
        if hashTable.get(current) is None:
            hashTable[current] = True
            current = current.next
        else: 
            return current

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

listA = LinkedList()
listA.insert(node1)
listA.insert(node2)
listA.insert(node3)
listA.insert(node4)
node4.next = node3

node = detectLoop(listA)

if node is not None:
    print(node.value)
else:
    print("NO LOOP")