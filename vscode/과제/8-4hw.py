class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return self.stack == []
    
    def top(self):
        try:
            return self.stack[-1]
        except IndexError:
            return None
        
    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return None
    
    def push(self, x):
        self.stack.insert(-1, x) 

    def __repr__(self):
        print(self.stack)

p1 = Stack()
print(p1.empty())
print(p1.top())
print(p1.pop())
p1.push(100)
# print(p1.pop())
p1.__repr__()