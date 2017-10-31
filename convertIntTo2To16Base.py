"""Convert an Integer to a String in Base 2 to 16."""
"""
1) Reduce the original to a series of single-digit numbers
2) Convert the single digit-number to a string using a lookup.
3) Concatenate the single-digit strings together to form the final result.
"""

def toStr(n, base):
  toStr = ''
  digit = ['0', '1', '2', '3', '4', '5', '6', '7', 
           '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
  
  while n >= base:
    n, r = divmod(n, base)
    toStr += digit[r]
  
  toStr += digit[n]
  return toStr[::-1] 
  

if __name__ == "__main__":
  
  for idx in range(2, 17):
    print(toStr(10, idx))