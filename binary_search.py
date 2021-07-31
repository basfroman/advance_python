
def bin_search(n: int, lst: list) -> int:
    """Binary search index of element in list.
    Note: list should be sorted.

    Args:
        n: required number
        lst: sorted list on numbers.
    Returns:
        index of x in list is present or -1
    """
    if lst[0] > n or lst[-1] < n:
        return -1

    start, stop = 0, len(lst) - 1
    while True:
        ind = (stop - start) // 2 + start
        if n == lst[ind]:
            return ind
        elif start == stop:
            return -1
        elif n < lst[ind]:
            stop = ind
        elif n > lst[ind]:
            start = ind + 1


if __name__ == '__main__':
    list_of_numbers = [1, 2, 4, 11, 44]
    print(bin_search(0, list_of_numbers))
    print(bin_search(2, list_of_numbers))
    print(bin_search(3, list_of_numbers))
    print(bin_search(44, list_of_numbers))
    print(bin_search(999, list_of_numbers))

    # lst = [1, 2, 5, 6, 7, 10, 10, 11, 12, 21, 22, 33, 34, 67, 98]
