from collections import deque
from typing import Optional


class ListNode:
    """
    此为一个简单的链表
    """

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __repr__(self):
        return f"{self.val}"

    @classmethod
    def generate_list_node(cls, list_data):
        root_node = cls(list_data[0])
        current_node = root_node
        for node_value in list_data[1:]:
            next_node = cls(node_value)
            current_node.next = next_node
            current_node = next_node
        return root_node

    def display(self, root=None):
        if not root:
            return f"{self.val}=>{self.next.display(root=self)}"
        else:
            if self != root:
                if not self.next:
                    return f"{self.val}"
                else:
                    return f"{self.val}=>{self.next.display(root=root)}"


class TreeNode:
    """
    此为一个简单的树中节点结构
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    def display(self):
        lines, *_ = self.display_aux()
        for line in lines:
            print(line)

    def display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "%s" % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.display_aux()
        right, m, q, y = self.right.display_aux()
        s = "%s" % self.val
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Tree:
    """
    此为一个简单的生成树结构
    """

    def __init__(self, node_values):
        self.node_values = node_values
        self.root = TreeNode(node_values.pop(0))
        self.add_node([self.root], self.node_values)

    @classmethod
    def add_node(cls, standby_nodes, to_add_values):
        new_standby_node = []
        for standby_node in standby_nodes:
            if to_add_values:
                standby_node.left = (
                    TreeNode(to_add_values.pop(0))
                    if to_add_values[0]
                    else to_add_values.pop(0)
                )
            if to_add_values:
                standby_node.right = (
                    TreeNode(to_add_values.pop(0))
                    if to_add_values[0]
                    else to_add_values.pop(0)
                )
            if standby_node.left:
                new_standby_node.append(standby_node.left)
            if standby_node.right:
                new_standby_node.append(standby_node.right)
        if to_add_values:
            cls.add_node(new_standby_node, to_add_values)


class BalancedTreeGetter:
    """
    此为一个简单生成平衡排序树结构
    """

    def __init__(self):
        self.current_root = None

    @classmethod
    def get_balance_rate(cls, node, height):
        left_height = height[node.left] if node.left else 0
        right_height = height[node.right] if node.right else 0
        return right_height - left_height

    @classmethod
    def left_rotate_old(cls, center_node, balanced_rate):
        if not center_node.right.left:
            balanced_rate[center_node] -= 2
            balanced_rate[center_node.right] -= 1
            sub_center = center_node.right
            sub_center.left = center_node
            center_node.right = None
        else:
            sub_center = center_node.right
            center_node.right = sub_center.left
            sub_center.left = center_node
            balanced_rate[center_node] -= 1
            balanced_rate[sub_center] -= 1
        return sub_center

    def insert_right(self, node, value, balanced_rate):
        if node not in balanced_rate:
            balanced_rate[node] = 0
        if node.right:
            add_height = self.insert_right(node.right, value, balanced_rate)
            if add_height:
                balanced_rate[node] += 1
            if balanced_rate[node.right] > 1:
                node.right = self.left_rotate_old(node.right, balanced_rate)
                add_height = 0
                balanced_rate[node] -= 1
            elif balanced_rate[node] > 1 and node == self.current_root:
                self.current_root = self.left_rotate_old(node, balanced_rate)
            return add_height
        else:
            node.right = TreeNode(value)
            balanced_rate[node.right] = 0
            if not node.left:
                balanced_rate[node] += 1
                return 1
            else:
                return 0

    def sorted_list_to_bst(self, head: ListNode) -> Optional[TreeNode]:
        if not head:
            return None
        self.current_root = head
        balanced_rate = dict()
        if not head.next:
            return TreeNode(head.val)
        self.current_root = TreeNode(head.val)
        current_list_node = head.next
        balanced_rate[self.current_root] = 0
        while current_list_node:
            self.insert_right(self.current_root, current_list_node.val, balanced_rate)
            current_list_node = current_list_node.next
        return self.current_root


class CommonBalancedTreeGetter(object):
    def __init__(self, unsorted_list):
        self.current_root = None
        self.unsorted_list = unsorted_list
        self.height = {}

    def get_bst(self):
        if not self.unsorted_list:
            return None
        self.current_root = TreeNode(self.unsorted_list[0])
        self.height[self.current_root] = 1
        for num in self.unsorted_list[1:]:
            self.common_insert(num)
            self.current_root.display()
        return self.current_root

    def common_insert(self, value):
        node_history, directory_history, add_height = self._insert(value)
        rotate_center, rotate_father, rotate_type = self._update_height(
            node_history, directory_history, add_height
        )
        self._common_rotate(rotate_center, rotate_father, rotate_type)

    def _get_height(self, node):
        if not node:
            return 0
        else:
            return self.height[node]

    def _get_current_height(self, node):
        return max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _insert(self, value):
        step_node = self.current_root
        node_history = deque([step_node])
        directory_history = deque(["middle"])
        add_height = False
        while step_node:
            if value == step_node.val:
                break
            elif value < step_node.val:
                if not step_node.left:
                    step_node.left = TreeNode(value)
                    node_history.appendleft(step_node.left)
                    directory_history.appendleft("left")
                    if step_node.left not in self.height:
                        self.height[step_node.left] = 1
                    if not step_node.right:
                        add_height = True
                    break
                else:
                    node_history.appendleft(step_node.left)
                    directory_history.appendleft("left")
                    step_node = step_node.left
            else:
                if not step_node.right:
                    step_node.right = TreeNode(value)
                    node_history.appendleft(step_node.right)
                    if step_node.right not in self.height:
                        self.height[step_node.right] = 1
                    directory_history.appendleft("right")
                    if not step_node.left:
                        add_height = True
                    break
                else:
                    node_history.appendleft(step_node.right)
                    directory_history.appendleft("right")
                    step_node = step_node.right
        return node_history, directory_history, add_height

    def _update_height(self, node_history, directory_history, add_height):
        node_index = -1
        node_history.popleft()
        rotate_center = None
        rotate_type = ()
        rotate_father = None
        while node_history:
            current_node = node_history.popleft()
            if add_height:
                self.height[current_node] += 1
            node_index += 1
            if rotate_center:
                rotate_father = current_node
            left_height = self.height[current_node.left] if current_node.left else 0
            right_height = self.height[current_node.right] if current_node.right else 0
            if (
                right_height - left_height >= 2 or right_height - left_height <= -2
            ) and not rotate_center:
                rotate_center = current_node
                rotate_type = (
                    directory_history[node_index],
                    directory_history[node_index - 1],
                )
        return rotate_center, rotate_father, rotate_type

    def _common_rotate(self, rotate_center, rotate_father, rotate_type):
        if rotate_center:
            if rotate_type == ("right", "right"):
                sub_center = self.left_rotate(rotate_center)
                if rotate_father:
                    rotate_father.right = sub_center
                else:
                    self.current_root = sub_center
            elif rotate_type == ("left", "left"):
                sub_center = self.right_rotate(rotate_center)
                if rotate_father:
                    rotate_father.left = sub_center
                else:
                    self.current_root = sub_center
            elif rotate_type == ("right", "left"):
                sub_center = self.right_left_rotate(rotate_center)
                if rotate_father:
                    rotate_father.left = sub_center
                else:
                    self.current_root = sub_center
            elif rotate_type == ("left", "right"):
                sub_center = self.left_right_rotate(rotate_center)
                if rotate_father:
                    rotate_father.left = sub_center
                else:
                    self.current_root = sub_center
            if rotate_father:
                self.height[rotate_father] = self._get_current_height(rotate_father)
            else:
                self.height[self.current_root] = self._get_current_height(
                    self.current_root
                )

    def left_rotate(self, center_node):
        sub_center = center_node.right
        center_node.right = sub_center.left
        sub_center.left = center_node
        self.height[center_node] = self._get_current_height(center_node)
        self.height[sub_center] = self._get_current_height(sub_center)
        return sub_center

    def right_rotate(self, center_node):
        sub_center = center_node.left
        center_node.left = sub_center.right
        sub_center.right = center_node
        self.height[center_node] = self._get_current_height(center_node)
        self.height[sub_center] = self._get_current_height(sub_center)
        return sub_center

    def right_left_rotate(self, center_node):
        center_node.right = self.right_rotate(center_node.right)
        result = self.left_rotate(center_node)
        return result

    def left_right_rotate(self, center_node):
        center_node.left = self.left_rotate(center_node.left)
        return self.right_rotate(center_node)


if __name__ == "__main__":
    test_list = [7, 6, 9, 15, 16, 12, 5, 3]
    test_result = CommonBalancedTreeGetter(test_list).get_bst()
    test_result.display()
