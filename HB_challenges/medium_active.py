"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""

    window = [0, 2021]
    # count = 0

    for author in bio_data:
        if author[1] >= window[0] and author[1] <= window[1]:
            count +=1
            window[0] = author[1]
        if author[2] <= window[1] and author[2] >= window[0]:
            window[1] = author[2]
    
    # print(window)

    return (window[0], window[1])



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")