"""66. Plus One - https://leetcode.com/problems/plus-one/description/"""
"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

  
"""

'''
Solution:
  1. Parse array from end 
  2. If last element is 9, make it 0 and carry = 1
  3. For next iteration check if digits[i] + carry == 10
     repeat step 2
  4. If list add and increase list size, append 1 to beginning
  
  
  
  
  
   
    
    
    
    
    
    
    
  
'''

"""
Optimal Solution:

"""