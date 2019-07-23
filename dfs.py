# Depth First Search in Binary tree
class Node:
    left = None
    right = None

    def __init__(self, value):
        self.value = value


def dfs(node):
    if node is None: return
    if node.left is None and node.right is None:
        print(node.value)
        return
    
    
    dfs(node.left)
    print(node.value)
    dfs(node.right)
        
def bfs(node):
    queue = []
    queue.append(node)
    while len(queue) > 0:
        item = queue.pop(0)
        if item.left is not None:
            queue.append(item.left)
        if item.right is not None:
            queue.append(item.right)
        print(item.value)

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")

nodeA.left = nodeB
nodeB.left = nodeC
nodeA.right = nodeD
nodeD.left = nodeE

print("===============================")
print("DFS")
print("===============================")
dfs(nodeA)
print("===============================")
print("BFS")
print("===============================")
bfs(nodeA)