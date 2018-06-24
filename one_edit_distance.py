"""
161. One Edit Distance

Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

1. Insert a character into s to get t
2. Delete a character from s to get t
3. Replace a character of s to get t

Example 1:

  Input: s = "ab", t = "acb"
  Output: true
  Explanation: We can insert 'c' into s to get t.

Example 2:

  Input: s = "cab", t = "ad"
  Output: false
  Explanation: We cannot get t from s by only one step.

Example 3:

  Input: s = "1203", t = "1213"
  Output: true
  Explanation: We can replace '0' with '1' to get t.
"""
  
class Solution:
def isOneEditDistance(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # get length of s and t
    m, n = len(s), len(t)
    # if their distance is > 1 then False
    if abs(m - n) > 1:
        return False
    
    # iterate through both strings
    for i in range(min(m, n)):
        # if characters differ
        if s[i] != t[i]:
            # for equal strings 
            if m == n:
                # see if the rest of string is the same
                return s[i + 1:] == t[i + 1:]
            # if s is larger see if the rest of s is equal to t
            elif m > n:
                return s[i + 1:] == t[i:]
            # if t is larger see if rest of t is equal to s
            elif m < n:
                return s[i:] == t[i + 1:]

    # check if string are different by one with 1 delete.
    # This will handle returning false if strings are the same.
    return m != n

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
