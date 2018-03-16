"""Stack implementation."""

class Stack():
  """Stack class."""
  
  def __init__(self):
    """
    :type None
    :rtype None
    """
    self.items = []
    
  def push(self, item):
    """
    Push item onto the stack.
    :type item to add to the top of the stack.
    :rtype None
    """
    self.items.append(item)
  
  def pop(self):
    """
    Pop/remove item from the stack.
    :type None
    :rtype item popped off the top of the stack.
    """
    return self.items.pop()
    
  def peek(self):
    """
    Peek at top of the stack.
    :type None
    :rtype item at the top of the stack.
    """
    return self.items[-1]
    
  def isEmpty(self):
    """
    Tests if stack is empty.
    :type None
    :rtype True/False if stack is empty or not.
    """
    return len(self.items) == 0
  
  def size(self):
    """
    Get the size of the stack.
    :type None
    :rtype integer size of stack.
    """
    return len(self.items)
  
  
if __name__=="__main__":
  s = Stack()
  assert(s.isEmpty() == True)
  assert(s.size() == 0)
  s.push(1)
  s.push('Dog')
  s.push('Hello world')
  s.push(13.532)
  assert(s.pop() == 13.532)
  assert(s.size() == 3)
  assert(s.isEmpty() == False)