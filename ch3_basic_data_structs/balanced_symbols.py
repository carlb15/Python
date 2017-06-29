from stack_2 import Stack

"""3.7 Balanced Symbols"""

def symbolsMatch(open, close):
    openSymbol = "({["
    closeSymbol = ")}]"
    return openSymbol.index(open) == closeSymbol.index(close)

def symbolsAreBalanced(strOfSymbols):
    myStack       = Stack()
    symbolsAreBalanced = True

    for symbol in strOfSymbols:
        if symbol in "({[":
            myStack.push(symbol)
        elif symbol in ")]}" and not myStack.isEmpty():
            top = myStack.pop()

            if not symbolsMatch(top, symbol):
                symbolsAreBalanced = False
        else:
            symbolsAreBalanced = False


    return myStack.isEmpty() and symbolsAreBalanced

assert(symbolsAreBalanced("()"))
assert(symbolsAreBalanced("(())"))
assert(not symbolsAreBalanced("("))
assert(not symbolsAreBalanced("(()"))
assert(symbolsAreBalanced("()(())(())"))
assert(not symbolsAreBalanced(")"))
assert(symbolsAreBalanced("{{([][])}()}"))
assert(symbolsAreBalanced("[[{{(())}}]]"))
assert(symbolsAreBalanced("[][][](){}"))
assert(not symbolsAreBalanced("([)]"))
assert(not symbolsAreBalanced("((()]))"))
assert(not symbolsAreBalanced("[{()]"))
assert(not symbolsAreBalanced("]"))
assert(not symbolsAreBalanced("}"))
assert(not symbolsAreBalanced("[{("))
assert(symbolsAreBalanced(""))
