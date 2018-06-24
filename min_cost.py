from collections import namedtuple
import sys
Coord = namedtuple("Coord", ("x","y"))

def compute_min_cost(cost, d):
  def min_cost_helper(curr):
    def valid_coord(c):
      if -1 < c.x <= d.x and \
         -1 < c.y <= d.y:
        return True
      return False
  
    if not valid_coord(curr):
      return sys.maxsize
    if curr.x == 0 and curr.y == 0:
      return cost[0][0]

    if C[curr.x][curr.y] == -1:
      C[curr.x][curr.y] = cost[curr.x][curr.y] + \
                    min(min_cost_helper(Coord(curr.x - 1, curr.y)), \
                        min_cost_helper(Coord(curr.x, curr.y - 1)), \
                        min_cost_helper(Coord(curr.x - 1, curr.y - 1)))
    print(C)
    return C[curr.x][curr.y]
  
  C = [[-1] * len(cost[0]) for _ in range(len(cost))]

  return min_cost_helper(d)


# Driver program to test above functions
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(compute_min_cost(cost, Coord(2, 2)))