import unittest

def longestCommonPrefix(strs):
    prefix = ""
    if len(strs) < 2:
        return strs[0]
    
    pointer = 0
    
    stack = strs[0]
    
    while stack:
        for i in range(len(strs)):
            word = strs[i]
            if pointer < len(word):
                letter = word[pointer]
                if letter == stack[pointer]:
                    # keep checking
                    if i == len(strs) - 1:
                        pointer +=1
                        prefix = prefix + letter
                else:
                    return prefix
            else:
                return prefix
    
    return prefix

class Test(unittest.TestCase):

    def test_small_prefix(self):
        actual = longestCommonPrefix(["flower","flow","flight"])
        expected = "fl"
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        actual = longestCommonPrefix([""])
        expected = ""
        self.assertEqual(actual, expected)

    def test_list_of_empty_strings(self):
        actual = longestCommonPrefix(["",""])
        expected = ""
        self.assertEqual(actual, expected)

    def test_list_of_short_strings(self):
        actual = longestCommonPrefix(["ab","a"])
        expected = "a"
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)