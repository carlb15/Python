
def binarySearchHelper(item, numberList, left, right):
  if left > right:
    return -1
  
  mid = left + ((right - left) // 2)
  if numberList[mid] == item:
    return mid
  elif numberList[mid] > item:
    return binarySearchHelper(item, numberList, left, mid - 1)
  
  return binarySearchHelper(item, numberList, mid + 1, right)

def binarySearch(item, numberList):
  left = 0
  right = len(numberList) - 1
  
  print("%d" % binarySearchHelper(item, numberList, left, right))
  
  return False if binarySearchHelper(item, numberList, left, right) == -1  else True

if __name__ == "__main__":
  numberList = [1, 4, 6, 8, 12, 15, 18, 19, 24, 27, 31, 42, 43, 58]
  item = int(input("What number are you looking for? "))
  isItFound = binarySearch(item, numberList)
  if isItFound:
    print("Your number is in the list!")
  else:
    print("Your number is not in the list.")
