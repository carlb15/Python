"""
63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
  
  1 = obstacle. 0 = free space


EX start == end 
  num ways = 1
[
  [0]
]

num ways =0 b.c. of the obstacle.
[
  [1]
]


BF: Go right and down 
  counting the steps as we go.
  
  if valid_square and not at end square:
    num_ways(row, col + 1) + num_ways(row - 1, col)
  
  Solution is O(2^n) Time
              O(n + m) Space
              
Base Case:
  if invalid_square (check ranges, visited, or grid[i][j] == 1)
    return 0
  if row == ROW and col == COL
    return 1
  if memo[row][col] == -1:
    return memo[row][col]
  
  memo[row][col] = num_ways(row - 1, col) + num_ways(row, col - 1)
  return memo[row][col]

O(n^2) Time O(n^2) Space
  
  
Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

  [ 1,  1,  1],
  [ 1, -1,  1],
  [ 1,  1,  2]

Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

def num_ways(grid):
  def num_ways_helper(grid, memo, row, col):
    def valid_square(row, col):
      if 0 <= row < len(grid) and \
         0 <= col < len(grid[0]) and \
         grid[row][col] == 0:
         return True
      return False
    
    # Base Cases
    if not valid_square(row, col):
      return 0
    # Reached end of matrix
    if row == 0 and col == 0:
      return 1
    
    # the value isn't computed then compute.
    if memo[row][col] == -1:
      memo[row][col] = num_ways_helper(grid, memo, row - 1, col) + \
                       num_ways_helper(grid, memo, row, col - 1)
    return memo[row][col]

  # error checking for valid grid
  
  memo = [[-1]*len(grid[0]) for _ in range(len(grid))]
  memo[0][0] = 1
  
  # recursively call starting at the bottom right of grid.
  num_ways_helper(grid, memo, len(grid) - 1, len(grid[0]) - 1)
  
  # return the number ways to get to bottom left.
  return memo[-1][-1]































