583. Delete Operation for Two Strings

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.


class Solution:
    def minDistance(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """        
        # if A == B return 0
        # if A[i] != B[j]
        # Need to compute the Longest common subsequence of A and B
        # result = len(A) + len(B) - 2 * LCS(A, B)
        # if there's no LCS then to get A == B need to del all of A and B
        # otherwise if LCS exists need to remove LCS from len(A) + len(B)
        # calculation.
        def lcs(memo, a_idx, b_idx):
            # reach base case for A or B
            if a_idx == 0 or b_idx == 0:
                return 0
            
            if memo[a_idx - 1][b_idx - 1] == -1:
                # continue adding to subsequence
                if A[a_idx - 1] == B[b_idx - 1]:
                    memo[a_idx - 1][b_idx - 1] = 1 + lcs(memo, a_idx - 1, b_idx - 1)
                else: # delete from A and B
                    memo[a_idx - 1][b_idx - 1] = max(lcs(memo, a_idx, b_idx - 1),\
                                                     lcs(memo, a_idx - 1, b_idx))
            
            return memo[a_idx - 1][b_idx - 1]
            
        memo = [[-1] * len(B) for _ in A]
    
        return len(A) + len(B) - (2 * lcs(memo, len(A), len(B)))
 
 
 
 class Solution:
    def minDistance(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        O(n*m)time O(m)space
        """        
        if not A:
            return len(B)
        elif not B:
            return len(A)
        
        DP = [0] * (len(B) + 1)
            
        for a_idx in range(len(A) + 1):
            temp = [0] * (len(B) + 1)
            for b_idx in range(len(B) + 1):
                # if either is 0 then get the index of the other
                # first row and column will be 1-len(A) or len(B)
                if a_idx == 0 or b_idx == 0:
                    temp[b_idx] = a_idx + b_idx
                # if equal char then carry previous char edit.
                elif A[a_idx - 1] == B[b_idx - 1]:
                    temp[b_idx] = DP[b_idx - 1]
                # get min of deleting from A or B
                else:
                    temp[b_idx] = 1 + min(temp[b_idx - 1], DP[b_idx])
            # use previous row for next row.
            DP = temp 
        return DP[-1]