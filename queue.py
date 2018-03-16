"""Queue implementation."""

class Queue:
  """Queue Class."""
  
  def __init__(self):
    """
    Creates a new queue that is empty.
    :type self
    :rtype None
    """
    self.items = []
  
  def isEmpty(self):
    """
    Tests to see if queue is empty.
    :type   Queue
    :rtype: True/False
    """
    return len(self.items) == 0

  def enqueue(self, data):
    """
    Adds new items to rear of queue.
    :type  data to add
    :rtype None
    """
    self.items.insert(0, data)
  
  def dequeue(self):
    """
    Removes the front item from the queue.
    :type None
    :rtype removed item
    """
    return self.items.pop()
  
  def size(self):
    """
    Gets the size of the queue.
    :type None
    :rtype Integer size of queue.
    """
    return len(self.items)
  
  
  
  
if __name__=="__main__":
  q = Queue()
  assert(q.isEmpty() == True)
  assert(q.size() == 0)
  q.enqueue("Dog")
  q.enqueue(1)
  assert(q.dequeue() == "Dog")
  assert(q.isEmpty() == False)
  assert(q.size() == 1)
  
  
  
  
  