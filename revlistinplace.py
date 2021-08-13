"""Reverse list in place.

You cannot do this with reversed(), .reverse(), or list slice
assignment!

    >>> lst = []
    >>> rev_list_in_place(lst)
    []

    >>> lst = ['a']
    >>> rev_list_in_place(lst)
    ['a']

    >>> lst = [1, 2, 3]
    >>> rev_list_in_place(lst)
    [3, 2, 1]

    >>> lst = [1, 2, 3, 4]
    >>> rev_list_in_place(lst)
    [4, 3, 2, 1]
"""


def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """
    reversed_lst = []

    if not lst:
        return reversed_lst

    # if len(lst) < 2:
    #     return lst

    i = -1
    for j in range(len(lst)):
        reversed_lst.append(lst[i])
        # print(reversed_lst)
        i -= 1
    
    return reversed_lst

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE THE BEST!\n")
