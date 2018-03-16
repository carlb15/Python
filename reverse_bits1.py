from reverse_bits import swap_bits

"""Pre-computed look-up for reversing a number."""
BIT_MASK  = 0xFFFF
MASK_SIZE = 16

def reverse_x(x, n):
  i, j = 0, n
  while i < j:
      x = swap_bits(x, i, j)
      i += 1
      j -= 1
  return x

PRECOMP_TABLE = [reverse_x(i, MASK_SIZE - 1) for i in range(1 << MASK_SIZE)]

def reverse_bits(x):
  """
  Reverse 8-bit integers.
  O(n/L) time complexity where n is the word size
  and L is the look-up table key size. Algorithm 
  handles repeated queries better than previous approach.
  """
  """
  EX: 11001101    -> [11]  [00]   [11]   [01] -> [10] | [11] | [00] | [11] -> 10110011
      Input bits  -> MSB,  MSB-1  LSB+1  LSB  -> Combine reversed sub bits -> Output bits.
  """
  return( # Compute MSB
          # Retrieve the LSB, shift to MSB 
          PRECOMP_TABLE[x & BIT_MASK] << (3 * MASK_SIZE)
          # Compute MSB - 1
          # 1. Retrieve LSB + 1
          # 2. AND with BIT_MASK to isolate
          # 3. Left shift by 2 * mask size to move into the MSB - 1 place.
        | PRECOMP_TABLE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE)
          # Compute LSB + 1
          # 1. Right shift 2 * mask size to get MSB - 1
          # 2. Isolate with bit mask.
          # 3. Shift and set into the LSB + 1 position.
        | PRECOMP_TABLE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE
          # Compute LSB
          # Shift to MSB position
          # Isolate with bit mask and set by ORing to the result bits.
        | PRECOMP_TABLE[(x >> (3 * MASK_SIZE)) & BIT_MASK] )

if __name__=="__main__":
  """Test reversing the int."""
  for i in range(1000):
    assert(reverse_bits(i) == reverse_x(i, 63))