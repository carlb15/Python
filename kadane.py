def kadane_track_indices(arr):
  """
  Implementation of Kadane's algorithm for finding the sub-array
  with the largest sum. Track the indices of the sub-array.

  Note: Doesn't handle duplicate max values.

  O(n) Time Complexity 
  O(1) Space Complexity.
  """

  # stores max sum sub-array found so far
  max_so_far = 0

  # stores max sum of sub-array ending at current position
  max_ending_here = 0
  
  # start and end points of max sum sub-array.
  start = 0
  end = 0

  # start index of positive sum sequence
  beg = 0

  for idx in range(len(arr)):
    # if all array elements are negative.
    if (max(arr) < 0):
      max_so_far = max(arr)
      start = arr.index(max_so_far)
      end = start + 1
      break

    # Update max sum sub-array ending @ index i by
    # adding current element to max sum ending at previous idx.
    max_ending_here = max_ending_here + arr[idx]

    if max_ending_here < 0:
      max_ending_here = 0
      # reset start of positive sum sequence
      beg = idx + 1
    
    if max_so_far < max_ending_here:
      # update the max sum
      max_so_far = max_ending_here
      # update max sum sub-array indices
      start = beg
      end = idx

  print("The sum of contiguous sub-array with largest sum is %d", max_so_far)
  print("The contiguous sub-array with the largest sum is ", arr[start:end])

  return max_so_far


def kadane(arr):
  """
  Implementation of Kadane's algorithm for finding the sub-array
  with the largest sum.
  
  O(n) Time Complexity 
  O(1) Space Complexity.
  """

  # stores max sum sub-array found so far
  max_so_far = arr[0]

  # stores max sum of sub-array ending at current position
  max_ending_here = arr[0]

  for idx in range(len(arr)):
    # Update max sum sub-array ending @ index i by
    # adding current element to max sum ending at previous idx.
    max_ending_here = max_ending_here + arr[idx]

    # if max sum is negative, set it to 0 to represent and
    # empty sub-array
    max_ending_here = max(max_ending_here, arr[idx])

    # update result if current sub-array sum is greater
    max_so_far = max(max_so_far, max_ending_here)

  return max_so_far
  

if __name__=="__main__":
  assert(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
  assert(kadane([-8, -3, -6, -2, -5, -4]) == -2)
  assert(kadane_track_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
  assert(kadane_track_indices([-8, -3, -6, -2, -5, -4]) == -2)