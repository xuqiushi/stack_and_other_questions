from math import floor


class Solution:
    @classmethod
    def left_right_search(cls, s, current_position, current_half_length=0):
        left_remaining = current_position - current_half_length
        right_remaining = (len(s) - 1) - current_position - current_half_length
        min_remaining = min(left_remaining, right_remaining)
        total_count = 0
        for i in range(1, min_remaining + 1):
            if (
                s[current_position - current_half_length - i]
                == s[current_position + current_half_length + i]
            ):
                total_count += 1
            else:
                break
        return total_count

    def longest_palindrome(self, s: str) -> str:
        new_string = "#" + "#".join(s) + "#"
        longest_center = -1
        longest_half_length = -1
        every_half_length = [0 for i in range(len(new_string))]
        for i in range(len(new_string)):
            if i >= longest_center + longest_half_length:
                current_half_length = self.left_right_search(new_string, i)
            else:
                longest_left = longest_center - longest_half_length
                symmetry_point = 2 * longest_center - i
                symmetry_left = symmetry_point - every_half_length[symmetry_point]
                if symmetry_left > longest_left:
                    current_half_length = every_half_length[symmetry_point]
                elif symmetry_left < longest_left:
                    current_half_length = longest_center + longest_half_length - i
                else:
                    current_half_length = self.left_right_search(new_string, i)
            every_half_length[i] = current_half_length
            if i + current_half_length > longest_center + longest_half_length:
                longest_center = i
                longest_half_length = current_half_length
        true_max_index = every_half_length.index(max(every_half_length))
        longest_string = new_string[
            true_max_index
            - max(every_half_length) : true_max_index
            + max(every_half_length)
            + 1
        ]
        return longest_string.replace("#", "")


if __name__ == "__main__":
    test_string = "babad"
    solution = Solution()
    print(solution.longest_palindrome(test_string))
