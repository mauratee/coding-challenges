"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""
   
    if not matrix:
        return None

    zeroed_matrix = ([])
    zero_idx = ''

    for row in matrix:
        for idx, num in enumerate(row):
            if num == 0:
                zero_idx = idx
                if idx > 0 and idx < len(row):
                    idx = idx -= 1
                    row[idx] = 0
                    break
                    # zeroed_matrix.append(row)
                continue
                # for list in matrix
                    # for idx, num in enumerate(list)
                        # if idx == zero_idx:
                            # num == 0
        
        zeroed_matrix.append(row)

    return zeroed_matrix

# zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
