"""Number of Paths"""
"""
  Given N rows and M columns
  How many ways are there to get from bottom left to top right
  going upwards or rightwards?
  
  Base Case:
    if invalid square or square is visited:
      return 0
    if end square 
      return 1
  General Formula:
    update boolean matrix with row,col
    return SUM( num_ways_helper(row - 1, col)
                num_ways_helper(row, col + 1) )
  
  Boolean matrix size N rows and M columns 
  - know where we have already visited
  O(N*M) Time, O(N*M) Space
"""

def num_ways_helper(grid, visited, row, col):
  def valid_square(row, col):
    if 0 <= row < len(grid) and \
       0 <= col < len(grid[0]) and \
       not visited[row][col]:
       return True
    return False

  if row == 0 and col == len(grid[0]) - 1:
    return 1
  if not valid_square(row, col):
    return 0

  visited[row][col] = True
  return num_ways_helper(grid, visited, row, col + 1) +
         num_ways_helper(grid, visited, row - 1, col)


def num_ways(grid):
  # error checking on grid
  if len(grid) < 1 or len(grid[0]) < 1:
    return -1
  
  visited = [[False] * M for _ in range(N)]
  
  numWays = num_ways_helper(grid, visited, N - 1, 0)
  return numWays
  
  
# iterative solution
def num_ways(grid):
  paths = [[1] * len(grid[0]) for _ in range(len(grid))]
  
  for x in range(1, len(grid)):
    for y in range(1, len(grid[0])):
      paths[x][y] = paths[x - 1][y] + paths[x][y - 1]
  return paths[0][-1]
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
