"""Coin change Problem"""
"""
EX:
Change for $51 using ($1, 2, 5, 10, 20)

Greedy Approach
  Subtract largest bills
    51 -20 = 31 - 20 = 11 - 10= 1 - 1= 0
      20, 20, 10, 1 = 5 bills
  
What if bills to use were (3, 5, 7, 11)?
Smallest # bills for $13?
  13 - 11 = 2 Can't go further

C dollars want to use 1 d dollar
  C - d bills + 1 for using one d dollar.
  EX: $10 and 2 dollar bills
    min to make $10 -> min to make $8 + 1 ->
    min to make $6 + 2 -> $4 + 3 -> $2 + 4 -> $0 + 5
    = 5 $2 bills to make $10

Base Case:
  C where is is some # of dollars.
  Bills(0) = 0
  Bills(C) = impossible if C < 0
  
Subproblem:
  Bills(C) = Bills(C - d) + 1 if bills(C -d) is possible
    
  Bills(C) = impossible if bills(C - d) is impossible
    EX: C = 10, d=100 -> C-d = -90 impossible 
    
EX:
C = 10
d = 2

bills(10)
  = bills(8) + 1
  = bills(6) + 1 + 1
  = bills(4) + 1 + 1 + 1
  = bills(2) + 1 + 1 + 1 + 1
  = bills(0) + 1 + 1 + 1 + 1 + 1
  = 5

bills[0] = 0

for c from 1 to C
  if c - d >= 0 and bills[c - d] is not impossible:
    bills[c] = bills[c-d] + 1
  else:
    bills[c] = impossible
 
return bills[C-1]
    

Extend to mutiple denominations
  - if we want to see all possible combinations
    then we need try all of them and get the min # bills.
  - dn is some denomination min(C-dn)
  -

let denom[] be an array of denominations
let bills[C] be smallest amount of bills to make C with denoms

Base Case:
  bills[0] = 0
  
Subproblem
for c from 1 to C
  bills[c] = impossible
  for d in denom
    if c-d >0 and bills[c-d] is not impossible
      bill[c] = min(bills[c], bills[c-d] + 1)
  
  
EX:
  denom = [3,4,5]
  C = 7
  bills[0] = 0
  bills[1] = impossible (bills[1 -3], bills[1-4], bills[1-5] are      
             impossible   
             
  ...
  bills[C] = (bills[3] + 1 or bills[4] + 1)

"""

def min_number_of_bills(C, denom):
  # base case
  if C == 0:
    return 0
  
  bills = [0] * (C + 1)
  for c in range(1, C + 1):
    bills[c] = float('inf')
    for d in denom:
      if c - d >= 0 and bills[c - d] != float('inf'):
        bills[c] = min(bills[c], bills[c - d] + 1)
        
  return bills[C]

  
if __name__=="__main__":
  print('C = 7, Expect 2 Returned ', min_number_of_bills(7, [3,4,5]))































