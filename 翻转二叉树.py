from collections import deque

from achievement import TreeNode, Tree


class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        root.display()
        cache = deque()
        cache.append(root)
        while cache:
            current_node = cache.pop()
            current_node.left, current_node.right = current_node.right, current_node.left
            if current_node.left:
                cache.append(current_node.left)
            if current_node.right:
                cache.append(current_node.right)
        return root


if __name__ == "__main__":
    test_list = [4, 2, 7, 1, 3, 6, 9]
    test_root = Tree(test_list).root
    Solution().invert_tree(test_root).display()
