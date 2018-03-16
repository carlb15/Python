def subsets(nums):
  result = [[]]
  nums.sort()
  for anum in nums:
      for i in range(len(result)):
          print("Current subsets %s" % result)
          result.append(result[i] + [anum])
  print("Solution is %s %d" % (result, len(result)))
  return result
  
  
if __name__=="__main__":
  subsets([1,2])
  subsets([1,2,3])
  subsets([1,2,3,4])