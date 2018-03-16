"""Unsorted Table Map Implementation."""
from MapBase import MapBase

class UnsortedTableMap(MapBase):
  """
  Class that relies on storing key-value pairs in 
  arbitrary order within a Python list.
  """
  
  def __init__(self):
    """Initialize the unsorted list."""
    self._table = []

  def __getitem__(self, k):
    """
    O(n) time complexity.
    :type key k
    :rtype value associated with key k
    """
    for item in item._table:
      if k == item._key:
        return item._value
    # Item not found
    raise KeyError("Key Error: " + repr(k))

  def __setitem__(self, k, v):
    """
    Set value v to key k, overwriting existing value if present.
    O(n) time complexity.
    :type key k
    :type value v
    :rtype None
    """
    for item in self._table:
      if k == item._key:
        item._value = v
        return
    # Add new Item class instance containing key, value pair.
    self._table.append(self._Item(k,v))

  def __delitem__(self, k):
    """
    Remove item associated with key k.
    O(n) time complexity.
    :type key k
    :error KeyError when key k not found.
    """
    for j in range(len(self._table)):
      # key found in table.
      if k == self._table[j]._key:
        # Remove the item
        self._table.pop(j)
        return
    raise KeyError("Key Error: " + repr(k))

  def __len__(self):
    """Get the size of the table."""
    """
    :rtype table size
    """
    return len(self._table)

  def __repr__(self):
    """Print the table."""
    return '\n'.join(str(item) for item in self._table)

  def __iter__(self):
    """Generate iteration of map's keys."""
    for item in self._table:
      # yields the a map's key.
      yield item._key

if __name__=="__main__":
  unsortedmap = UnsortedTableMap()
  unsortedmap[4] = 'hello'
  unsortedmap[5] = 'world'
  unsortedmap[8] = 'joe'
  print(len(unsortedmap))
  print(unsortedmap)
  del unsortedmap[4]
  it = iter(unsortedmap)
  print(next(it))
  print(next(it))












