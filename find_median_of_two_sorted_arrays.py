"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
from sys import maxsize

MAX_NUM = maxsize
MIN_NUM = -maxsize

class Solution:
  def findMedianSortedArrays(self, A, B):
    """
    :type nums_x: List[int]
    :type nums_y: List[int]
    :rtype: float
    """
    def get_median(C):
      if not C:
        return []
      if len(C) % 2 == 0:
        left = C[(len(C) - 1) // 2]
        right = C[len(C) // 2]
        return (left + right) / 2
      return C[(len(C))//2]
    
    x, y = len(A), len(B)
    # make first array the smaller one
    if x > y:
      x, y, A, B = y, x, B, A
    if x == 0 or y == 0:
      return get_median(B) if not A else get_median(A)
        
    # start and end of X
    low, high = 0, x

    # iterate through nums_x
    while low <= high:
      # create partition for X 
      partitionX = (low + high) // 2
      # create partition for Y including partition of X
      partitionY = ((x + y + 1) // 2) - partitionX
      
      # check for boundary case:
      #   1. partitionX is 0 so no left subarray
      maxLeftX  = MIN_NUM if partitionX == 0 else A[partitionX - 1]
      #   2. partitionX is at len of A so no right subarray
      minRightX = MAX_NUM if partitionX == x else A[partitionX]
      
      maxLeftY  = MIN_NUM if partitionY == 0 else B[partitionY - 1]
      minRightY = MAX_NUM if partitionY == y else B[partitionY]
      
      # determine if median is found
      if maxLeftX <= minRightY and maxLeftY <= minRightX:
        # Correct partition found.
        # 1. If combined array is even length:
        #    Get max of left elements and min of right elements
        # 2. Elif combined array is odd length:
        #    Get max of left
        if (x + y) % 2 == 0:
          return float(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
        else:
          return float(max(maxLeftX, maxLeftY))
      # Too far on right side for partitionX so move left
      elif maxLeftX > minRightY:
        high = partitionX - 1
      # too far left side for partitionX so move right
      else:
        low = partitionX + 1
  
    raise ValueError('One or both input arrays are unsorted')    

if __name__=="__main__":
  sol = Solution()
  nums1 = [1, 3]
  nums2 = [2]
  print('Expect: 2 Received:', sol.findMedianSortedArrays(nums1, nums2))
  nums1 = [1, 2]
  nums2 = [3, 4]
  print('Expect: 2.5 Received:', sol.findMedianSortedArrays(nums1, nums2))
  nums1 = [1, 2]
  nums2 = []
  print('Expect: 1.5 Received:', sol.findMedianSortedArrays(nums1, nums2))
  nums1 = []
  nums2 = [3, 4]
  print('Expect 3.5 Received:', sol.findMedianSortedArrays(nums1, nums2))
  nums1 = []
  nums2 = [4]
  print('Expect 4 Received:', sol.findMedianSortedArrays(nums1, nums2))
  nums1 = [1]
  nums2 = []
  print('Expect 1 Received:', sol.findMedianSortedArrays(nums1, nums2))