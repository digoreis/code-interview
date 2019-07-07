# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that
#  the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

class Node:
    next = None
    previous = None
    def __init__(self, value):
        self.value = value
    
    def invert(self):
        newNext = self.next
        self.next = self.previous
        self.previous = newNext

class LinkedList:
    tail = None
    head = None

    def debug(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def debugInvert(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.previous

    def reverse(self):
        current = self.tail
        while current:
            invertNode = current
            current = current.previous
            invertNode.invert()
        
        oldHead = self.head
        self.head = self.tail
        self.tail = oldHead
            
            


    def insert(self,value):
        node = Node(value)
        if (self.tail is None) and (self.head is None):
            self.tail = node
            self.head = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

def sumTwoList(listA, listB):
    carry = 0
    currentListA = listA.head
    currentListB = listB.head
    resultList = LinkedList()

    while currentListA or currentListB or carry > 0:
        valueA = 0
        if currentListA is not None:
            valueA = currentListA.value
            currentListA = currentListA.next

        valueB = 0
        if currentListB is not None:
            valueB = currentListB.value
            currentListB = currentListB.next

        newValue = carry + valueA + valueB
        carry = int(newValue / 10)
        newValue = int(newValue % 10)
        resultList.insert(newValue)

    return resultList

listA = LinkedList()
listA.insert(7)
listA.insert(1)
listA.insert(6)
listB = LinkedList()
listB.insert(5)
listB.insert(9)
listB.insert(2)

result = sumTwoList(listA, listB)
result.debug()
result.reverse()
result.debug()