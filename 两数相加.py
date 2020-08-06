# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return f"{self.val} -> {self.next}"
        else:
            return f"{self.val}"


def generate_node_list(node_value_list):
    node = ListNode(node_value_list[0])
    current_node = node
    current_index = 1
    while current_index < len(node_value_list):
        current_node.next = ListNode(node_value_list[current_index])
        current_node = current_node.next
        current_index += 1
    return node


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_x = l1
        current_y = l2
        final_result = None
        current_carry = 0
        current_node = None
        while current_x or current_y or current_carry:
            current_x_value = current_x.val if current_x else 0
            current_y_value = current_y.val if current_y else 0
            current_result = current_x_value + current_y_value + current_carry
            remainder = current_result % 10
            if current_node:
                current_node.next = ListNode(remainder)
                current_node = current_node.next
            else:
                current_node = ListNode(remainder)
                final_result = current_node
            current_x = current_x.next if current_x else current_x
            current_y = current_y.next if current_y else current_y
            current_carry = current_result // 10
        return final_result


if __name__ == "__main__":
    test_x = [1]
    test_y = [9, 9]
    test_x_node = generate_node_list(test_x)
    test_y_node = generate_node_list(test_y)
    result = Solution().addTwoNumbers(test_x_node, test_y_node)
    print(result)
