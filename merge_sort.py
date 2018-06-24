"""Merge Sort"""

def merge(A, tempA, left, mid, right):
  # copy elements into temporary array.
  for i in range(left, right + 1):
    tempA[i] = A[i]
  
  helperLeft = left
  helperRight = mid + 1
  curr = left
  
  # merge left and right elements into array A
  while helperLeft <= mid and helperRight <= right:
    if tempA[helperLeft] <= tempA[helperRight]:
      A[curr] = tempA[helperLeft]
      helperLeft += 1
    else:
      A[curr] = tempA[helperRight]
      helperRight += 1
    curr += 1
  
  remaining = mid - helperLeft
  for i in range(remaining + 1):
    A[curr + i] = tempA[helperLeft + i]
  return left

def merge_sort(A):
  def sort_helper(A, tempA, left, right):
    if left < right:
      mid = (left + right) // 2
      sort_helper(A, tempA, left, mid)
      sort_helper(A, tempA, mid + 1, right)
      merge(A, tempA, left, mid, right)

  tempA = [0] * len(A)
  sort_helper(A, tempA, 0, len(A) - 1)
  return A

if __name__=="__main__":
  print(merge_sort([51, 1, 42, 2, 10, 100, 32]))