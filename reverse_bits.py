def swap_bits(x, i, j):
  """
  Swap the ith and jth indices in 'x'.
  """
  # Extract the i and j indices to see if they differ.
  if (x >> i) & 1 != (x >> j) & 1:
    # Retrieve the bits to flip by shifting to
    # the ith and jth indices. Create a bit mask.
    bit_mask = (1 << i) | (1 << j)
    # Flip bits. 
    #   x ^ 1 = 0 when x = 1. 
    #   x ^ 1 = 0 when x = 0.
    x ^= bit_mask
  return x

def reverse_bits(x):
  """
  Reverse the bits in 'x'.
  """
  leftIdx = 0
  rightIdx = x.bit_length() - 1
  while leftIdx < rightIdx:
    x = swap_bits(x, leftIdx, rightIdx)
    leftIdx += 1
    rightIdx -= 1
  return x

if __name__=="__main__":
  """Test reversing the int."""
  print("147 reversed is 201")
  assert(reverse_bits(147) == 201)
  print("4 reversed is 1")
  assert(reverse_bits(4) == 1)
  print("6 reversed is 3")
  assert(reverse_bits(6) == 3)
  print("120 reversed is 15")
  assert(reverse_bits(120) == 15)