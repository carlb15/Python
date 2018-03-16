""""Circular buffer."""


class CircularBuffer():
    """Circular buffer with static array."""

    def __init__(self, size=10):
      """Initialize items."""
      self.maxsize = size
      self.buffer = [-1] * self.maxsize
      self.tail = -1
      self.head = -1

    def isFull(self):
      """Check if queue is full."""
      return self.head == (self.tail % self.maxsize) + 1

    def isEmpty(self):
      """Check if queue is empty."""
      return self.head == self.tail

    def add(self, item):
      """Add item to queue."""
      """
         Args: item to add
         Returns: True if suceeds, otherwise False.
      """
      if not self.isFull():
          self.tail = (self.tail + 1) % self.maxsize
          self.buffer[self.tail] = item
          return True
      return False

    def remove(self):
      """Remove an item from the queue."""
      """            
        Returns: Item if it suceeds, otherwise None.
      """
      if self.isEmpty():
        return None
         
      itemToRemove = self.buffer[self.head]
      self.head = (self.head + 1) % self.maxsize
      return itemToRemove


if __name__ == "__main__":
  circBuf = CircularBuffer()
  assert(not circBuf.isFull())
  assert(circBuf.isEmpty())
  assert(circBuf.remove() == None)
  for i in range(10):
      assert(circBuf.add(1))
  assert(circBuf.remove())