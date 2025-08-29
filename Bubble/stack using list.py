stack = [14,23,43,12,4,35,5]

stack.append(20)
stack.append(20)
stack.append(30)
stack.append(10)

print(stack[-1])
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

print(stack[-1])

isEmpty = not bool(stack)
print(isEmpty)