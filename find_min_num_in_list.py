import sys
import time
from random import randrange

def find_min_num_in_list_1(myList):
  """ O(n2) solution """
  minNum = sys.maxsize
  
  for i in range(len(myList)):
    for j in range(len(myList)):
      if myList[i] < myList[j] and myList[i] < minNum:
        minNum = myList[i]
      elif myList[j] < myList[i] and myList[j] < minNum:
        minNum = myList[j]
   
  return minNum
  
  
def find_min_num_in_list_2(myList):
  """ O(n) solution """ 
  minNum = sys.maxsize
  
  for idx in range(len(myList)):
    if minNum > myList[idx]:
      minNum = myList[idx]
   
  return minNum
   

print("See time duration of O(n^2) solution\n")
for listsize in range(1000, 10001, 1000):
  alist = [randrange(100000) for x in range(listsize)]
  start = time.time()
  print("Minimum value %d" % find_min_num_in_list_1(alist))
  end = time.time()
  print("size: %d time: %f" % (listsize, end-start))
  
print("\nSee time duration of O(n) solution\n")
for listsize in range(1000, 10001, 1000):
  alist = [randrange(100000) for x in range(listsize)]
  start = time.time()
  print("Minimum value %d" % find_min_num_in_list_2(alist))
  end = time.time()
  print("size: %d time: %f" % (listsize, end-start))   