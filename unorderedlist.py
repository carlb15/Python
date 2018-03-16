"""Unordered List Implementation"""
from node import Node

class UnorderedList():
  """Unordered List Class."""
  
  def __init__(self):
    """
    Initializes an unordered list.
    """
    self.head = None
    
  def add(self, item):
    """
    Adds an item to the list.
    :type an item 
    """
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
  
  def remove(self, item):
    """
    Removes the item from the list.
    :type item to remove
    """
    prev = None
    curr = self.head
    found = False
    
    while curr != None and not found:
      if curr.getData() == item:
        found = True
      else:
        prev = curr
        curr = curr.getNext()
    
    # Remove head of list.
    if prev == None:
      self.head = curr.getNext()
    else:
      prev.setNext(curr.getNext())


  def search(self, item):
    """
    Determine if item is in the list.
    :type item to find
    :rtype index of item found
    """
    curr = self.head
    found = False
    while curr != None and not found:
      if curr.getData() == item:
        found = True
      else:
        curr = curr.getNext()
    return found
    
  def isEmpty(self):
    """
    Test if the list is empty.
    :rtype True/False
    """
    return self.head == None
  
  def size(self):
    """
    Get the size of the list.
    :rtype integer size of list
    """
    curr = self.head
    count = 0
    while curr != None:
      count += 1
      curr = curr.getNext()
    return count
  
  def append(self, item):
    """
    Append an item to the end of the list.
    :type item to append
    """
    if self.head == None:
      return Node(item)

    curr = self.head
    # iterate to the end of the list.
    while curr.getNext() != None:
      curr = curr.getNext()

    # append item to the end of the list.
    curr.setNext(Node(item))

  def itemAtIndex(self, index):
    """
    Get the item at the index.
    :type a valid index 
    :rtype item at the given index.
    """
    curr = self.head
    pos = 0
    while curr != None and index != pos:
      curr = curr.getNext()
    return curr

  def index(self, item):
    """
    Get the position of the item in the list.
    Assumes item is present.
    :type item to find
    :rtype position of item in the list.
    """
    curr = self.head
    count = 0
    while curr != None:
      if curr.getData() == item:
        break
      count += 1
      curr = curr.getNext()
    return count

  def insert(self, pos, item):
    """
    Inserts an item into the list.
    Assumes no duplicates and enough positions for pos to work.
    :type pos to add item 
    :type item to add
    """
    # Inserting at the beginning of the list.
    if pos == 0:
      temp = self.head
      self.head = Node(item)
      self.head.setNext(temp)
      return

    idx = 0
    prev = None
    curr = self.head
    while curr != None and (idx - 1) != pos:
      curr = curr.getNext()
      idx += 1

    temp = Node(item)
    temp.setNext(curr.getNext())
    curr.setNext(temp)

  def pop(self, pos=-1):
    """
    Removes and returns the last item in the list.
    :type pos of item to remove from list.
    :rtype item removed
    """
    if pos == -1:
      return self.remove(self.size() - 1)
    else:
      return self.remove(self.itemAtIndex(pos))
   

if __name__=="__main__":
  mylist = UnorderedList()

  mylist.add(31)
  mylist.add(77)
  mylist.add(17)
  mylist.add(93)
  mylist.add(26)
  mylist.add(54)

  print(mylist.size())
  print(mylist.search(93))
  print(mylist.search(100))

  mylist.add(100)
  print(mylist.search(100))
  print(mylist.size())

  mylist.remove(54)
  print(mylist.size())
  mylist.remove(93)
  print(mylist.size())
  mylist.remove(31)
  print(mylist.size())
  print(mylist.search(93))