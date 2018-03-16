"""Binary Search Implementations."""

def binarySearch(alist, item, start, end):
  """
  Recursive Binary Search.
  O(log(n)) time complexity.
  :type alist of ordered values.
  :type item to find
  :type starting index
  :type ending index
  """
  if start > end:
    return False

  mid = (start + end) // 2
  if alist[mid] == item:
    return True
  elif alist[mid] > item:
    end = mid - 1
    return binarySearch(alist, item, start, end)
  else:
    start = mid + 1
    return binarySearch(alist, item, start, end)

def binary_search(alist, item):
  """
  Iterative Binary Search.
  O(log(n)) time complexity.
  :type alist ordered values.
  :type the item to find.
  :rtype True or False if item is in list.
  """
  left = 0
  right = len(alist) - 1

  # iterate while left index isn't
  # greater than the right index.
  while left <= right:
    # determine the midpoint of the list.
    mid = (left + right) // 2
    # check if midpoint is the item
    if alist[mid] == item:
      return True
    # search the left half if item 
    # is smaller than the midpoint
    if alist[mid] > item:
      right = mid - 1
    # search the right half if item
    # is greater than the midpoint.
    elif alist[mid] < item:
      left = mid + 1
  # item is not in the list.
  return False

if __name__=="__main__":
  print("Iterative solution testing.")
  alist = [1,2,3,4,5,6,7,8,9,10]
  assert(binary_search(alist, 1) == True)
  assert(binary_search(alist, 7) == True)
  assert(binary_search(alist, 4) == True)
  assert(binary_search(alist, 2) == True)
  assert(binary_search(alist, 10) == True)
  alist = [1]
  assert(binary_search(alist, 10) == False)
  assert(binary_search(alist, 1) == True)
  
  testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
  print(binary_search(testlist, 3))
  print(binary_search(testlist, 13))
  
  print("Recursive solution testing.")
  alist = [1,2,3,4,5,6,7,8,9,10]
  assert(binarySearch(alist, 1, 0, len(alist) - 1) == True)
  assert(binarySearch(alist, 7, 0, len(alist) - 1) == True)
  assert(binarySearch(alist, 4, 0, len(alist) - 1) == True)
  assert(binarySearch(alist, 2, 0, len(alist) - 1) == True)
  assert(binarySearch(alist, 10, 0, len(alist) - 1) == True)
  alist = [1]
  assert(binarySearch(alist, 10, 0, len(alist) - 1) == False)
  assert(binarySearch(alist, 1, 0, len(alist) - 1) == True)
  
  testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
  print(binarySearch(testlist, 3, 0, len(testlist) - 1))
  print(binarySearch(testlist, 13, 0, len(testlist) - 1))
  
  
  