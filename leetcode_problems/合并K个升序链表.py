from typing import List, Optional

from achievement import ListNode


class Solution:
    def merge_k_lists(self, lists: List[ListNode]) -> Optional[ListNode]:
        result = None
        current_selected = None
        lists = [item for item in lists if item]
        if not lists:
            return None
        sorted_nodes = sorted(lists, key=lambda x: -x.val)
        while sorted_nodes:
            current_node = sorted_nodes.pop()
            if not result:
                result = current_node
                current_selected = current_node
            else:
                current_selected.next = current_node
                current_selected = current_selected.next
            if not current_node.next:
                continue
            else:
                current_node = current_node.next
                inserted = False
                insert_index = len(sorted_nodes) - 1
                while not inserted:
                    if insert_index == -1:
                        inserted = True
                        sorted_nodes.insert(0, current_node)
                    else:
                        if current_node.val <= sorted_nodes[insert_index].val:
                            sorted_nodes.insert(insert_index + 1, current_node)
                            inserted = True
                        else:
                            insert_index -= 1
        return result


if __name__ == "__main__":
    test_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    test_lists = [ListNode.generate_list_node(test_list) for test_list in test_lists]
    print(Solution().merge_k_lists(test_lists).display())
