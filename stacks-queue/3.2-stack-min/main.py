# How would you design a stack which , in addition to push and pop, has a function min with return the minimum element? Push, 
# pop and min should opere in 0(1) time.

class Stack:
    items = []
    minimum = 0

    def pop(self):
        item = self.items.pop()
        if item[0] == self.minimum:
            self.minimum = item[1]
        return item[0]
    
    def push(self, value):
        self.items.append((value, self.minimum))
        if self.minimum >= value or self.minimum == 0:
            self.minimum = value

    def min(self):
       return self.minimum

stack = Stack()
stack.push(10)
stack.push(5)
print("Expect(5): ",stack.min())
stack.push(23)
stack.push(1)
print("Expect(1): ",stack.min())
stack.pop()
print("Expect(5): ",stack.min())