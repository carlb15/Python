"""Binary tree implementation."""


class BinaryTree:
    """Binary Tree implementation."""

    def __init__(self, rootObj):
        """Initialization of BST."""
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """Insert node into left subtree."""
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        """Insert into right subtree."""
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        """Get root's right child."""
        return self.rightChild

    def getLeftChild(self):
        """Get root's left child."""
        return self.leftChild

    def setRootVal(self, rootObj):
        """Set the root's value."""
        self.key = rootObj

    def getRootVal(self):
        """Get the root's value."""
        return self.key


def buildTree():
    r = BinaryTree('a')
    r.insertLeft('b')
    r.getLeftChild().insertRight('d')
    r.insertRight('c')
    r.getRightChild().insertLeft('e')
    r.getRightChild().insertRight('f')
    return r

def printTree(root):
    if root == None:
        return
    print(root.getRootVal())
    printTree(root.getLeftChild())
    printTree(root.getRightChild())

if __name__=="__main__":
    root = buildTree()
    printTree(root)
"""
    r = BinaryTree('a')
    print(r.getRootVal())
    assert(r.getRootVal() == 'a')
    print(r.getLeftChild())
    assert(r.getLeftChild() == None)
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    assert(r.getLeftChild().getRootVal() == 'b')
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    assert(r.getRightChild().getRootVal() == 'c')
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())
    assert(r.getRightChild().getRootVal() == 'hello')
"""
