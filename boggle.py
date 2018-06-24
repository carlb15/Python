dictionary = {"GEEKS", "FOR", "QUIZ", "GO"}
N, M = 3, 3
board = [['G','I','Z'],
		['U','E','K'],
		['Q','S','E']]

class Graph:
  class Vertex:
    def __int__(self, v):
      self.val = v
      self.adj = []

def findWords(board):
  def search(node, word, visited):
    if node not in visited:
      visited.append(node)
      word.append(node.val)      
      for adjNode in node.adj:
      	search(node, word, visited)    
    if word not in dictionary:
      word.pop()
  
  result = []
  g = creategraph(board)
  
  for u in g.vertices():
    visited = []
    visited.append(u)
    word = ""
    for adj in u.adj:      
      search(adj, word, visited)
      if word in dictionary:
      	result.append(word)
  return result
  
  
      