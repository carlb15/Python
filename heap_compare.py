"""Determine whether the kth smallest element in heap
  is greater than or equal to x. Algorithm should run
  in O(k) worst-case, independent of size of heap.
"""

import heapq

def pq_child(n):
  return 2 * n


def heap_compare(pq, pq_idx, count, x):
  # if the kth index is reached or end of the
  # priority queue then terminate.
  if count <= 0 or pq_idx > len(pq):
    return count

  # keep going while priority queue elements are smaller than x.
  if pq[pq_idx] < x:
    count = heap_compare(pq, pq_child(pq_idx), count - 1, x)
    count = heap_compare(pq, pq_child(pq_idx) + 1, count, x)

  return count


if __name__=="__main__":
  pq = [4, 1, 2, 63, 6, 45, 43]
  heapq.heapify(pq)
  print(pq)
  for i in range(len(pq)):
    print('idx ', i)
    print('result ', heap_compare(pq, 1, 4, i))
  
  
  