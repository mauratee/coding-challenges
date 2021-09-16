"""Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    if needle not in haystack:
        return None

    # x = 0

    # if needle == haystack[x]:
    #     return x
    # else:
    #     return x + recursive_index(needle, haystack)

    def _recursive_index(needle, haystack, start):

        if start == len(haystack):
            return None

        if haystack[start] == needle:
            return start
        
        return _recursive_index(needle, haystack, start +1)
    
    return _recursive_index(needle, haystack, 0)


# def recursive_index(needle, haystack):
#     """Given list (haystack), return index (0-based) of needle in the list.

#     Return None if needle is not in haystack.

#     Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
#     """

#     # START SOLUTION

#     def _recursive_index(needle, haystack, start_at):

#         # Check if not found (we've gone too far)
#         if start_at == len(haystack):
#             return None

#         # Have we found it?
#         if haystack[start_at] == needle:
#             return start_at

#         return _recursive_index(needle, haystack, start_at + 1)

#     return print_recursive_index(needle, haystack, 0)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO GO GO!\n")
