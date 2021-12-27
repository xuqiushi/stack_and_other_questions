# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from achievement import TreeNode, Tree


class Solution:
    def walk_tree(self, node):
        if node.left:
            (
                left_balanced,
                left_child_left_depth,
                left_child_right_depth,
            ) = self.walk_tree(node.left)
            left_depth = max(left_child_left_depth, left_child_right_depth) + 1
        else:
            left_balanced = True
            left_depth = 1
        if node.right:
            (
                right_balanced,
                right_child_left_depth,
                right_child_right_depth,
            ) = self.walk_tree(node.right)
            right_depth = max(right_child_left_depth, right_child_right_depth) + 1
        else:
            right_balanced = True
            right_depth = 1
        balanced = (
            False
            if not (left_balanced and right_balanced)
            else abs(left_depth - right_depth) <= 1
        )
        return balanced, left_depth, right_depth

    def is_balanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        balanced, left_depth, right_depth = self.walk_tree(root)
        return balanced


if __name__ == "__main__":
    test_node_values = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
    test_tree = Tree(test_node_values)
    print(Solution().is_balanced(test_tree.root))
