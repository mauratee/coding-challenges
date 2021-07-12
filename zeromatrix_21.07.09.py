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
    zero_idx_row = None
    zero_idx_matrix = None

    for idx, row in enumerate(matrix):
        for jdx, num in enumerate(row):
            if num == 0:
                zero_idx_row = jdx
                zero_idx_matrix = idx
                for x in range(len(row)):
                        row[x] = 0
                break
                # for list in matrix
                    # for idx, num in enumerate(list)
                        # if idx == zero_idx:
                            # num == 0
        
        zeroed_matrix.append(row)

    if zero_idx_row:
        for idx, row in enumerate(zeroed_matrix):
            if idx == zero_idx_matrix:
                continue
            for jdx, num in enumerate(row):
                if jdx == zero_idx_row:
                    row[jdx] = 0

    # print(zero_idx_row)
    # print(zero_idx_matrix)


    return zeroed_matrix

zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
