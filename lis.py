def binary_search(S, left, right, key):
    # Find smallest element that's >= key
    while left <= right:
        # find midpoint
        mid = left + (right - left) // 2
        # if element found move lower.
        if S[mid] >= key:
            right = mid - 1
        else:
            left = mid + 1
    # smallest element is left index.
    return left
        

def len_of_lis(A):
    """
    Computing the Longest Increasing Subsequence 
    O(nlogn) Time
    O(n)     Space
    """

    # error handling for empty list.
    if len(A) < 1:
        return 0
    
    # create subsequence list.
    subseq    = [0] * len(A)
    # set to initial sequence element.
    subseq[0] = A[0]
    # create sequence index for adding elements.
    seqIdx    = 0

    # iterate through the input sequence
    for i in range(1, len(A)):
        # Append to subsequence - basically new LIS.
        if A[i] > subseq[seqIdx]:
            seqIdx += 1
            subseq[seqIdx] = A[i]
        # Replace start of sequence 
        elif A[i] < subseq[0]:
            subseq[0] = A[i]
        else:
            # binary search through the subsequence
            # to find and replace the smallest element
            # with A[i] 
            idxToReplace = binary_search(subseq, 0, seqIdx, A[i])
            subseq[idxToReplace] = A[i]

    # Longest subsequence is the length of subseq
    return seqIdx + 1
    

"""
1
0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15
Output : 6
"""
#T = int(input("Number Test Cases = "))

#for idx in range(T):
A = [int(i) for i in input("Sequence ").split()]
print("Output: ", len_of_lis(A))
