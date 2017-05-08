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
    return found


if __name__ == "__main__":
    assert(linear_search([1, 2, 3, 4], 1))
    assert(not linear_search([1, 2, 3, 4], 10))
    shopping = ['apples', 'bananas', 'chocolate', 'pasta']
    item = input('What item do you want to find? ')
    if linear_search(shopping, item):
        print('Item %s is found.' % item)
    else:
        print('Item %s is not found.' % item)
