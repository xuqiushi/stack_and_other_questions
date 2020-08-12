"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

    def __repr__(self):
        return str(self.val)


class Graph(object):
    def __init__(self, adj_list):
        self.root = None
        self.__make_graph(adj_list)

    def __make_graph(self, adj_list):
        nodes = [Node(i + 1) for i in range(len(adj_list))]
        for node_index, neighbor in enumerate(adj_list):
            for child_node_index in neighbor:
                nodes[node_index].neighbors.append(nodes[child_node_index - 1])
        self.root = nodes[0]


class Solution:
    @classmethod
    def clone_graph(cls, node: Node):
        if not node:
            return None
        old_cache = deque()
        old_cache.append(node)
        new_cache = deque()
        new_node = Node(1)
        new_cache.append(new_node)
        walked_node = {node: new_node}
        while old_cache:
            current_node = old_cache.popleft()
            current_new_node = new_cache.popleft()
            neighbors = current_node.neighbors
            for neighbor in neighbors:
                if neighbor not in walked_node:
                    new_neighbor = Node(neighbor.val)
                    current_new_node.neighbors.append(new_neighbor)
                    old_cache.append(neighbor)
                    new_cache.append(new_neighbor)
                    walked_node[neighbor] = new_neighbor
                else:
                    current_new_node.neighbors.append(walked_node[neighbor])
        return new_node


if __name__ == "__main__":
    test = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph = Graph(test)
    solution = Solution()
    test_new_node = solution.clone_graph(graph.root)
