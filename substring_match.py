def substring_match(T, S):
  """
  Simple substring matching. 
  O(|S| * |T - S|) Time
  O(1) Space
  """
  return any([T[idx:idx+len(S)] == S for idx in range(len(T) - len(S) + 1)])
"""
  for idx in range(len(T) - len(S) + 1):
    print(T[idx:idx + len(S)], S)
    if T[idx:idx + len(S)] == S:
      return True
  return False
"""
  
  
if __name__=="__main__":
  print("Expect True ", substring_match('hello world', 'hello'))
  print("Expect True ", substring_match('hello world', 'world'))
  print("Expect True ", substring_match('hello world', 'wor'))
  print("Expect False ", substring_match('hello world', 'blue'))
  print("Expect False ",substring_match('hello world', 'word'))

