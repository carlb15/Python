"""
Let fib(n) be the nth Fibonacci number
 
Base case:
fib(0) = 1, fib(1) = 1
 
Subproblem:
fib(n) = fib(n - 1) + fib(n - 2)
 
Example:
fib(5) 
= fib(4) + fib(3) 
= fib(3) + fib(2) + fib(2) + fib(1) 
= fib(2) + fib(1) + fib(1) + fib(0) + fib(1) + fib(0) + fib(1) 
= fib(1) + fib(0) + fib(1) + fib(1) + fib(0) + fib(1) + fib(0) + fib(1) 
= 1 + 1 + 1 + 1 + 1 + 1 + 1 = 8  
"""

"""
Fibonacci number

Base Case:
  fib(0) = 0 fib(1) = 1

General Form:
  fib(2) = fib(1) + fib(0)
  fib(n) = fib(n-1) + fib(n-2)

Recursion O(2^n)

[0, 1, ]
for idx = 2 to n+1:
  A[idx]= A[idx-1] + A[idx-2]

return A[n]
O(n) Time 
O(n) Space

Improvement is to store A[idx-1] A[idx-2] instead of Array
  O(1) Space
"""
  
def fib(n):
  if n==0 or n == 1:
    return 1
  
  fib_i_minus_2, fib_i_minus_1 = 1, 1
  fib_i = 0
  for idx in range(2, n + 1):
    fib_i = fib_i_minus_2 + fib_i_minus_1 # 8
    fib_i_minus_2 = fib_i_minus_1 # 3
    fib_i_minus_1 = fib_i # 5
  
  return fib_i


if __name__=="__main__":
  print("For fib(5) - Expect 8 Returned ",fib(5))




  
  
  
  
  
  
  
  
  
  