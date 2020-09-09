from typing import List
import heapq


class Solution:
    @classmethod
    def _get_graph(cls, nums):
        result = set()
        all_points = set()
        for num_index, num in enumerate(nums):
            all_points.add(num_index)
            for i in range(1, num + 1):
                result.add((num_index, num_index + i))
        return all_points, result

    @classmethod
    def _dijkstra(cls, start, al_points, graph):
        standby_set = al_points.copy()
        standby_set.remove(start)
        connection = {}
        for point in standby_set:
            connection[point] = start
        existed_distance = {start: 0}
        standby_distance_dict = {}
        for point in standby_set:
            if (start, point) in graph:
                standby_distance_dict[point] = 1
        while standby_set:
            next_point = min(standby_distance_dict, key=standby_distance_dict.get)
            existed_distance[next_point] = standby_distance_dict[next_point]
            standby_set.remove(next_point)
            del standby_distance_dict[next_point]
            for standby_index, standby_point in enumerate(standby_set):
                if (next_point, standby_point) in graph and standby_point not in standby_distance_dict:
                    standby_distance_dict[standby_point] = existed_distance[next_point] + 1
        return existed_distance

    def jump(self, nums: List[int]) -> int:
        if len(set(nums)) == 1 and set(nums).pop() == 1:
            return len(nums) - 1
        al_points, graph = self._get_graph(nums)
        distance = self._dijkstra(0, al_points, graph)
        return distance[len(nums) - 1]


if __name__ == "__main__":
    test_nums = [2,3,1,1,4]
    print(Solution().jump(test_nums))
