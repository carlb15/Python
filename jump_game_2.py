"""
45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

class Solution:
    def jump(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(A) < 2:
            return 0
        
        stairs = A[0]
        ladder = A[0]
        jumps = 1    
        
        for idx in range(1, len(A)):
            # end of jumps
            if idx == len(A) - 1:
                return jumps
            
            # check if current value
            # in A is new ladder to store
            if A[idx] + idx > ladder:
                ladder = A[idx] + idx
            
            stairs -= 1 
            
            if stairs == 0:
                stairs = ladder - idx
                jumps +=  1
        
        return jumps