"""Validate tic tac toe board"""

def has_won_hash_table(board):
  """Determine winner with hash table
     Good option for many queries.
     Assume: blank space = 0, x = 1, o = 2
     3^9 or 20,000 possible board combinations for a 3x3 board.
     Create a hash table with all combinations of the board and
     then query for the given board.
     key = all possibly boards, value = winner
     Need to recompute hash table for new boards.
  """
  def convertBoardToInt(board):
    factor = 1
    mySum = 1
    for row in range(len(board)):
      for col in range(len(board[0])):
        val = 0
        if board[row][col] == 'x':
          val = 1
        elif board[row][col] == 'o':
          val = 2
        mySum += val * factor
        factor *= 3
    return mySum

  winnerHashTable = dict()
  key = convertBoardToInt(board)
  winnerHashTable[key] = 'x'
  return winnerHashTable[key]


def has_won_recursive(board):
  """Validate NxN board recursively."""
  def find(row, col, move, count, x_or_o):
    def valid_sq():
      if -1 < row < len(board)   and \
         -1 < col < len(board)   and \
         -1 < count <= len(board)and \
         x_or_o == board[row][col]:
         return True
      return False

    if not valid_sq():
      return False

    count += 1

    if count == len(board):
      return True

    if move == "down":
      print('down')
      return find(row + 1, col, 'down', count, x_or_o)
    elif move == 'diag':
      print('diag')
      return find(row + 1, col + 1, 'diag', count, x_or_o)
    elif move == 'revdiag':
      print('revdiag')
      return find(row - 1, col + 1, 'revdiag', count, x_or_o)
    elif move == 'right':
      print('right')
      return find(row, col + 1, 'down', count, x_or_o)

    return (find(row + 1, col, 'down', count, x_or_o) or \
            find(row + 1, col + 1, 'diag', count, x_or_o) or \
            find(row - 1, col + 1, 'revdiag', count, x_or_o) or \
            find(row, col + 1, 'right', count, x_or_o))

  def check_winner(player):
    for row in range(len(board)):
      if find(row, 0, 'any', 0, player):
        return True
    for col in range(len(board)):
      if find(0, col, 'any', 0, player):
        return True
    return False
    
  x_wins = check_winner('x')
  if not x_wins:
    return 'o wins!' if check_winner('o') else 'no one wins'
  return 'x wins!'


def has_won_with_set(board):
  # check rows
  for row in range(len(board)):
    rowValues = set([board[row][col] for col in range(len(board[0]))])
    if len(rowValues) == 1 and board[row][0] != 0:
      return board[row][0]
  
  # check columns
  for col in range(len(board)):
    colValues = set([board[row][col] for row in range(len(board))])
    if len(colValues) == 1 and board[0][col] != 0:
      return board[0][col]
  
  # check diagonals
  diag1 = set([board[idx][idx] for idx in range(len(board))])
  diag2 = set([board[idx][len(board) - 1 - idx] for idx in range(len(board))])
  midIdx = len(board) // 2
  if (len(diag1) == 1 or len(diag2) == 1) and board[midIdx][midIdx] != 0:
    return board[midIdx][midIdx]
  return 0

if __name__=="__main__":
  board = [[2, 2, 0],
           [2, 1, 0],
           [2, 1, 1]]
  print('Expect: 2, Result:', has_won_with_set(board), '\n')

  board = [[1, 2, 0],
           [2, 1, 0],
           [2, 1, 1]]

  print('Expect: 1, Result:', has_won_with_set(board), '\n')

  board = [[0, 1, 0],
           [2, 1, 0],
           [2, 1, 1]]

  print('Expect: 1, Result:', has_won_with_set(board), '\n')

  board = [[1, 2, 0],
           [2, 1, 0],
           [2, 1, 2]]

  print('Expect: 0, Result:', has_won_with_set(board), '\n')

  board = [[1, 2, 0],
           [2, 1, 0],
           [2, 1, 0]]

  print('Expect: 0, Result:', has_won_with_set(board), '\n')
  
  board = [[1, 2, 0, 1, 0, 0, 2],
           [2, 1, 2, 1, 0, 2, 0],
           [0, 2, 0, 0, 2, 0, 0],
           [1, 0, 0, 2, 0, 0, 1],
           [2, 2, 2, 1, 0, 2, 0],
           [1, 2, 2, 1, 2, 0, 1],
           [2, 1, 0, 0, 2, 2, 0]]

  print('Expect: 2, Result:', has_won_with_set(board), '\n')
"""
  board = [['x','x','x'],
           ['x', '', 'o'],
           ['o', '', 'o']]
  print('Expect: x, Result:', has_won_hash_table(board), '\n')
  board = [['x','x','x'],
           ['x', '', 'o'],
           ['o', '', 'o']]
  print('Expect: x, Result:', has_won_recursive(board), '\n')

  board = [['x','x','o'],
           ['', 'x', 'o'],
           ['o', '', 'x']]
  print('Expect: x, Result:', has_won_recursive(board), '\n')
  
  board = [['x', 'x', 'o'],
           [' ', 'o', ' '],
           ['o', 'x', 'x']]

  print('Expect: o, Result:', has_won_recursive(board), '\n')

  board = [['x', 'x', 'o'],
           [' ', 'x', 'o'],
           ['o', ' ', 'o']]

  print('Expect: o, Result:', has_won_recursive(board), '\n')

  board =[['x', 'x', 'o', 'x'],
          [' ', 'o', 'o', 'x'],
          ['o', ' ', 'x', 'x'],
          ['o', 'o', 'x', 'x']]
  print('Expect: x, Result:', has_won_recursive(board), '\n')
"""