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

    best_depth = None

    if not root:
        return 0
    else:
        best_depth = 1

    to_visit = [root]
    seen = set()
    
    # find deepest path and track versus other paths
    # depth first search
    
    depth_so_far = 0
    
    while to_visit:
        current_node = to_visit.pop()
        print("current_node is ", current_node)

        if current_node.left:
            to_visit.append(current_node.left)
            depth_so_far += 1
            
        if current_node.right:
            to_visit.append(current_node.right)
            depth_so_far += 1
        
        else:
            print("depth so far = ", depth_so_far)
            if depth_so_far > best_depth:
                best_depth = depth_so_far
            depth_so_far = 0
    
    return best_depth




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