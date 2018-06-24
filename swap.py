def swap(num1, num2):
  """Pythonic way"""
  num1, num2 = num2, num1
  return num1, num2

def swap1(num1, num2):
  """Works for integers"""
  num1 += num2 
  num2 = num1 - num2
  num1 = num1 - num2
  return num1, num2
  
def swap2(a, b):
  """Bit manipulation - works for more than integers"""
  a = a ^ b
  b = a ^ b
  a = a ^ b
  return a, b
  
  
if __name__=="__main__":
  print('(1, 2) to ', swap1(1, 2))
  print('(0, 2) to ', swap1(0, 2))
  print('(-10, 2) to ', swap1(-10, 2))
  print('(13, -32) to ', swap1(13, -32))
  print('(-31, -20) to ', swap1(-31, -20))
  
  print('bit manipulation')
  print('(1, 2) to ', swap2(1, 2))
  print('(0, 2) to ', swap2(0, 2))
  print('(-10, 2) to ', swap2(-10, 2))
  print('(13, -32) to ', swap2(13, -32))
  print('(-31, -20) to ', swap2(-31, -20))