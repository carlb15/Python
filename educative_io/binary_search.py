"""Binary Search Code Rust."""

def binary_search_helper(A, low, high, key):
    """Binary Search Helper."""
    """
        Binary search helper for recursively searching through an array.

        A: Sorted Array
        low: smallest index in array
        high: highest index in array
        key: value to find
    """

    if low > high:
        return -1

    mid = low + ((high - low) // 2)
    if key == A[mid]:
        return mid
    elif A[mid] > key:
        return binary_search_helper(A, low, mid - 1, key)
    else:
        return binary_search_helper(A, mid + 1, high, key)

def binary_search(A, key):
    """Binary Search Algorithm."""
    """
        log(n) search through an array.

        A: sorted array to search
        key: key to find

        return: -1 if key is not found or the index of the key
    """
    return binary_search_helper(A, 0, len(A) - 1, key)


if __name__ == "__main__":
    assert(binary_search([1, 2, 3, 4], 3) == 2)
    assert(binary_search([1, 2, 3, 4], 5) == -1)
