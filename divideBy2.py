from stack_2 import Stack
""" Divide by  2 algorithm """

def divideBy2(decimalNum):
  binString  = str()
  myStack = Stack()

  if decimalNum == 0:
      return "0"
  elif decimalNum < 0:
      return None

  while decimalNum > 0:
      myStack.push(decimalNum % 2)
      decimalNum //= 2

  while not myStack.isEmpty():
      binString += str(myStack.pop())

  return binString

print(divideBy2(-1))
print(divideBy2(0))
print(divideBy2(1))
print(divideBy2(2))
print(divideBy2(3))
print(divideBy2(4))
print(divideBy2(20))
print(divideBy2(42))
print(divideBy2(233)) # 11101001
