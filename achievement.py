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
    def left_rotate(cls, center_node, balanced_rate):
        if not center_node.right.left:
            balanced_rate[center_node] = 0
            balanced_rate[center_node.right] = 0
            balanced_rate[center_node.right.right] = 0
            sub_center = center_node.right
            sub_center.left = center_node
            center_node.right = None
        else:
            sub_center = center_node.right
            center_node.right = sub_center.left
            sub_center.left = center_node
            balanced_rate[center_node] = 0
            balanced_rate[sub_center] = 0
        return sub_center

    def insert_right(self, node, value, balanced_rate):
        if node not in balanced_rate:
            balanced_rate[node] = 0
        if node.right:
            add_height = self.insert_right(node.right, value, balanced_rate)
            if add_height:
                balanced_rate[node] += 1
            if balanced_rate[node.right] > 1:
                node.right = self.left_rotate(node.right, balanced_rate)
                add_height = 0
                balanced_rate[node] -= 1
            elif balanced_rate[node] > 1 and node == self.current_root:
                self.current_root = self.left_rotate(node, balanced_rate)
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
