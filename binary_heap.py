"""Binary Heap Implementation"""

class BinHeap:
  def __init__(self):
    """Initialize binary heap."""
    # list of heap items
    #   Children of some node p are left = 2p, right = 2p+1
    #   left children are <=
    #   Parent of node at pos n is n//2.
    self.heapList = [0]
    # current size of heap
    self.currentSize = 0

  def _percolateUp(self, idx):
    """
    Private method to percolate item to 
    correct position in heap to maintain 
    heap property.
    """
    # Move item to correct position while
    # we're not at the dummy root.
    while idx // 2 > 0:
      # while item is less than parent.
      if self.heapList[idx] < self.heapList[idx//2]:
        # swap child and parent.
        self.heapList[idx], self.heapList[idx//2] = \
          self.heapList[idx//2], self.heapList[idx]
      # move to parent's position
      idx = idx//2

  def insert(self, item):
    """Insert into heap.
      Append to end of heapList percolate to 
      correct possition by comparing to parent 
      to maintain heap property.
    """
    self.heapList.append(item)
    self.currentSize += 1
    self._percolateUp(self.currentSize)

  def _percolateDown(self, idx):
    """
    Private method to move the root to its correct
    position in the heap to maintain heap property.
    """
    # While we're not at the end of the heap.
    while (idx * 2) <= self.currentSize:
      # get the smaller of the two children.
      minChildIndex = self.minChild(idx)
      # if minChild is smaller than parent swap them.
      if self.heapList[idx] > self.heapList[minChildIndex]:
        self.heapList[idx], self.heapList[minChildIndex] = \
          self.heapList[minChildIndex], self.heapList[idx]
      # move to smaller child.
      idx = minChildIndex

  def minChild(self, idx):
    """
    Get the smaller of the two children.
    """
    # Only a left child.
    if (idx * 2) + 1 > self.currentSize:
      return idx * 2
    # Get left child
    if self.heapList[idx * 2] < self.heapList[idx * 2 + 1]:
      return idx * 2
    # Get right child
    return idx * 2 + 1

  def delMin(self):
    """
    Delete the minimum from the heap. Restore
    the heap property by percolating down.
    """
    # Remove minimum from top of heap
    minValue = self.heapList[1]
    # Get last item in heap.
    self.heapList[1] = self.heapList[self.currentSize]
    self.currentSize -= 1
    self.heapList.pop()
    self._percolateDown(1)
    return minValue

  def buildHeap(self, alist):
    """
    Building a heap given a list.
    O(n) time
    """
    middleLen = len(alist) // 2
    # set the size.
    self.currentSize = len(alist)
    # Create the heap.
    
    self.heapList = [0] + alist[:]
    # Heap is a complete binary tree
    # so any nodes past halfway point will be
    # leaves and have no children.
    while middleLen > 0:
      self._percolateDown(middleLen)
      middleLen -= 1


if __name__=="__main__":
  bh = BinHeap()
  alist = [9,5,6,2,3]
  print("Building heap with: ", alist)
  
  bh.buildHeap(alist)
  print('Popping the minimum value from heap.')
  print(bh.delMin())
  print(bh.delMin())
  print(bh.delMin())
  print(bh.delMin())
  print(bh.delMin())
