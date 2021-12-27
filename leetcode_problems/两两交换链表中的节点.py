from achievement import ListNode


class Solution:
    def swap_pairs(self, head: ListNode) -> ListNode:
        new_head = head
        current_last = None
        while head:
            current_first = head
            head = head.next
            if not head:
                break
            current_second = head
            head = head.next
            current_next = head
            if not current_last:
                new_head = current_second
            else:
                current_last.next = current_second
            current_second.next = current_first
            current_first.next = current_next
            current_last = current_first
        return new_head


if __name__ == "__main__":
    test_list = [1, 2, 3, 4]
    test_head = ListNode.generate_list_node(test_list)
    print(test_head.display())
    print(Solution().swap_pairs(test_head).display())
