"""Quick Sort"""

def quick_sort(A):
  def sort_helper(A, left, right):
    def partition(left, right):
      # Pivot is the midpoint of left and right.
      pivot = A[(left + right) // 2]
      
      # Go until left > right 
      while left <= right:
        # Find left element greater than pivot
        while A[left] < pivot:
          left += 1
        # Find right element less than pivot
        while A[right] > pivot:
          right -= 1
          
        # when left is still <= right, swap
        if left <= right:
          A[left],A[right] = A[right], A[left]
          left += 1
          right -= 1
      # return the left index
      return left

    # partition the array
    partitionIdx = partition(left, right)
    
    # check if left side can be sorted
    if left < partitionIdx - 1:
      sort_helper(A, left, partitionIdx - 1)
    # check if right side can be sorted
    if right > partitionIdx:
      sort_helper(A, partitionIdx, right)
    # return sorted array
    return A

  return sort_helper(A, 0, len(A) - 1)

if __name__=="__main__":
  print(quick_sort([10, 3, 1, 41, 32, 2]))