"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    carrots_eaten = 0

    if nrows % 2 == 0:
        print(nrows)
        middle_rows = (nrows // 2, (nrows // 2) - 1 )
        print(middle_rows)
    else:
        print(nrows)
        middle_row = (nrows // 2)
        print(middle_row)

    if ncols % 2 == 0:
        print(ncols)
        middle_cols = (ncols // 2, (ncols // 2) - 1 )
        print(middle_cols)
    else:
        print(ncols)
        middle_col = (ncols // 2)
        print(middle_col)

    if middle_row and middle_col:
        start = garden[middle_row][middle_col]
        print(start)
        carrots_eaten += start
        garden[middle_row][middle_col] = 0
        # print(garden)
    else:
        max_start = 0
        if middle_rows:
            for row in middle_rows:





    # return carrots_eaten

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")
