"""Find duplicates in an array in O(n) time O(1) Space
  Given array n elements which contains elements from 0 to n-1
  EX: N = 7 [1,2,3,1,3,6,6] Answer = [1, 3, 6]
"""

"""
My Algorithm:
  #Option 1.
    result = []
    counting sort to order input array A
    iterate thru array checking adjacent numbers 
      if idx-1 == idx 
        add to result
""" 
  #Option 2:
  # iterate through array 0 to n-1
  # if arr[abs(x) - 1] is negative then DUP
  # otherwise make arr[abs(x) - 1] *= -1
  
  
    def findDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """      
        result = []
        # iterate through numbers
        for x in nums:
            # number is negative its
            # index then its a duplicate
            if nums[abs(x)-1] < 0:
                result.append(abs(x))
            # mark first occurrence of number as negative
            else:
                nums[abs(x)-1] *= -1
        return result
        