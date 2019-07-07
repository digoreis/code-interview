# Implement an algorithm to find the kth to last element of a singly linked list.
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

def kthToLast(node, kth):
    if node.next is None: return (node,0)
    reference, index = kthToLast(node.next, kth)
    if index == -1:
        return (reference, index)
    if index == kth:
        return (reference, -1)
    else:
        return (node, index + 1)
    return (None, -1)



list = LinkedList()
list.insert("A")
list.insert("B")
list.insert("B")
list.insert("C")
list.insert("C")
list.insert("C")
list.insert("C")
list.insert("D")

print(kthToLast(list.head, 6)[0].value)
print(kthToLast(list.head, 1)[0].value)
print(kthToLast(list.head, 2)[0].value)
print(kthToLast(list.head, 0)[0].value)