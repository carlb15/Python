"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        O(len(s)) Time 
        O(len(s)) Space
        """
        if not s:
            return True
        elif len(s) == 1:
            return False
        
        brackets = {')':"(", 
                    "}":"{", 
                    "]":'['}          
        
        stack = []
        for ch in s:
            if ch in brackets.values():
                stack.append(ch)            
            elif len(stack) > 0 and brackets[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return False if len(stack) != 0 else True

