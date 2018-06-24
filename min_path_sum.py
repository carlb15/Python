"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
  Input:
  [
    [1,3,1],
    [1,5,1],
    [4,2,1]
  ]

  Output: 7

Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
Base case:
  path[row][0] = path[row - 1][0]
  path[0][col] = path[0][col - 1]
  
  or 
  if invalid square then return impossible value +inf
  
  dp[i][j] = min(dp(i + 1, j), dp(i, j + 1)) + grid[i][j]
  
Recurrence:
  path[row][col] = min(path[row + 1][col], path[row][col + 1])

  start at (1,1)
  for row in range ROW
    for col in range COL
      path[row][col] = min(path[row-1][col], path[row][col -1])
                       + grid[row][col]

  O(m*n) Time 
  O(m*n) Space

  Example:
  Input:
  [
    Grid
    [1,3,1],
    [1,5,1],
    [4,2,1]
    
    A
    [1,4,5],
    [2,7,6],
    [6,8,7]
    1 -> 1 -> 1 -> 3 -> 1
    Reverse list 1 -> 3 -> 1 -> 1 -> 1
  ]

def minPathSum(self, grid):
  # check for valid grid
  
  path = [[0] * len(grid[0]) for _ in range(len(grid))]
  path = compute_first_row(path, 0)
  path = compute_first_col(path, 0)
  
  for row in range(1, len(grid)):
    for col in range(1, len(grid[0])):
      path[row][col] = min(path[row - 1][col], path[row][col - 1]) + grid[row][col]
  return path[-1][-1]
  
  
""" 1D array solution
    We just need the bottom array and the right element
    Create a dp array of row size, dp[-1][-1] = grid[-1][-1] 
    then move left and update dp[j]
    
    for each row in grid
      for j = len(grid) -2 to 0
        d[j] = grid[i][j] + min(dp[j], dp[j + 1])
    
    then dp[0] for final row is the answer
    
    O(m*n) Time and O(m) Space
    
    
    if input array is not read only then
    modify the array elements as we move through the 
    array to get O(1) space
    

"""


def minPathSum(self, grid):
  """
  :type grid: List[List[int]]
  :rtype: int
  
  Can move right or down
      path[0][0] = path[0][0]
      path[0][1] = path[0][0] + path[0][1]
  
  """
  def compute_first_col(grid, paths):
    for row in range(1, len(grid)):
      paths[row][0] = paths[row - 1][0] + grid[row][0]
    return paths
  
  def compute_first_row(grid, paths):
    for col in range(1, len(grid[0])):
      paths[0][col] = paths[0][col - 1] + grid[0][col]
    return paths
  
  if len(grid) == 0 or len(grid[0]) == 0:
    return 0
  
  # create the summation array
  paths = [[0] * len(grid[0]) for _ in range(len(grid))]
  # set your base case of (0,0)
  paths[0][0] = grid[0][0]
  # compute first row summation
  paths = compute_first_row(grid, paths)
  # compute first column summation
  paths = compute_first_col(grid, paths)        

  for row in range(1, len(grid)):
    for col in range(1, len(grid[0])):
      paths[row][col] = min(paths[row][col - 1], paths[row - 1][col]) + grid[row][col]   
              
  return paths[-1][-1]

  
def minPathSum(self, grid):
  """
  :type grid: List[List[int]]
  :rtype: int
  
  Can move right or down
      path[0][0] = path[0][0]
      path[0][1] = path[0][0] + path[0][1]
  
  """        
  if len(grid) == 0 or len(grid[0]) == 0:
      return 0
  
  rows = [0] * len(grid[0])
  
  for row in range(len(grid)):
      for col in range(len(grid[0])):
          if row == 0 and col == 0:
              rows[col] = grid[0][0]
          elif row == 0:
              rows[col] = grid[row][col] + rows[col - 1]
          elif col == 0:
              rows[col] = grid[row][col] + rows[col]
          else:
              rows[col] = min(rows[col], rows[col - 1]) \
                               + grid[row][col]
  return rows[-1]

  



