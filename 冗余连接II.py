from collections import deque
from typing import List


class Solution:
    @classmethod
    def find_root(cls, roots, node):
        if roots[node] != node:
            roots[node] = cls.find_root(roots, roots[node])
            return roots[node]
        else:
            return roots[node]

    def find_redundant_directed_connection(self, edges: List[List[int]]) -> List[int]:
        edge_count = len(edges)
        roots = {i: i for i in range(edge_count + 1)}
        parents = {i: i for i in range(edge_count + 1)}
        double_parent = -1
        circle = -1
        for edge_index, (start_node, end_node) in enumerate(edges):
            if parents[end_node] != end_node:
                double_parent = edge_index
            else:
                parents[end_node] = start_node
                start_root = self.find_root(roots, start_node)
                end_root = self.find_root(roots, end_node)
                if start_root == end_root:
                    circle = edge_index
                else:
                    roots[end_node] = start_root
        if double_parent < 0:
            return edges[circle]
        else:
            if circle < 0:
                return edges[double_parent]
            else:
                return [parents[edges[double_parent][1]], edges[double_parent][1]]


if __name__ == "__main__":
    test_edges = [[4, 2], [1, 5], [5, 2], [5, 3], [2, 4]]
    print(Solution().find_redundant_directed_connection(test_edges))
