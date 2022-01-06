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
    best_depth = None
    current_depth = 0

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
        depth_so_far += 1
        print("best depth is ", best_depth)
        print("depth so far is ", depth_so_far)

        # if current_node.left:
        #     if current_node.left not in seen:
        #         to_visit.append(current_node.left)
        #         if current_node != root:
        #             seen.add(current_node)
            
        # if current_node.right:
        #     if current_node.left not in seen:
        #         to_visit.append(current_node.right)
        #         if current_node != root:
        #             seen.add(current_node)

        if current_node.left or current_node.right:
            next = current_node.left or current_node.right
            if next not in seen:
                to_visit.append(next)
                if current_node != root:
                    seen.add(current_node)
        
        #if not current_node.left and not current_node.right
        if current_node.right is None and current_node.left is None:
            if depth_so_far > best_depth:
                current_depth = best_depth
                best_depth = depth_so_far
            depth_so_far = current_depth
            to_visit.append(root)
            print("depth so far = ", depth_so_far)
    
    return best_depth




class Test(unittest.TestCase):

    # [3,9,20,null,null,15,7]
    def test_not_deep(self):
        actual = maxDepth(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None))))
        expected = 3
        self.assertEqual(actual, expected)

    # [1,2,3,4,5]

    #     1
    #    /  \
    #   2    3
    #  / \
    # 4   5

    def test_uneven(self):
        actual = maxDepth(TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None)))
        expected = 3
        self.assertEqual(actual, expected)
    
    # [1,2]
    def test_so_small(self):
        actual = maxDepth(TreeNode(1, TreeNode(2, None, None), None))
        expected = 2
        self.assertEqual(actual, expected)

    # [1,null,2]
    def test_two_nodes(self):
        actual = maxDepth(TreeNode(1, None, TreeNode(2, None, None)))
        expected = 2
        self.assertEqual(actual, expected)

    # [1,2,3,4,null,null,5]
    def test_balanced(self):
        actual = maxDepth(TreeNode(1, TreeNode(2, TreeNode(4, None, None), None), TreeNode(3, None, TreeNode(5, None, None))))
        expected = 3
        self.assertEqual(actual, expected)

    # [7,-7,8,null,null,-3,6,null,9,null,null,null,-5]
    
    #         7
    #        / \
    #      -7   8
    #          / \
    #         -3  6
    #              \
    #               9
    #                \
    #                -5     

    def test_negative(self):
        actual = maxDepth(TreeNode(7, TreeNode(-7, None, None), TreeNode(8, TreeNode(-3, None, TreeNode(9, None, TreeNode(-5, None, None))), TreeNode(6, None, None))))
        expected = 5
        self.assertEqual(actual, expected)




unittest.main(verbosity=2)