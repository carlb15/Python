5.12 Sample Offline Data

IN : array distinct elements and a size
RET: subset the size of the given size. Put in input array.
     all subsets should be equally likely
     
A = [1,2,5,7,10], len(A) = 5
size = 3

library random has choice - chooses a random value out an array

[5, 10, 1, 5, 7, 10]

if not valid A or size
  throw error
  return None or A
  

for idx in range given_size:
  # if give size gets large then we can create subset 
  # large len(A) / 2
  randIdx = random.randint(idx, len(A) - idx)
  A[idx],A[randIdx] = A[randIdx], A[idx]


O(size) Time O(1) space 


BOOK answer

for idx in range(k):
  # generate random index [idx, len(A) - 1]
  randIdx = random.randint(idx, len(A) - 1)
  # swap with idx
  A[idx], A[randIdx] = A[randIdx], A[idx]
  