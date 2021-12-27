from typing import List
from collections import deque
from copy import deepcopy


class Solution:
    @classmethod
    def get_hashed_path(cls, tickets):
        hashed_tickets = {}
        for ticket in tickets:
            if ticket[0] in hashed_tickets:
                hashed_tickets[ticket[0]].append(ticket[1])
                hashed_tickets[ticket[0]] = list(
                    reversed(sorted(hashed_tickets[ticket[0]]))
                )
            else:
                hashed_tickets[ticket[0]] = [ticket[1]]
        return hashed_tickets

    @classmethod
    def dfs_recursion_find_path(cls, start, hashed_tickets):
        if start not in hashed_tickets:
            return None
        else:
            next_positions = hashed_tickets[start]
            for position_index in range(len(next_positions) - 1, -1, -1):
                new_hashed_tickets = deepcopy(hashed_tickets)
                new_start = new_hashed_tickets[start].pop(position_index)
                if not new_hashed_tickets[start]:
                    del new_hashed_tickets[start]
                if not new_hashed_tickets:
                    return [start, new_start]
                else:
                    sub_path = cls.dfs_recursion_find_path(
                        new_start, new_hashed_tickets
                    )
                    if sub_path:
                        return [start] + sub_path
                    else:
                        continue

    @classmethod
    def dfs_stack_find_path(cls, start, hashed_tickets):
        cache = deque()
        current_hashed_tickets = hashed_tickets
        cache.append(([start], current_hashed_tickets))
        while cache:
            current = cache.pop()
            current_hashed_tickets = current[1]
            if not current_hashed_tickets:
                return current[0]
            if current[0][-1] not in current_hashed_tickets:
                continue
            next_positions = current_hashed_tickets[current[0][-1]]
            for position_index in range(len(next_positions)):
                new_hashed_tickets = deepcopy(current_hashed_tickets)
                new_start = new_hashed_tickets[current[0][-1]].pop(position_index)
                if not new_hashed_tickets[current[0][-1]]:
                    del new_hashed_tickets[current[0][-1]]
                cache.append((current[0] + [new_start], new_hashed_tickets))
        return None

    @classmethod
    def hierholzer_search(cls, start, hashed_tickets):
        cache = deque()
        result = deque()
        cache.append(start)
        while cache:
            if cache[-1] in hashed_tickets:
                next_node = hashed_tickets[cache[-1]].pop()
                if not hashed_tickets[cache[-1]]:
                    del hashed_tickets[cache[-1]]
                cache.append(next_node)
            else:
                result.appendleft(cache.pop())
        return list(result)

    def find_itinerary(self, tickets: List[List[str]]) -> List[str]:
        hashed_tickets = self.get_hashed_path(tickets)
        start_ticket = "JFK"
        return self.hierholzer_search(start_ticket, hashed_tickets)


if __name__ == "__main__":
    test_tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(Solution().find_itinerary(test_tickets))
