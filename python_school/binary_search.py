"""Binary Search in an ordered list."""


def binary_search(myList, item):
    """Binary search through an ordered list."""
    """
    Args:
        myList: ordered list to search
        item: item to find

    Returns: True if item is found and False if not.
    Example:
    """
    leftIdx = 0
    rightIdx = len(myList) - 1
    found = False
    numOfSearches = 0

    while leftIdx <= rightIdx and not found:
        middleIdx = (leftIdx + rightIdx) // 2
        if myList[middleIdx] == item:
            found = True
        elif myList[middleIdx] > item:
            rightIdx = middleIdx - 1
        else:
            leftIdx = middleIdx + 1
        numOfSearches += 1

    print("Number of searches required %d" % numOfSearches)
    return found


if __name__ == "__main__":
    myList = [2]
    assert(binary_search(myList, 2))
    myList = [2, 3]
    assert(binary_search(myList, 3))
    assert(not binary_search(myList, 4))
    assert(not binary_search([], 3))
    myList = [2, 5, 7, 12, 14, 21, 28, 31, 36]
    assert(binary_search(myList, 2))
    assert(binary_search(myList, 7))
    assert(binary_search(myList, 14))
    assert(binary_search(myList, 31))
    assert(binary_search(myList, 36))
    assert(not binary_search(myList, -2))
    assert(not binary_search(myList, 16))
    assert(not binary_search(myList, 100))
