def search(A, left, right, target):
  if right < left \
    or right > (len(A) - 1) \
    or left < 0:
    return -1

  mid = int((left + right) // 2)
  if target == A[mid]:
    return mid

  idx = -1
  
  if A[left] <= target <= A[mid]:
    return search(A, left, mid - 1, target)
  elif A[mid] <= target <= A[right]:
    return search(A, mid + 1, right, target)
  else:
    idx = search(A, left, mid - 1, target)
    if idx == -1:
      return search(A, mid + 1, right, target)
    else:
      return idx
  return -1
"""
  # Left side is sorted
  if A[left] < A[mid]:
    # target is in range of mid and left
    if A[left] <= target <= A[mid]:
      return search(A, left, mid - 1, target)
    # target is on the right
    else:
      return search(A, mid + 1, right, target)
  # Right side is sorted
  elif A[mid] < A[left]:
    # target is in range of mid and right
    if A[mid] <= target <= A[right]:
      return search(A, mid + 1, right, target)
    # target is on the left
    else:
      return search(A, left, mid - 1, target)
  # check left is all duplicates
  elif A[left] == A[mid]:
    # Right side is different
    if A[mid] != A[right]:
      return search(A, mid + 1, right, target)
    else:
      # Search both sides since duplicates on each side.
      idx = search(A, left, mid - 1, target)
      if idx == -1:
        idx = search(A, mid + 1, right, target)
      else:
        return idx

  return -1
"""

if __name__=="__main__":
  A1 = [10, 15, 20, 0, 5]
  A2 = [50, 5, 20, 30, 40]
  A3 = [2, 2, 2, 3, 4, 2]
  assert(search(A1, 0, len(A1) - 1, 5) == 4)
  assert(search(A2, 0, len(A2) - 1, 5) == 1)
  assert(search(A3, 0, len(A3) - 1, 5) == -1)
  assert(search([], 0, len(A3) - 1, 5) == -1)
  assert(search(A3, 0, len(A3), 2) == -1)
  assert(search(A3, -1, len(A3) - 1, 2) == -1)