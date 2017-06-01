"""Interactive Python: Queue."""


class Queue():
    """Queue Implementation."""

    def __init__(self):
        """Initialize the queue."""
        self.myList = []

    def enqueue(self, item):
        """Add a new item to the rear of the queue."""
        """
        Run-time: O(n)

        Args:
            item: item to add

        Returns: None
        """
        self.myList.insert(0, item)

    def dequeue(self):
        """Remove the front item from the queue."""
        """
        Run-time: O(1)

        Args: None

        Returns: Returns removed item.
        """
        if len(self.myList) == 0:
            return None

        return self.myList.pop()

    def isEmpty(self):
        """Test to see whether the queue is empty."""
        """
        Args: None

        Returns: True if empty, False otherwise.
        """
        return len(self.myList) == 0

    def size(self):
        """Get number of items in the queue."""
        """
        Args: None

        Returns: number of items in the queue.
        """
        return len(self.myList)


if __name__ == "__main__":
    myQueue = Queue()
    assert(myQueue.isEmpty())
    assert(myQueue.size() == 0)
    myQueue.enqueue(1)
    myQueue.enqueue(-1)
    myQueue.enqueue(10)
    myQueue.enqueue("hello")
    myQueue.enqueue('world')
    myQueue.enqueue(1.001011)
    assert(myQueue.size() == 6)
    assert(not myQueue.isEmpty())
    assert(myQueue.dequeue() == 1)
    assert(myQueue.dequeue() == -1)
    assert(myQueue.dequeue() == 10)
    assert(myQueue.dequeue() == 'hello')
    assert(myQueue.dequeue() == 'world')
    assert(myQueue.dequeue() == 1.001011)
    assert(myQueue.dequeue() is None)
    assert(myQueue.size() == 0)
    assert(myQueue.isEmpty())
    q = Queue()
    print(q.isEmpty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.isEmpty())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
