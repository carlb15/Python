"""Map Base Class."""
from collections import MutableMapping

class MapBase(MutableMapping):
  """Our own abstract base class that includes a nonpublic _Item class."""

  #------------------------ nested _Item class --------------------------#
  class _Item:
    __slots__ = '_key', '_value'
    
    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __equal__(self, other):
      """Compare items based on their keys."""
      return self._key == other._key

    def __ne__(self, other):
      """Not equal."""
      return not (self == other)

    def __lt__(self, other):
      """Less than Comparison for keys."""
      return self._key < other._key

    def __repr__(self):
      return "key %s value %s" % (self._key, self._value)
      
      
      
      
      