"""Deque Implementation."""

class Deque():
  """Deque Class."""
  """
  Deques are structured as an ordered collection of items where items are 
  added from either end, either front or rear.
  """
  
  def __init__(self):
    """
    Initialize an empty deque.
    :type None
    :rtype None
    """
    self.items = []
  
  def addFront(self, item):
    """
    Add item to the front of the deque.
    :type item to add
    :rtype None
    """
    self.items.insert(0, item)
    
  def addRear(self, item):
    """
    Add item to the end of the deque.
    :type item to add
    :rtype None
    """
    self.items.append(item)
  
  def removeFront(self):
    """
    Remove item from front of deque.
    :type None
    :rtype front item in deque.
    """
    return self.items.pop(0)
  
  def removeRear(self):
    """
    Remove item from rear of deque.
    :type None
    :rtype item from rear of deque.
    """
    return self.items.pop()
    
  def isEmpty(self):
    """
    Test if deque is empty.
    :type None
    :rtype True/False
    """
    return len(self.items) == 0
    
  def size(self):
    """
    Returns size of deque.
    :type None
    :rtype integer size of deque.
    """
    return len(self.items)
    
    
if __name__=="__main__":
  d = Deque()
  assert(d.size() == 0)
  assert(d.isEmpty() == True)
  d.addFront(5)
  d.addFront(4)
  d.addFront(3)
  d.addRear(1)
  assert(d.size() == 4)
  assert(d.isEmpty() == False)
  assert(d.removeFront() == 3)
  assert(d.removeRear() == 1)
  assert(d.removeRear() == 5)
  d.removeRear()
  assert(d.isEmpty() == True)
  assert(d.size() == 0)
  
  d1 = Deque()
  assert(d1.isEmpty() == True)
  d1.addRear(4)
  d1.addRear('dog')
  d1.addFront('cat')
  d1.addFront(True)
  assert(d1.size() == 4)
  assert(d1.isEmpty() == False)
  d1.addRear(8.4)
  assert(d1.removeRear() == 8.4)
  assert(d1.removeFront() == True)
  