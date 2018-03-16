"""Find a pair with given sum in a BST"""

class Node():
  """Node class."""
  def __init__(self, initdata):
    """Initialize the node."""
    self.data = initdata
    self.left = None
    self.right = None

def preorder(root):
  if root == None:
    return

  print(root.data)
  preorder(root.left)
  preorder(root.right)


if __name__=="__main__":
  root = Node(15)
  root.left = Node(10)
  root.right = Node(25)

  l = root.left
  l.left = Node(8)
  l.right = Node(12)
  l.left.left = Node(6)
  l.left.right = Node(9)

  r = root.right
  r.left = Node(20)
  r.left.left = Node(18)
  r.left.right = Node(22)
  r.right = Node(30)

  