from collections import deque
from leetcode_python.achievement import ListNode


class Solution:
    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        new_head = head
        current_last = None
        while head:
            reversed_nodes = deque()
            sub_index = 0
            for sub_index in range(k):
                if not head:
                    sub_index -= 1
                    break
                reversed_nodes.append(head)
                head = head.next
            if sub_index < k - 1 or sub_index == 0:
                break
            current_next = head
            current_first = reversed_nodes.pop()
            if not current_last:
                new_head = current_first
            else:
                current_last.next = current_first
            current_sub = current_first
            while reversed_nodes:
                current_sub.next = reversed_nodes.pop()
                current_sub = current_sub.next
            current_sub.next = current_next
            current_last = current_sub
        return new_head


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    test_k = 3
    test_head = ListNode.generate_list_node(test_list)
    print(test_head.display())
    print(Solution().reverse_k_group(test_head, test_k).display())
