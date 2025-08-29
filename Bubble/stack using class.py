class stack():
    def __init__(self):
        self.stack = []
    def add(self,element):
        self.stack.append(element)
    def isEmpty(self):
        return len(self.stack)==0
                          
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def __str__(self):
        return str(self.stack)
    
Stack = stack()

Stack.isEmpty()
Stack.add(10)
Stack.add(20)
Stack.pop()
print(Stack)
print(type(stack))
    
