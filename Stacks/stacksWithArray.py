class Stack:
    def __init__(self, capacity=1):
        self.top = -1
        self.capacity = capacity
        self.A = [None]*capacity

    def push(self, data):
        if self.capacity == self.top+1:
            print("stack overflow")
            return
        self.top += 1
        self.A[self.top] = data

    def resize(self):
        self.capacity *= 2
        newArray = [None]*self.capacity
        if newArray is None:
            print("system memory problem")
        for i in range(0, self.top+1):
            newArray[i] = self.A[i]
            self.A = newArray

    def peek(self):
        if self.top == -1:
            print("stack underflow")
            return
        return self.A[self.top]

    def pop(self):
        if self.top == -1:
            print("stack underflow")
            return
        temp = self.A[self.top]
        self.top -= 1
        if self.top < self.capacity//2:
            print("trying to resize,decrease")
            self.capacity //= 2
            newarray = [None] * self.capacity
            for i in range(0, self.top+1):
                newarray[i] = self.A[i]
            self.A = newarray
        return temp

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top+1 == self.capacity


stack = Stack()
stack.push(5)
print(stack.peek())
print(stack.pop())
print(stack.isEmpty())
print(stack.isFull())
print(stack.capacity)
