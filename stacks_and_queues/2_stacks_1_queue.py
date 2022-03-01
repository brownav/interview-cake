# Implement a queue using two stacks

class Queue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        self.in_stack.append(value)


    def dequeue(self):
        if self.out_stack:
            return self.out_stack.pop()
        elif self.in_stack: 
            for i in range(len(self.in_stack)):
                value = self.in_stack.pop()
                self.out_stack.append(value)
            return self.out_stack.pop()
        else:
            return None


obj = Queue()
obj.enqueue(0)
obj.enqueue(1)
obj.enqueue(2)
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())



