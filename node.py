"""Node Class Implementation."""

class Node():
  """Node Class."""
  
  def __init__(self, initdata):
    """
    Initialization of a Node.
    :type data to initialize a node.
    """
    self.data = initdata
    self.next = None
    
  def getData(self):
    """
    Get the node data.
    :rtype node data
    """
    return self.data
    
  def getNext(self):
    """
    Get the next node.
    :rtype self.next
    """
    return self.next
    
  def setData(self, newData):
    """
    Set the node's data.
    :type node's data
    """
    self.data = newData
  
  def setNext(self, newnext):
    """
    Set the node's next.
    :type newnext 
    """
    self.next = newnext
    
if __name__=="__main__":
  temp = Node(93)
  assert(temp.getData() == 93)
  temp1 = Node(32)
  temp.setNext(temp1)
  assert(temp.getNext() == temp1)
