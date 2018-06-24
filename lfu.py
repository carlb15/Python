"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.capacity = capacity
        # least frequently used cache store (key, (value, frequency))
        self.lfu_cache = {}
        # Create buckets for each (frequency, keys).
        self.freq_table = defaultdict(OrderedDict)
        
        print("Create LFU ", self.lfu_cache, " and frequency table ", self.freq_table)
        
        self.minimum_freq = 0

    
    def get(self, key):
        """
        Least Frequently Used.
        Get item from cache update its status 
        in the cache.
        :type key: int
        :rtype: int
        """
        # if key isn't present, return -1
        if key not in self.lfu_cache:
            print('Key not present: return -1')
            return -1
        
        print("Get value,freq from LFU ", self.lfu_cache[key])
        # Get the value, frequency from the LFU table
        value, freq = self.lfu_cache[key]

        print("Remove freq,key ", (freq, key), " from FREQ table ", self.freq_table)
        # Remove the frequency,key from the frequency table.
        del self.freq_table[freq][key]
        print("REMOVED freq,key from FREQ table ", self.freq_table)
        
        # Frequency is at the minimum and not in the Frequency table.
        if freq == self.minimum_freq and not self.freq_table[freq]:
            print('Update minimum_freq ', self.minimum_freq)
            # increase the minimum.
            self.minimum_freq += 1
        
        print('Add key to new bucket freq bucket ', (freq + 1, key))
        # Move the key to frequency + 1 bucket
        self.freq_table[freq + 1][key] = 0
        print("freq table updated " , self.freq_table)
        
        
        # Update the LFU cache with value and freq + 1
        self.lfu_cache[key] = (value, freq + 1)
        print('Update increment frequency ', (key, value, freq), ' in LFU cache for key ', self.lfu_cache)
        
        # return the value 
        return value

        
    def put(self, key, newValue):
        """
        Get item and update or
        remove least frequently used 
        and add new item. If tie then
        LRU item is evicted.
        :type key: int
        :type value: int
        :rtype: void
        """
        # Don't allow requests to empty cache.
        if self.capacity < 1:
            return
        
        # when key is present, update it.
        if key in self.lfu_cache:
            oldValue, freq = self.lfu_cache[key]
            # Update LFU cache with the new value.
            self.lfu_cache[key] = (newValue, freq)
            # call get() to update frequency table
            self.get(key)
        # Cache has reach capacity
        elif len(self.lfu_cache) == self.capacity:
            # Get the least frequently used key,value
            old_key, value = self.freq_table[self.minimum_freq].popitem(last=False)
            # Remove LFU item
            del self.lfu_cache[old_key]
            # Set the minimum frequency to 1 (our first bucket)
            self.minimum_freq = 1
            # Add the new item with frequency of 1
            self.lfu_cache[key] = (newValue, self.minimum_freq)
            # Add key to frequency table in bucket 1
            self.freq_table[self.minimum_freq][key] = 0
        else:
            # reset minimum
            self.minimum_freq = 1
            # add item to the LFU cache with frequency of 1
            self.lfu_cache[key] = (newValue, self.minimum_freq)
            # add key frequency bucket 1 in the frequency table
            self.freq_table[self.minimum_freq][key] = 0
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)