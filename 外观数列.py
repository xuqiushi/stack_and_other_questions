from collections import OrderedDict


class Solution:
    @classmethod
    def get_description(cls, word):
        custom_counter = []
        last_char = None
        for char in word:
            if not last_char:
                custom_counter.append([char, 1])
                last_char = char
            else:
                if char == last_char:
                    custom_counter[-1][1] += 1
                else:
                    custom_counter.append([char, 1])
                last_char = char
        result = ""
        for item in custom_counter:
            result += f"{item[1]}{item[0]}"
        return result

    def count_and_say(self, n: int) -> str:
        result = "1"
        for i in range(1, n):
            result = self.get_description(result)
        return result


if __name__ == "__main__":
    test_n = 6
    print(Solution().count_and_say(test_n))
