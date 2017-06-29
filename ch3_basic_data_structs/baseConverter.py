from stack_2 import Stack
""" Convert between bases 2-16 """

def baseConverter(decimalNum, base):
  binString  = str()
  myStack    = Stack()
  digits     = "0123456789ABCDEF"

  if decimalNum == 0:
      return "0"
  elif decimalNum < 0:
      return None
  elif base < 2 or base > 16:
      return None

  while decimalNum > 0:
      rem = decimalNum % base
      myStack.push(rem)
      decimalNum //= base

  while not myStack.isEmpty():
      binString += str(digits[myStack.pop()])

  return binString

print(baseConverter(-1, 2))
print(baseConverter(2, -2))
print(baseConverter(10, 1000))
print(baseConverter(0, 2))
print(baseConverter(1, 8))
print(baseConverter(3, 2))
print(baseConverter(4, 2))
print(baseConverter(20, 2))
print(baseConverter(42, 2))
print(baseConverter(233, 2))  # 11101001
print(baseConverter(233, 8))  # 351
print(baseConverter(233, 16)) # E9
print(baseConverter(256, 16))
print(baseConverter(26, 26))
