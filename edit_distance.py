"""
72. Edit Distance
Given two words word1 and word2, find the minimum number of 
operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

  Insert a character
  Delete a character
  Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""

[    r  o  s
   0 0  0  0  
h  0 -  -  -
o  0 -  -  -
r  0 -  -  -
s  0 -  -  -
e  0 -  -  -
]
Base Case:              
if row < 0: # all values left in word2
return col + 1
elif col < 0:
return row + 1

if memo[row][col] == -1:
if word1[row] == word2[col]:
  memo[row][col] = memo[row - 1][col - 1]
else:
  memo[i][j] =  min( minDistHelper(i - 1, j) + 1,      # delete
                     minDistHelper(i - 1, j  - 1) + 1, # replace
                     minDistHelper(i, j - 1) + 1)      # add    
return memo[row][col]

word1 = "horse", word2 = "ros"
cases
1. word1[i - 1], word2[j - 1] if ch1 == ch2
Get the previous computed value
2. memo[i][j] =  min( minDistHelper(i - 1, j) + 1,      # delete
                    minDistHelper(i - 1, j  - 1) + 1, # replace
                    minDistHelper(i, j - 1) + 1)      # add                  
O(n*m) Time O(n*m) Space


class Solution:
def minDistance(self, A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """  
    def editDistHelper(memo, a_idx, b_idx):
      # get the rest of B
      if a_idx < 0:
        return b_idx + 1
      # get the rest of A
      if b_idx < 0:
        return a_idx + 1
      
      # character edit not computed 
      if memo[a_idx][b_idx] == -1:
        # characters match so get edit from previous edit.
        if A[a_idx] == B[b_idx]:
          memo[a_idx][b_idx] = editDistHelper(memo, a_idx - 1, b_idx - 1)
        # try deleting, adding, substituting 
        else:
          deleteLast = editDistHelper(memo, a_idx, b_idx - 1)
          subLast = editDistHelper(memo, a_idx - 1, b_idx - 1)
          addLast = editDistHelper(memo, a_idx - 1, b_idx)
          memo[a_idx][b_idx] = min(deleteLast, subLast, addLast) + 1
      
      return memo[a_idx][b_idx]


    if not A and not B:
      return 0
    elif not A:
      return len(B)
    elif not B:
      return len(A)
    
    memo = [[-1] * (len(B)) for _ in range(len(A))]

    editDistHelper(memo, len(A) - 1, len(B) - 1)

    return memo[-1][-1]
