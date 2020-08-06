from itertools import combinations

from scipy.sparse import csc_matrix
import numpy as np


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
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
            lines, n, p, x = self.left._display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
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


class Solution:
    def get_nodes_and_lines(self, parent_index, current_node, lines, values):
        if current_node:
            values.append(current_node.val)
            current_index = len(values) - 1
            if parent_index >= 0:
                lines.append((parent_index, current_index))
            if current_node.left:
                self.get_nodes_and_lines(
                    current_index, current_node.left, lines, values
                )
            if current_node.right:
                self.get_nodes_and_lines(
                    current_index, current_node.right, lines, values
                )

    def rob(self, root) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        lines = []
        values = []
        self.get_nodes_and_lines(-1, root, lines, values)
        lines = np.array(lines)
        half_relate_matrix = csc_matrix(
            (np.ones(lines.shape[0]), (lines[:, 0], lines[:, 1])),
            shape=(len(values), len(values)),
        ).toarray()
        relate_matrix = np.ones((len(values), len(values))) - half_relate_matrix - half_relate_matrix.T
        all_combinations = [
            item
            for r in range(len(values), len(values))
            for item in list(combinations(range(len(values)), r))
        ]
        values = np.array(values).reshape(1, -1)
        result = []
        for combination in all_combinations:
            combination_relate = relate_matrix[combination, :][:, combination]
            if (combination_relate.sum(axis=0) == len(combination)).all():
                result.append(values[:, combination][0].sum())
        return max(result)


class SolutionTwo:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root: return 0, 0

            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)

            return root.val + ln + rn, max(ls, ln) + max(rs, rn)

        return max(_rob(root))


if __name__ == "__main__":
    test_node_values = [
        41,
        37,
        44,
        24,
        39,
        42,
        48,
        1,
        35,
        38,
        40,
        None,
        43,
        46,
        49,
        0,
        2,
        30,
        36,
        None,
        None,
        None,
        None,
        None,
        None,
        45,
        47,
        None,
        None,
        None,
        None,
        None,
        4,
        29,
        32,
        None,
        None,
        None,
        None,
        None,
        None,
        3,
        9,
        26,
        None,
        31,
        34,
        None,
        None,
        7,
        11,
        25,
        27,
        None,
        None,
        33,
        None,
        6,
        8,
        10,
        16,
        None,
        None,
        None,
        28,
        None,
        None,
        5,
        None,
        None,
        None,
        None,
        None,
        15,
        19,
        None,
        None,
        None,
        None,
        12,
        None,
        18,
        20,
        None,
        13,
        17,
        None,
        None,
        22,
        None,
        14,
        None,
        None,
        21,
        23,
    ]
    test_tree = Tree(test_node_values)
    print(SolutionTwo().rob(test_tree.root))
