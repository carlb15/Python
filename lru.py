from collections import OrderedDict

class LRUCache:

def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.capacity = capacity
    self.cache = OrderedDict()
    

def get(self, key):
    """
    :type key: int
    :rtype: int
    """
    # if key not present or key < 0 return -1
    # else: return key
    try:
        # Get value of key
        value = self.cache.pop(key)
        # key is most recently used.
        self.cache[key] = value
        # return the key's value
        return value
    except KeyError:
        # key,value not in cache.
        return -1                
    

def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: void
    """
    # has capacity been reached?
    try:
        # remove item
        self.cache.pop(key)
    except KeyError:
        if len(self.cache) >= self.capacity:
            # Pop least recently used item
            # Popping when is False pops in FIFO order.
            self.cache.popitem(last = False)
    
    # Update cache with new item
    self.cache[key] = value
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)