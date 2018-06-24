"""Merge Two sorted arrays."""


def merge_sorted_arrays(A, B, lastA, lastB):
  if not A or not B:
    return None
  
  while B:
    bValue = B.pop()
    lastA += 1
    A[lastA] = bValue
    idx = lastA
    while idx > 0 and A[idx] < A[idx - 1]:
      A[idx], A[idx - 1] = A[idx - 1], A[idx]
      idx -= 1

  return A


if __name__=="__main__":
  A = [2, 3, 5, 0, 0]
  B = [1, 4]
  print(merge_sorted_arrays(A, B, 2, 1))
  print(merge_sorted_arrays(A, [], 2, 1))
  print(merge_sorted_arrays([], B, 2, 1))
  A = [2, 3, 5, 0]
  B = [1]
  print(merge_sorted_arrays(A, B, 2, 0))
  A = [2, 3, 5, 0]
  B = [6]
  print(merge_sorted_arrays(A, B, 2, 0))