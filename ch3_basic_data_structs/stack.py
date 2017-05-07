__author__ = "Carl Barbee"

class Stack:
    """Stack Class"""

    def __init__(self):
        """Initialize a new stack"""
        self.top     = -1
        self.myStack = []


    def push(self, item):
        """Adds a new item to the top of the stack."""
        """@param item to add to the stack"""
        """@returns Nothing."""

        self.top     += 1
        self.myStack.append(item)


    def pop(self):
        """Removes the top item from the stack"""
        """@param None"""
        """@returns removed item"""

        self.top -= 1

        return self.myStack.pop()


    def peek(self):
        """Returns the top item from the stack but doesn't remove it"""
        """@param Nothing"""
        """@returns top item from the stack"""

        return self.myStack[self.top]


    def isEmpty(self):
        """Tests whether the stack is empty."""
        """@param Nothing"""
        """@returns Boolean"""

        return self.top == -1


    def size(self):
        """Returns the number of items on the stack."""
        """@param Nothing"""
        """@returns size of stack"""
        return len(self.myStack)


s = Stack()
assert(s.size() == 0)
assert(s.isEmpty())
s.push(4)
s.push('dog')
assert(s.peek() == 'dog')
s.push(True)
assert(s.size() == 3)
assert(not s.isEmpty())
s.push(8.4)
assert(s.pop() == 8.4)
assert(s.pop() == True)
assert(s.size() == 2)
