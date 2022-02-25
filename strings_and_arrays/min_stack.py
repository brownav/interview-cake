# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]



minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.stack)
print(minStack.min_stack)
print("min", minStack.getMin()) # return -3
minStack.pop()
print("top", minStack.top())    # return 0
print("min", minStack.getMin()) # return -2
minStack.push(12)
minStack.push(-4)
print("min", minStack.getMin()) # return -2
print(minStack.stack)
print(minStack.min_stack)

# -2, 0, -3, 12
# -2, -2, -3, -3