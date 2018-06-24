"""Maximum sum subarray"""
import itertools

def max_sum_subarray(A):
  if not A:
    return 0
  min_sum = max_sum = A[0]
  for sum in itertools.accumulate(A[1:]):
    min_sum = min(min_sum, sum)
    max_sum = max(max_sum, sum - min_sum)
  return max_sum
    
if __name__=="__main__":
  A = [-904, -40, -523, -12, -335, -385, -124, -481, -31]
  print('Expect 1479 Received ', max_sum_subarray(A))