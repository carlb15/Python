def BinaryTree(r):
  """Create a new binary tree."""
  return [r, [], []]

def insertLeft(root, newBranch):
  """Insert a new left node."""
  t = root.pop(1) # get the left child
  if len(t) > 1:
    # add new left child to root and 
    # make old left child it's left child.
    root.insert(1, [newBranch, t, []])
  else:
    root.insert(1, [newBranch, [], []])
  return root

def insertRight(root, newBranch):
  """Insert a new right node."""
  t = root.pop(2) # get the right child
  if len(t) > 1:
    root.insert(2, [newBranch, [], t])
  else:
    root.insert(2, [newBranch, [], []])
  return root

def getRootVal(root):
  """Get the root's value."""
  return root[0]

def setRootVal(root, newVal):
  """Set the root value."""
  root[0] = newVal

def getLeftChild(root):
  """Get the left child."""
  return root[1]
  
def getRightChild(root):
  """Get the right child."""
  return root[2]