def sort_anagrams_1(strs):
  """
  :type strs List[str]
  :rtype List[List[str]]
  """
  map = {}
  for v in strs:
    target = ''.join(sorted(v))
    print(target)
    if target not in map:
      map[target] = []
    map[target].append(v)
    print('building map ', map[target])
  
  result = []
  for value in map.values():
    print('anagrams ', value)
    result += [sorted(value)]

  return result
  



def sort_anagrams(myList):
  def convert_strs_to_hashes(myList):
    d = dict()
    
    for anagram in myList:
      h = sum([ord(i) for i in anagram])
      if h not in d:
        d[h] = []
      d[h].append(anagram)

    return d

  if not myList or len(myList) < 2:
    return 0 if not myList else 1
  
  d = convert_strs_to_hashes(myList)
  
  outputList = []
  for key, values in d.items():
    outputList.extend(values)
  return outputList


if __name__=="__main__":
  anagrams = ["acme", "acre", "came", "care", "mace", "race"]
  print("Before ", anagrams)
  print("After ", sort_anagrams(anagrams))
  anagrams = ["acme", "acre", "came", "care", "mace", "race"]
  print("Before ", anagrams)
  print("After ", sort_anagrams_1(anagrams))

