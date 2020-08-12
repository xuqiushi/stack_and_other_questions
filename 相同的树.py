# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from 打家劫舍3 import TreeNode, Tree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            if p == q:
                return True
            else:
                return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    test_1 = [1, 2]
    test_2 = [1, None, 2]
    test_tree_1 = Tree(test_1)
    test_tree_2 = Tree(test_2)
    test = Solution().isSameTree(test_tree_1.root, test_tree_2.root)
    print(test)
