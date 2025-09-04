
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)





q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print("Front element (peek):", q.peek())   
print("Dequeued:", q.dequeue())

print("Front element (peek):", q.peek())              
print("Is empty?", q.is_empty())           
print("Size:", q.size())                   
