import unittest

def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    # call recursed and start at 0
    # function check if haystack[start] == needle
    # if not, keep calling function
    # if does match, return whatever index we're at

    # underscore function name means only call this in local namespace
    def _recursed(needle, haystack, start):

        if start < len(haystack):
            if haystack[start] == needle:
                return start
            return recursed(needle, haystack, start + 1)
    
    return recursed(needle, haystack, 0)

    # runtime of simple recursive functions is O(n)

class Test(unittest.TestCase):
    def test_needle_in_haystack(self):
        result = recursive_index(1, [3,4,1])
        expect = 2
        self.assertEqual(result, expect)

    def test_needle_not_in_haystack(self):
        result = recursive_index(2, [3,4,1])
        expect = None
        self.assertEqual(result, expect)

unittest.main(verbosity=2)
