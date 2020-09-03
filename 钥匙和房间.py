from typing import List
from collections import deque
import numpy as np


class Graph(object):
    def __init__(self, edges):
        self.edges = edges
        self.node_count = len(edges)

    def tarjan(self, start):
        selected_set = set()  # 已经被选择过的点
        result = []  # 结果
        gray_set = set()  # dfs中已经在栈中的点
        dfs_que = deque()  # 完成通用递归的dfs栈
        dfn = dict()  # tarjan dfn值
        dfn_que = deque()  # tarjan dfs栈
        dfn_selected_set = set()  # 相当于dfn的去重set
        low = dict()  # tarjan 最先祖先值
        # 开始深度搜索
        dfs_que.append(start)
        gray_set.add(start)
        appear_time = 0
        while dfs_que:
            # 取出dfs当前节点
            current_node = dfs_que.pop()
            # 当前节点加到当前dfn中，并初始化dfn与low
            dfn_que.append(current_node)
            dfn_selected_set.add(current_node)
            dfn[current_node] = appear_time
            low[current_node] = appear_time
            appear_time += 1
            # 更新一下当前的low并且如果还有未跑到的子节点，加到整体栈中。
            for next_node in self.edges[current_node]:
                if next_node in dfn_selected_set and next_node not in selected_set:
                    low[current_node] = min(low[current_node], dfn[next_node])
                if next_node not in gray_set:
                    dfs_que.append(next_node)
                    gray_set.add(next_node)
            # 如果当前节点还有出度则dfn不终止，如果当前没有出度则开始反向出栈dfn，这里的出度包含已经加入到整体栈中的节点。
            while dfn_que and (not self.edges[current_node] or not dfs_que):
                sub_result = []
                for i in range(len(dfn_que) - 1, -1, -1):
                    if i != len(dfn_que) - 1:
                        low[dfn_que[i]] = min(low[dfn_que[i]], low[dfn_que[i + 1]])
                    if dfn[dfn_que[i]] == low[dfn_que[i]]:
                        for j in range(len(dfn_que) - i):
                            sub_result.append(dfn_que.pop())
                            selected_set.add(sub_result[-1])
                        break
                result.append(sub_result)
                if dfs_que:
                    current_node = dfn_que[-1]
        return result


class Solution:
    @classmethod
    def get_adjacency_matrix(cls, rooms):
        matrix = np.zeros((len(rooms), len(rooms)))
        for room_index, room in enumerate(rooms):
            for key in room:
                matrix[room_index, key] = 1
        return matrix

    @classmethod
    def get_reachable_matrix(cls, adjacency_matrix):
        last_matrix = np.zeros(adjacency_matrix.shape)
        new_matrix = adjacency_matrix
        while not np.array_equal(last_matrix, new_matrix):
            last_matrix = new_matrix
            new_matrix = (new_matrix + np.eye(new_matrix.shape[0])).dot(
                new_matrix + np.eye(new_matrix.shape[0])
            )
            new_matrix[new_matrix > 0] = 1
        return new_matrix

    def can_visit_all_rooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 1:
            return True
        adjacency_matrix = self.get_adjacency_matrix(rooms)
        reachable_matrix = self.get_reachable_matrix(adjacency_matrix)
        return (reachable_matrix[0] == 1).all()


if __name__ == "__main__":
    test_rooms = [[1, 3], [2], [0], []]
    print(Graph(test_rooms).tarjan(0))
    pass
