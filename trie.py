"""Trie Data Structure"""

class TrieNode:
  """Trie Node Class."""
  ALPHABET = 26
  
  def __init__(self):
    # Number of children is size of the alphabet
    # this can be a map to generalize for unicode.
    self.children = [None] * TrieNode.ALPHABET
    # isEndOfWord is True is node represents the end of a word.
    self.isEndOfWord = False
  
  def leafNode(self):
    """Check if node is leaf node or not."""
    return self.isEndOfWord
  
  def isAFreeNode(self):
    """If node has no children then it's free."""
    for child in self.children:
      if child:
        return False
    return True


class Trie:
  """Trie Class
  Memory Requirement: O(ALPHABET_SIZE * k * N)
  where N is the number of keys in trie.
  ALPHABET_SIZE = 26
  """
  
  def __init__(self):
    """Initialize a Trie"""
    self.root = self.getNode()
  
  def getNode(self):
    """Retrieve a new Trie Node."""    
    return TrieNode()
  
  def _charToIndex(self, ch):
    """Private helper function
       Converts key current character into index
       use only 'a' through 'z' and lower case
    """
    return ord(ch) - ord('a')
    
  def insert(self, key):
    """
    If not present, inserts key into Trie
    If key is prefix of trie node,
    just mark leaf node 
    O(k) Time where k is the length of key
    """
    pCrawl = self.root
    length = len(key)
    # For each character in the key
    for level in range(length):
      # Convert the character into an index.
      index = self._charToIndex(key[level])
      
      # if current character is not present
      if not pCrawl.children[index]:
        # Replace the None with the character.
        pCrawl.children[index] = self.getNode()
      # Move pCrawl to that character
      pCrawl = pCrawl.children[index]
      
    # Mark last character of key as leaf node.
    pCrawl.isEndOfWord = True

  def search(self, key):
    """
    Search key in trie 
    Returns true if key present in trie,
    else false 
    O(k) time where k is the length of key.
    """
    # start at the root of the trie
    pCrawl = self.root
    length = len(key)
    # Go level by level (i.e. character by character)
    for level in range(length):
      # Get the index of the character at the current level
      index = self._charToIndex(key[level])
      # key not present in the trie, i.e., current character 
      # not present at this level then word isn't present in
      # the trie.
      if not pCrawl.children[index]:
        return False
      # move to the character in the trie 
      pCrawl = pCrawl.children[index]
    
    # when the last character is valid
    # and it's a leaf node (end of word) return True.
    return pCrawl and pCrawl.isEndOfWord


  def _deleteHelper(self, node, key, level, length):
    """Helper function for deleting key from trie."""
    if node:
      # Base Case
      if level == length:
        # if node is a leaf node then unmark it.
        if node.leafNode():
          node.isEndOfWord = False
        
        # If node is empty then delete it.
        return node.isAFreeNode()    
      else:
        # Get the index of the character
        index = self._charToIndex(key[level])
        # get next level to delete
        if self._deleteHelper(node.children[index], \
                              key, \
                              level + 1, \
                              length):
          # last node marked for deletion
          del node.children[index]
          
          # recursively move up and delete eligible nodes.
          # i.e. 1. a leaf node without children.
          return not node.leafNode() and \
                     node.isItFreeNode()
    return False
        
  
  def delete(self, key):
    """
      Delete a node from the trie.
      1. Key may not be in trie. delete() shouldn't modify trie.
      2. Key present as unique key (not part of key contains another
         key (prefix), nor key itself is prefix of another key. Delete all nodes.
      3. Key is prefix of another long key in trie. Unmark   
         leaf node.
      4. Key is present and atleast one other is a prefix, then delete nodes from 
         end of key until first leaf node of longest prefix key.
    """
    length = len(key)
    if length > 0:
      # delete starting at the root
      self._deleteHelper(self.root, key, 0, length)


# driver function
def main():
  # Input keys (use only 'a' through 'z' and lower case)
  keys = ["the","a","there","anaswe","any",
          "by","their"]
  output = ["Not present in trie",
            "Present in trie"]

  # Trie object
  t = Trie()

  # Construct trie
  for key in keys:
      t.insert(key)

  # Search for different keys
  print("{} ---- {}".format("the",output[t.search("the")]))
  print("{} ---- {}".format("these",output[t.search("these")]))
  print("{} ---- {}".format("their",output[t.search("their")]))
  print("{} ---- {}".format("thaw",output[t.search("thaw")]))
  
  t.delete(keys[0])
 
  print("{} {}".format(keys[0],\
        "Present in trie" if t.search(keys[0]) \
                        else "Not present in trie"))

  print("{} {}".format(keys[6],\
        "Present in trie" if t.search(keys[6]) \
                          else "Not present in trie"))

if __name__ == '__main__':
  main()
