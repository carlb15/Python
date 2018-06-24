"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9
"""

"================Bottom-up SOLUTION==========================="
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        O(n*sqrt(n)) Time
        O(n) Space
        """
        if n == 0 or n == 1:
            return n
        
        A = [MAX_NUM] * (n + 1)
        A[0] = 0
        
        for idx in range(1, n + 1):
            k = 1
            while k*k <= idx:
                A[idx] = min(A[idx], A[idx - k*k] + 1)                
                k += 1
        return A[n]

"================MEMOIZED SOLUTION==========================="
        
        
from sys import maxsize as MAX_NUM
from math import sqrt

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        
        O(n*sqrt(n)) Time
        O(n) Space
        """
        def numSquaresHelper(n, memo):
            # precalculated value
            if memo[n] != MAX_NUM:
                return memo[n]
            
            root = int(sqrt(n))
            min_num = MAX_NUM
            
            for idx in range(root, 0, -1):
                min_num = min(numSquaresHelper(n - idx * idx, memo), min_num)
            
            memo[n] = min_num + 1
            return memo[n]
        
        memo = [MAX_NUM] * (n + 1)
        memo[0] = 0
        return numSquaresHelper(n, memo)