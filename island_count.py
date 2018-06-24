def numIslands(grid):
  """
  :type grid: List[List[str]]
  :rtype: int
  """
  
  def valid_sq(grid, row, col, visited):
    if  0 <= row < len(grid) and \
        0 <= col < len(grid[0]) and \
        grid[row][col] == '1' and \
        (row,col) not in visited:
        return True
    return False


  def get_adjacent_squares(grid, row, col, visited):
    adjacent = []
    if valid_sq(grid, row - 1, col, visited):
      adjacent.append((row - 1, col))
      visited.add((row - 1, col))
    if valid_sq(grid, row + 1, col, visited):
      adjacent.append((row + 1, col))
      visited.add((row + 1, col))
    if valid_sq(grid, row, col - 1, visited):
      adjacent.append((row, col - 1))
      visited.add((row, col - 1))
    if valid_sq(grid, row, col + 1, visited):
      adjacent.append((row, col + 1))
      visited.add((row, col + 1))

    return adjacent


  def bfs(grid, row, col, visited):
    if not valid_sq(grid, row, col, visited):
      return

    q = [(row, col)]

    while q:
      sq = q.pop(0)

      if valid_sq(grid, sq[0], sq[1], visited):
        visited.add((row,col))
        q.extend(get_adjacent_squares(grid, sq[0], sq[1], visited))

  visited = set()
  island_count = 0

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if valid_sq(grid, row, col, visited):
        print('start of bfs ', ' row ', row, ' col ', col)
        bfs(grid, row, col, visited)
        island_count += 1
  return island_count

if __name__=="__main__":
  grid = [["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]]

  print(numIslands(grid))