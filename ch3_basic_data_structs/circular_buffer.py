"""Circular Buffer."""


class CircularBuffer():
    """Circular Buffer Implementation."""

    def __init__(self, start, size):
        """Initialize the circular buffer."""
        self.buffer = size * [0]
        self.size = size
        self.startIdx = start
        self.endIdx = start

    def isFull(self):
        """Test to see whether the buffer is full."""
        """
        Args: None

        Returns: True is full, False otherwise
        """
        if self.startIdx == 0 and (self.endIdx + 1) == self.size:
            return True
          
        return (self.startIdx - self.endIdx) == 2


    def adjustIdx(self, idx):
        if idx == self.size - 1:
            return 0
        return idx + 1


    def enqueue(self, item):
        """Add new item to the buffer."""
        """
        Run-time: O(1)

        Args:
            item: item to add

        Returns: None
        """
        print("Insert %s start %d, end %d" % (item, self.startIdx, self.endIdx))
        if self.isFull():
            self.buffer[self.endIdx] = item
            self.startIdx = self.adjustIdx(self.startIdx)
            #self.endIdx = self.adjustIdx(self.endIdx)
        elif self.endIdx == self.size:
            self.endIdx = self.adjustIdx(self.endIdx)
            self.buffer[self.endIdx] = item
        else:
            self.buffer[self.endIdx] = item
            self.endIdx = self.adjustIdx(self.endIdx)

        print(self.buffer)


    def isEmpty(self):
        """Test to see whether the queue is empty."""
        """
        Args: None

        Returns: True if empty, False otherwise.
        """
        return self.startIdx == self.endIdx


    def dequeue(self):
        """Remove the oldest item from the buffer."""
        """
        Run-time: O(1)

        Args: None

        Returns: Returns removed item.
        """
        if self.isEmpty():
            return None    
            
        removedItem = self.buffer[self.startIdx]
        self.buffer[self.startIdx] = -1
        
        print("Remove %s start %d, end %d" % (removedItem, self.startIdx, self.endIdx))
        
        self.startIdx = self.adjustIdx(self.startIdx)
        
        print(self.buffer)
        
        return removedItem


    def size(self):
        """Get number of items in the buffer."""
        """
        Args: None

        Returns: number of items in the queue.
        """
        if self.startIdx <= self.endIdx:
            return self.endIdx - self.startIdx

        return self.size - self.startIdx + self.endIdx


if __name__ == "__main__":
  buffer = CircularBuffer(2, 7)
  assert(buffer.isEmpty())
  assert(not buffer.isFull())
  buffer.enqueue(1)
  buffer.enqueue(2)
  buffer.enqueue(3)
  assert(buffer.dequeue() == 1)
  assert(buffer.dequeue() == 2)
  buffer.enqueue(4)
  buffer.enqueue(5)
  buffer.enqueue(6)
  buffer.enqueue(7)
  buffer.enqueue(8)
  buffer.enqueue(9)
  #assert(buffer.isFull())
  assert(not buffer.isEmpty())
  buffer.enqueue('A')
  buffer.enqueue('B')
  assert(buffer.dequeue() == 5)
  assert(buffer.dequeue() == 6)
