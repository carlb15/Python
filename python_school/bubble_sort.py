"""Bubble Sort."""


def bubble_sort(myList):
    """Bubble sort implementation."""
    """
    Bubble sort has worst/average/best run-time of O(n**2). Not a practical
    sorting algorithm.

    Args:
        myList: Unsorted list of numbers

    Returns: Sorted list of numbers.
    """


if __name__ == "__main__":
    myList = [12, 5, 7, 18, 11, 6, 12, 4, 17, 1]
    sortedList = [1, 4, 5, 6, 7, 11, 12, 12, 17, 18]
    assert(bubble_sort(myList) == sortedList)
