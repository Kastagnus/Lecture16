class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.stack)
s.pop()
print(s.stack)
