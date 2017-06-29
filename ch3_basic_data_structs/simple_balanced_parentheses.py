from stack_2 import Stack

"""3.6 Simple balanced parentheses"""

def parenthesesAreBalanced(strOfParens):
    myStack       = Stack()
    parenBalanced = True

    for paren in strOfParens:
        if paren in "(":
            myStack.push("(")
        elif paren in ")" and not myStack.isEmpty():
            myStack.pop()
        else:
            parenBalanced = False

    return myStack.isEmpty() and parenBalanced

assert(parenthesesAreBalanced("()"))
assert(parenthesesAreBalanced("(())"))
assert(not parenthesesAreBalanced("("))
assert(not parenthesesAreBalanced("(()"))
assert(parenthesesAreBalanced("()(())(())"))
assert(not parenthesesAreBalanced(")"))
