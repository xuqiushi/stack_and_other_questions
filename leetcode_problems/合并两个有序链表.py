from achievement import ListNode


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        current_result_node = None
        current_first_node = l1
        current_second_node = l2
        while current_first_node or current_second_node:
            if not current_first_node:
                current_select_node = current_second_node
                current_second_node = current_second_node.next
            elif not current_second_node:
                current_select_node = current_first_node
                current_first_node = current_first_node.next
            elif current_first_node.val <= current_second_node.val:
                current_select_node = current_first_node
                current_first_node = current_first_node.next
            elif current_second_node.val <= current_first_node.val:
                current_select_node = current_second_node
                current_second_node = current_second_node.next
            else:
                raise ValueError("Wrong")
            if not result:
                result = current_select_node
                current_result_node = current_select_node
            else:
                current_result_node.next = current_select_node
                current_result_node = current_result_node.next
        return result


if __name__ == "__main__":
    test_l1 = ListNode.generate_list_node([1, 2, 4])
    test_l2 = ListNode.generate_list_node([1, 2, 4])
    print(Solution().merge_two_lists(test_l1, test_l2))
