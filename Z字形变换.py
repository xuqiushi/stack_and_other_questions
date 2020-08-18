from collections import deque


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows < 2:
            return s
        result = {i: deque() for i in range(num_rows)}
        interval = 2 * num_rows - 2
        for char_index, char in enumerate(s):
            current_line = char_index % interval
            if current_line > num_rows - 1:
                current_line = num_rows - (current_line - num_rows + 1) - 1
            result[current_line].append(char)
        string_result = deque()
        for i in range(num_rows):
            while result[i]:
                string_result.append(result[i].popleft())
        return "".join(string_result)


if __name__ == "__main__":
    test_string = "ABCDEF"
    test_rows = 5
    solution = Solution()
    print(solution.convert(test_string, test_rows))
