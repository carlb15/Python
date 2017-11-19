from bst import BinaryTree
from stack import Stack
import operator as op # handles the evaluating the expression


def handleLeftParen(root, nodeStack):
    """Create new left subtree and descend to it."""
    root.insertLeft('')
    nodeStack.push(root)
    return root.getLeftChild()


def handleOperator(token, nodeStack, root):
    """Set root value, then create & move to right subtree."""
    root.setRootVal(token)
    root.insertRight('')
    nodeStack.push(root)
    return root.getRightChild()


def handleOperand(token, nodeStack, root):
    """Set root value and move to parent."""
    root.setRootVal(int(token))
    return nodeStack.pop()


def handleTokens(tokens, nodeStack, root):
    """Process all tokens in mathematical expression."""
    for token in tokens:
        if token in '(':
            root = handleLeftParen(root, nodeStack)
        elif token in ['+', '-', '/', '*']:
            root = handleOperator(token, nodeStack, root)
        elif token.isdigit():
            root = handleOperand(token, nodeStack, root)
        elif token in ')':
            root = nodeStack.pop()
        else:
            print("Invalid Token %s!" % token)
            raise ValueError

    return root


def buildAParseTree(mathExp):
    """Build Parse tree based on mathematical expression."""
    tokens = mathExp.split()
    root = BinaryTree('')
    nodeStack = Stack()
    nodeStack.push(root)

    try:
        root = handleTokens(tokens, nodeStack, root)
    except:
        print("Invalid mathematical expression!")
        root = None

    return root


def evaluate_expression(parseTree):
    if parseTree == None:
        return None

    """Evaluate the mathematical expression and return a result."""
    opers = {'+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv}

    left = parseTree.getLeftChild()
    right = parseTree.getRightChild()

    if left and right:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate_expression(left), evaluate_expression(right))
    else:
        return parseTree.getRootVal()


if __name__=="__main__":
    # Build parse tree with valid mathematical expression.
    mathExp = '( 3 + ( 4 * 5 ) )'
    print(mathExp)
    parseTree = buildAParseTree(mathExp)
    assert(evaluate_expression(parseTree) == 23)

    del parseTree

    # Build parse tree with invalid mathematical expression.
    mathExp = '( 3 + ( 4 ] * 5 ) ) }'
    print(mathExp)
    parseTree = buildAParseTree(mathExp)
    assert(parseTree == None)
    assert(evaluate_expression(parseTree) == None)
