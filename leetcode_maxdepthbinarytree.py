import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):

        return (
            f"<TreeNode object val: {self.val}, left: {self.left}, right: {self.right}>"
        )


def maxDepth(root):

    print(root)




class Test(unittest.TestCase):

    def test_not_deep(self):
        actual = maxDepth(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), 
        TreeNode(7, None, None))))
        expected = 3
        self.assertEqual(actual, expected)

    # def test_empty_string(self):
    #     actual = longestCommonPrefix([""])
    #     expected = ""
    #     self.assertEqual(actual, expected)

    # def test_list_of_empty_strings(self):
    #     actual = longestCommonPrefix(["",""])
    #     expected = ""
    #     self.assertEqual(actual, expected)

    # def test_list_of_short_strings(self):
    #     actual = longestCommonPrefix(["ab","a"])
    #     expected = "a"
    #     self.assertEqual(actual, expected)


unittest.main(verbosity=2)