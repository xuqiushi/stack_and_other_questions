# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from typing import List

from achievement import TreeNode, Tree


class Solution:
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result = []
        cache_que = deque()
        current_que = deque()
        cache_que.append((root, 0))
        while cache_que:
            current_node = cache_que.pop()
            while current_que and current_que[-1][1] >= current_node[1]:
                current_que.pop()
            current_que.append(current_node)
            if not current_node[0].left and not current_node[0].right:
                result.append(list(current_que))

            if current_node[0].right:
                cache_que.append((current_node[0].right, current_node[1] + 1))
            if current_node[0].left:
                cache_que.append((current_node[0].left, current_node[1] + 1))
        return [
            "->".join([str(node[0].val) for node in sub_result])
            for sub_result in result
        ]


if __name__ == "__main__":
    test_nodes = [1, 2, 3, 5, 6]
    test_root = Tree(test_nodes).root
    print(Solution().binary_tree_paths(test_root))
