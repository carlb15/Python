"""Ordered List impelementation."""

class Node(object):
    """Node class."""

    def __init__(self, initdata=None):
        """Initialization."""
        self.data = initdata
        self.next = None

    def getData(self):
        """Get node's data."""
        return self.data

    def setData(self, data):
        """Set node's data."""
        self.data = data

    def getNext(self):
        """Get next node."""
        return self.next

    def setNext(self, node):
        """Set next node."""
        self.next = node


        
class OrderedList(object):
  """Ordered List."""
  
  def __init__(self):
    self.head = None
    
  def add(self, item):
    """Adds new item to list ensuring order is preserved."""
    """
    :type item: Node()
    :rtype None
    """
    node = Node(item)
    if self.head == None or self.head.getData() > node.getData():
      node.setNext(self.head)
      self.head = node
      return
    
    prev = self.head
    curr = self.head
    while curr:
      if curr.getData() > node.getData():
        prev.setNext(node)
        node.setNext(curr)
        return      
      prev = curr
      curr = curr.getNext()
    
    # Add to the end
    prev.setNext(node)    
   
  def remove(self, item):
    """Removes the item from the list. Assumes item is present."""
    """
    :type item: Node()
    :rtype None
    """
    if self.head.getData() == item:
      self.head = self.head.getNext()
      return

    prev = curr = self.head
    while curr:      
      if curr.getData() == item:
        prev.setNext(curr.getNext())
        break
      prev = curr
      curr = curr.getNext()
  
  def search(self, item):
    """Searches for the item in the list."""
    """
    :type item: Node()
    :rtype Boolean
    """
    curr = self.head
    while curr:
      if curr.getData() == item:
        return True
      curr = curr.getNext()
    return False
    
  def isEmpty(self):
    """Tests to see if the list is empty."""
    """
    :type None
    :rtype Boolean
    """
    return self.head == None
    
  def size(self):
    """Returns the number of items in the list."""
    """
    :type None
    :rtype int
    """
    curr = self.head
    count = 0
    while curr:
      count += 1
      curr = curr.getNext()
    
    return count
    
  def index(self, item):
    """Returns the position of the item in the list."""
    """
    :type item: Node
    :rtype int
    """
    curr = self.head
    idx = 0
    while curr:
      if item == curr.getData():
        break
      idx += 1
      curr = curr.getNext()
    return idx
    
  def pop(self, pos=None):
    """Removes and returns the item. Position is optional and returns the last item if undefined."""
    """
    :type pos: int (optional) 
    :rtype item: Node()
    """
    if pos == None:
      pos = self.size() - 1
    if pos == 0:
      temp = self.head
      self.head = self.head.getNext()
      return temp.getData()
    
    prev = curr = self.head    
    for idx in range(self.size()):
      if idx == pos:
        prev.setNext(curr.getNext())
        return curr.getData()      
      prev = curr
      curr = curr.getNext()
 
  def print(self):
    curr = self.head
    while curr:
      print("%d" % curr.getData(), end=" ")
      curr = curr.getNext()
    print('\n--------------------------------')
        

if __name__ == "__main__":
  orderedList = OrderedList()
  
  assert(orderedList.isEmpty())
  assert(orderedList.size() == 0)
  
  orderedList.add(5)
  orderedList.add(1)
  orderedList.add(10)
  orderedList.add(-10)
  assert(orderedList.index(-10) == 0)        
  orderedList.add(7)
  orderedList.add(70)
  assert(orderedList.index(70) == 5)        
  assert(orderedList.size() == 6)
  orderedList.print()
  
  orderedList.remove(-10)  
  orderedList.remove(70)
  orderedList.remove(7)
  assert(orderedList.size() == 3)
  orderedList.print()
    
  assert(not orderedList.search(-10))
  assert(not orderedList.search(70))
  assert(not orderedList.search(7))
  assert(orderedList.search(1))
  assert(orderedList.search(5))
  orderedList.add(70)    
  assert(orderedList.search(70))    
  orderedList.remove(70)
  assert(not orderedList.search(70))    
  
  assert(not orderedList.isEmpty())
  
  assert(orderedList.size() == 3)
    
  assert(orderedList.index(1) == 0)    
  assert(orderedList.index(5) == 1)    
  assert(orderedList.index(10) == 2)        
    
  assert(orderedList.pop(0) == 1)
  assert(orderedList.size() == 2)
  assert(orderedList.pop() == 10)
  assert(orderedList.size() == 1)
  assert(orderedList.pop() == 5)
  assert(orderedList.isEmpty())
  orderedList.add(1)
  orderedList.add(100)
  orderedList.add(1000)
  assert(orderedList.pop() == 1000)
  assert(orderedList.pop() == 100)
  assert(orderedList.pop() == 1)
 