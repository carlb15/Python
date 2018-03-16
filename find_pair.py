"""Find Pair with given Sum in the Array."""

def findPair(arr, sum):
  d = dict()

  for idx, num in enumerate(arr):
    d[num] = idx

  for num1 in arr:
    num2 = sum - num1
    if num2 in d and d[num1] != d[num2]:
      pair = (d[num1], d[num2])
      print(pair)
  return False
  

if __name__=="__main__":
  arr = [8, 7, 2, 5, 3, 1]
  sum = 12
  print("Index 1, 3")
  findPair(arr, sum)
  sum = 10
  print("Indices 0, 2 and Indices 1, 4")
  findPair(arr, sum)