#Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node . Note that the intersetion is defined
#based on reference, not value. That is if kth node of the first linked list is the exact same node(by reference) as the jth node of the 
#second linked list, the they are intersecting.

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


def intersection(listA, listB):
    currentA = listA.head
    currentB = listB.head

    while currentA and currentB:
        if currentA == currentB:
            return currentA
        currentA = currentA.next
        currentB = currentB.next

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

listB = LinkedList()
listB.insert(node5)
listB.insert(node6)
listB.insert(node3)
listB.insert(node7)
listB.insert(node8)

node = intersection(listA,listB)

if node is not None:
    print(node.value)
else:
    print("NO CONNECT")
