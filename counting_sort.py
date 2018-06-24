"""counting sort"""

def counting_sort(A):
  k = 9
  L = [[] for _ in range(k)]
  
  for i in range(len(A)):
    L[key(A[i])].append(A[j])
  
  output = []
  for i in range(k):
    output.extend(L[i])
  
  print(output)

import random as rand
if __name__=="__main__":
  li = [rand.randint(0,10) for _ in range(10)]
  print('Before ', li)
  print('After ', counting_sort(li))
