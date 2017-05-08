"""Linear Search."""


def linear_search(myList, item):
    """Linear search through a list to find an item."""
    """
    Args:
        myList: List to search through.
        item: Item to find.

    Return: Return True if item is found and False otherwise.
    """
    position = 0
    found = False
    while position < len(myList) and not found:
        if myList[position] == item:
            found = True
        position += 1

    if not found:
        myList.append(item)

    return found, position


if __name__ == "__main__":
    myList = [1, 2, 3, 4]
    print(linear_search(myList, 1))
    print(linear_search(myList, 10))
    print(linear_search(myList, 3))
    print(linear_search(myList, 2))
    print(linear_search(myList, -1))
    print(linear_search(myList, -1))
