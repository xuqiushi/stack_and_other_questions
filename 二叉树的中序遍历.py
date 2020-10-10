from collections import deque
from typing import List

from achievement import TreeNode, Tree


class Solution:
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cache = deque([root])
        select_node = {None}
        result = []
        while cache:
            current_node = cache.pop()
            if current_node.left is None or current_node.left in select_node:
                result.append(current_node.val)
                select_node.add(current_node)
                if current_node.right and not current_node.left:
                    cache.append(current_node.right)
            else:
                if current_node.right:
                    cache.append(current_node.right)
                cache.append(current_node)
                cache.append(current_node.left)
        return result


if __name__ == "__main__":
    test_nums = [3, 1, 2]
    test_root = Tree(test_nums).root
    print(Solution().inorder_traversal(test_root))
