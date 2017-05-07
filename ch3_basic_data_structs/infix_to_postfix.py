"""Convert Infix notation to Postfix."""
from stack_2 import Stack


def is_operand(token):
    """Checks if token is an operand A-Z or 0-9, etc."""
    return token.isalpha() or token.isdigit()


def is_operator(token):
    """Checks if token is an operator '-+/*'."""
    return token in '-+/*'


def operator_gt_or_eq_to(op1, op2):
    """ Compare two operators to determine operator precedence."""
    if op1 in '/*' and op2 in '/*':
        return True
    elif op1 in '-+' and op2 in '/*-+':
        return True
    return False


def find_open_paren(opstack, postfix_list):
    """Pop tokens off stack until open ( is found."""
    while(opstack.peek() != '(' and not opstack.isEmpty()):
        postfix_list.append(opstack.pop())


def remove_ops_of_gt_eq_precedence(token, opstack, postfix_list):
    """Remove all opeartors of greater or equal precedence."""
    operatorIsGt = True
    tokenOnStack = None
    while not opstack.isEmpty() and operatorIsGt:
        tokenOnStack = opstack.peek()
        if is_operator(tokenOnStack):
            operatorIsGt = operator_gt_or_eq_to(token, tokenOnStack)
            if operatorIsGt:
                postfix_list.append(opstack.pop())
        else:
            operatorIsGt = False


def empty_opstack(opstack, postfix_list):
    """Empty the operator stack."""
    while not opstack.isEmpty():
        token = opstack.pop()
        if token != '(':
            postfix_list.append(token)


def infix_to_postfix(infix_str):
    """Convert Infix to Postfix notation."""

    infix_list = infix_str.split()
    opstack = Stack()
    postfix_list = []

    for token in infix_list:
        if is_operand(token):
            postfix_list.append(token)
        elif token == '(':
            opstack.push('(')
        elif token == ')':
            find_open_paren(opstack, postfix_list)
        elif is_operator(token):
            remove_ops_of_gt_eq_precedence(token, opstack, postfix_list)
            opstack.push(token)

    empty_opstack(opstack, postfix_list)

    return ''.join(postfix_list)


assert(infix_to_postfix('A + B') == 'AB+')
assert(infix_to_postfix('A * B + C * D') == 'AB*CD*+')
assert(infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )')
                         == 'AB+C*DE-FG+*-')
print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("( A + B ) * ( C + D )"))
print(infix_to_postfix("( A + B ) * C"))
print(infix_to_postfix("A + B * C"))
