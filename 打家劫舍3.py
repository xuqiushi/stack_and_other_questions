from itertools import combinations

from scipy.sparse import csc_matrix
import numpy as np

from achievement import TreeNode, Tree


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
