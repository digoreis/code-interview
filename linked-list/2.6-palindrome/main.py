# Implement a function to check if a linked list is a palindrome.

class Node:
    next = None
    previous = None
    def __init__(self, value):
        self.value = value

class LinkedList:
    tail = None
    head = None
    size = 0

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

    def insert(self,value):
        node = Node(value)
        if (self.tail is None) and (self.head is None):
            self.tail = node
            self.head = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1


def palindrome(list):
    if list.size == 0 :
        return False
    if list.size == 0 :
        return True

    currentHead = list.head
    currentTail = list.tail

    while currentHead and currentTail:
        if currentHead.value != currentTail.value:
            return False
        
        if currentHead == currentTail.previous and currentTail == currentHead.next:
            break

        currentHead = currentHead.next
        currentTail = currentTail.previous

        if currentHead == currentTail:
            break

    return True
         

listA = LinkedList()
listA.insert("A")
listA.insert("B")
listA.insert("X")
listA.insert("B")
listA.insert("A")

print(palindrome(listA))


listB = LinkedList()
listB.insert("A")
listB.insert("B")
listB.insert("X")
listB.insert("Z")
listB.insert("B")
listB.insert("A")

print(palindrome(listB))


listC = LinkedList()
listC.insert("A")
listC.insert("B")
listC.insert("B")
listC.insert("A")

print(palindrome(listC))