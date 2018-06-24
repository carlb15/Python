Given an integer, write a function to determine if it is a power of three.
  3^0 = 1 = 0001
  3^1 = 3 = 0011
  3^2 = 9 = 1001
  3^3 = 27 = 
  3^4 = 81
  
  if n == 0:
    return False
  if n == 1:
    return True
  
  n = input value
  while n > 1:
    if n % 3 != 0:
      return False
    n /= 3
  return True
  
  Example 1:
    Input: 27
    Output: true

  Example 2:
    Input: 0
    Output: false

  Example 3:
    Input: 9
    Output: true

  Example 4:
    Input: 45
    Output: false

Follow up:
Could you do it without using any loop / recursion?

Yes, use math.

n is a power of three if and only if i is an integer. 
In Java, we check if a number is an integer by taking the decimal part (using % 1) and checking if it is 0.

public class Solution {
    public boolean isPowerOfThree(int n) {
        return (Math.log10(n) / Math.log10(3)) % 1 == 0;
    }
}

In particular, n is of type int. In Java, this means it is a 4 byte, signed integer [ref]. The maximum value of this data type is 2147483647. Three ways of calculating this value are

MatInt = (2**32 // 2) - 1 = 2147483647

3**floor(log(2147483647,3)) = 1162261467

public class Solution {
    public boolean isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
}
Complexity Analysis

Time complexity : O(1). We are only doing one operation.

Space complexity : O(1). We are not using any additional memory.