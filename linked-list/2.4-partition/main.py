# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or 
# equal to x. If x is contained within the list , the values of x only need to be after the elements less than x(see below). 
# The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
class Node:
    next = None
    previous = None
    def __init__(self, value):
        self.value = value

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

    def insert(self,value):
        node = Node(value)
        if (self.tail is None) and (self.head is None):
            self.tail = node
            self.head = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

    def swap(self, fromNode, toNode):
        if fromNode == self.head:
            self.head = toNode
        if toNode == self.tail:
            self.tail = fromNode

        toNodePrevious = toNode.previous
        toNodeNext = toNode.next


        toNode.previous = fromNode.previous
        toNode.next = fromNode.next
        if fromNode.next is not None:
            fromNode.next.previous = toNode
        if fromNode.previous is not None:
            fromNode.previous.next = toNode

        fromNode.next = toNodeNext
        fromNode.previous = toNodePrevious 
        if fromNode.next is not None:
            fromNode.next.previous = fromNode
        if fromNode.previous is not None:
            fromNode.previous.next = fromNode
        
        return True

def partition(list, value):
    currentHead = list.head
    currentTail = list.tail
    while currentHead != currentTail:
        if currentHead.value < value:
            currentHead = currentHead.next
            continue

        if currentTail.value >= value:
            currentTail = currentTail.previous
            continue

        if currentHead.value >= value and currentTail.value < value:
            list.swap(currentHead,currentTail)
            newHead = currentHead
            currentHead = currentTail
            currentTail =  newHead

        if currentHead.next is None or currentTail.previous is None:
            break
        

list = LinkedList()
list.insert(3)
list.insert(5)
list.insert(8)
list.insert(5)
list.insert(10)
list.insert(2)
list.insert(1)

partition(list, 5)

list.debug()