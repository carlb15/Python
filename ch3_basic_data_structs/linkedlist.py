"""Linkedlist implementation."""


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
        
   
        
        
class UnorderedList(object):
  """Linkedlist implementation."""
  
  def __init__(self):
    """Initialization of list."""
    self.head = None
    self.end = None

  def isEmpty(self):
    """Tests if the list is empty."""
    """    
    :rtype: Bool
    """
    return self.head == None

  def add(self, item):    
    """Adds a new item to the list. Assumes item is not present."""
    """
    :type item: Node()     
    """
    if self.head == None:
      self.head = Node(item)
    elif self.end == None:      
      self.end = self.head
      self.head = Node(item)
      self.head.setNext(self.end)
    else:
      temp = Node(item)
      temp.setNext(self.head)
      self.head = temp    
      
  def remove(self, item):
    """Removes the item from the list. Assumes item is present."""
    """
    :type item: Node()     
    """  
    prev = self.head
    curr = self.head
    
    temp = Node(item)
    
    while curr:
      if self.head.getData() == temp.getData():
        self.head = curr.getNext()
        if self.end.getData() == temp.getData():
          self.end = None
        break
      elif self.end.getData() == temp.getData():
        self.end = prev
        break
      elif curr.getData() == temp.getData():
        prev.setNext(curr.getNext())
        curr = None
        break
      prev = curr
      curr = curr.getNext()

  def search(self, item):
    """Searches for the item in the list."""
    """
    :type item: Node() 
    :rtype: Bool
    """    
    curr = self.head
    while curr:
      if curr.getData() == item.getData():
        return True
      curr = curr.getNext()  
      
    return False
 
  def size(self):
    """Returns the number of items in the list."""
    """    
    :rtype: Int: size of list
    """ 
    size = 0
    curr = self.head
    
    while curr:
      curr = curr.getNext()
      size += 1
    
    return size
  
  def append(self, item):
    """Adds a new item to the end of the list. Assumes item is not present."""
    """
    :type item: Node()     
    """      
    temp = Node(item)
    self.end.setNext(temp)
    self.end = temp
   
  def index(self, item):
    """Returns the position of item in the list. Assumes item is present."""
    """
    :type item: Node() 
    :rtype pos: Int
    """  
    curr = self.head
    idx = 0    
    while curr:      
      if curr.getData() == item.getData():
        return idx
      idx += 1
      curr = curr.getNext()
    
  def insert(self, pos, item):
    """Adds a new item in the list at position pos. Assumes item is not present."""
    """
    :type item: Node() 
    """  
    if pos == 0:
      item.setNext(self.head)
      self.head = item
    else:
      prev = self.head
      curr = self.head
      idx = 0
      while curr:        
        if idx == pos:                
          prev.setNext(item)
          item.setNext(curr)
          break
        prev = curr
        curr = curr.getNext()
        idx += 1    

  def pop(self, pos=None):
    """
       Removes and returns the item at position pos. It needs the position and returns the item.
       Assumes the item is in the list.
    """
    """
    :type pos: int
    :rtype node: Node()
    """
    if pos == None:
      pos = self.size() - 1
    
    if pos == 0:
      h = self.head
      self.head = None
      return h
    else:
      prev = curr = self.head
      idx = 0
      while curr:
        if idx == pos:
          prev.setNext(curr.getNext())
          return curr          
        
        idx += 1
        prev = curr
        curr = curr.getNext()


if __name__ == "__main__":
  node = Node()
  assert(node.data == None)
  assert(node.next == None)
  node.setData(1)
  assert(node.getData() == 1)    
  node.setNext(Node(1000000000000))
  assert(node.getNext().getData() == 1000000000000)
  assert(node.next.getData() == 1000000000000)
  
  list = UnorderedList()
  assert(list.isEmpty())
  n1 = 1
  n2 = 2
  n3 = 10000
  n4 = 432424

  list.add(n1)
  list.add(n2)
  list.add(n3)  
  assert(not list.isEmpty())   

  # Remove from middle
  list.remove(n2)
  # Remove from beginning
  list.remove(n1)
  list.remove(n3)
  print('list size %d' % list.size())
  assert(list.size() == 0)  
  
  # Remove from end of list
  list.add(n3)  
  list.add(n4)
  list.remove(n3)
  assert(list.size() == 1)

  assert(list.search(n4))
  assert(not list.search(n3))
  
  n5 = 1434134
  list.append(n5)
  assert(list.search(n5))
  
  n6 = 16744
  list.append(n6)
  assert(list.index(n5) == 1)
  assert(list.index(n6) == 2)
  list.remove(n5)
  assert(list.index(n6) == 1)
  
  list.insert(0, n1)
  assert(list.index(n1) == 0)
    
  n10 = 12012030213
  n40 = 123899031954
  list.insert(2, n10)  
  list.insert(3, n40)  
  assert(list.index(n10) == 2)
  assert(list.index(n40) == 3)
  
  assert(list.pop(2) == n10)
  assert(list.pop() == n6)
  
  
  
  
  
  