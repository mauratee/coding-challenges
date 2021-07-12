"""Reverse a string using recursion.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """
    # base case(degenerate):
    # if astring is empty:
        # return ''

    # tracking variable to hold reversed string
    # index variable to hold index

    # loop over string from end[-1]
        # add character to reversed string
        # return reversed string


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. !KROW DOOG\n")
