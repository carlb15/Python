"""
matrix

start - lower left corner
end - lower right corner

     _____________
    |_|_|_|_|_|_|_|
    |_|Y|_|_|_|_|_|
    |S|Y|_|_|_|_|E|
       X
There are three ways you go move. You can go from “here” to either right/up, right, right/down
     _____________________
    |________|_Right/Up__|
    |__Here__|__Right____|
    |________|_Right/Down|

matrix[i+1][j+1] (right / up)
matrix[i+0][j+1] (right)
matrix[i-1][j+1] (right / down)

Warning: 
1. You can’t go directly up
2. You can’t go directly down
3. You can’t go to the left

     ___________________________
    |__NO___|___NO__|_Right/Up__|
    |__NO___|__Here__|__Right___|
    |__NO___|___NO__|_Right/Down|

Question: how many ways are there, to move from start to end
"""
def numWaysUtil(grid, visited, curr_row, curr_col):
  def valid_sq(curr_row, curr_col):
    if 0 <= curr_row < len(grid) and \
       0 <= curr_col < len(grid[0]) and \
       not visited[curr_row][curr_col]:
       return True
    return False

  if curr_row == len(grid)-1 and curr_col == len(grid[0])-1:
    return 1
  elif valid_sq(curr_row, curr_col):
    visited[curr_row][curr_col] = True
    return numWaysUtil(grid, visited, curr_row - 1, curr_col + 1) + \
      numWaysUtil(grid, visited, curr_row, curr_col + 1) + \
      numWaysUtil(grid, visited, curr_row + 1, curr_col + 1)
  return 0

def num_ways(grid):
  # error checking
  if len(grid) == 0 or len(grid[0]) == 0:
    return 0

  start_row = len(grid) - 1
  start_col = 0
  visited = [[False] * len(grid[0]) for _ in range(len(grid))]

  return numWaysUtil(grid, visited, start_row, start_col)

if __name__=="__main__":
  grid = [[0] * 3 for _ in range(4)]
  print("Given grid. Can move right/up, right, right/down")
  for row in range(len(grid)):
    print(grid[row][:])
  print("Number of ways to end ", num_ways(grid))
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  




