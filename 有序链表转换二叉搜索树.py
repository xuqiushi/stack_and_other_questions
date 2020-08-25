# Definition for singly-linked list.
from achievement import BalancedTreeGetter, ListNode


class Solution(BalancedTreeGetter):
    pass


if __name__ == "__main__":
    test_data = [-10, -3, 0, 5, 9]
    test_chain = ListNode.generate_list_node(test_data)
    tree_root = Solution().sorted_list_to_bst(test_chain)
    tree_root.display()
