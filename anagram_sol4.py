def anagram_solution_4(s1, s2):
  c1 = [0] * 26
  c2 = [0] * 26
  
  for i in range(len(s1)):
    # find the numeric value for the char
    pos = ord(s1[i]) - ord('a')
    # increment the character count
    c1[pos] = c1[pos] + 1
  
  for i in range(len(s2)):
    # find the numeric rep. of the char
    pos = ord(s2[i]) - ord('a')
    # increment the char counter
    c2[pos] = c2[pos] + 1
    
  j = 0
  stillOk = True
  while j < 26 and stillOk:
    if c1[j] == c2[j]:
      j = j + 1
    else:
      stillOk = False
  
  return stillOk
  
print(anagram_solution_4('apple', 'pleap'))
print(anagram_solution_4('apple', 'plea'))