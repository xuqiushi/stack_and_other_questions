from collections import deque
from achievement import ListNode


class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        cache = deque(maxlen=n + 1)
        current_node = head
        while current_node:
            cache.append(current_node)
            current_node = current_node.next
        if len(cache) < n + 1:
            to_delete_node = cache.popleft()
            head = to_delete_node.next
        elif n == 1:
            last_node = cache.popleft()
            last_node.next = None
        else:
            last_node = cache.popleft()
            cache.popleft()
            next_node = cache.popleft()
            last_node.next = next_node
        return head


if __name__ == "__main__":
    test_list = [1, 2]
    test_n = 1
    test_chain_head = ListNode.generate_list_node(test_list)
    print(Solution().remove_nth_from_end(test_chain_head, test_n))
