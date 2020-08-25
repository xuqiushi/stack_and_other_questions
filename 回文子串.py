from math import ceil


class Solution:
    @classmethod
    def get_current_max_length(cls, position, new_string, half_length=0):
        max_range = min(
            len(new_string) - half_length, len(new_string) - position - half_length
        )
        current_half_length = half_length
        for i in range(1, max_range):
            if (
                new_string[position - half_length - i]
                == new_string[position + half_length + i]
            ):
                current_half_length += 1
            else:
                break

        return current_half_length

    @classmethod
    def get_sub_half_length(cls, new_string):
        max_half_length = [0 for i in new_string]
        current_max_half_length = 0
        current_max_center = 0
        current_position = 0
        while current_position <= len(new_string) - 1:
            if current_position >= current_max_center + current_max_half_length:
                max_half_length[current_position] = cls.get_current_max_length(
                    current_position, new_string
                )
                current_max_center = current_position
                current_max_half_length = max_half_length[current_position]
            symmetry_point_position = 2 * current_max_center - current_position
            current_max_left = current_max_center - current_max_half_length
            if (
                current_max_left
                < symmetry_point_position - max_half_length[symmetry_point_position]
            ):
                max_half_length[current_position] = max_half_length[
                    symmetry_point_position
                ]
            elif (
                current_max_left
                > symmetry_point_position - max_half_length[symmetry_point_position]
            ):
                max_half_length[current_position] = (
                    symmetry_point_position - current_max_left
                )
            else:
                max_half_length[current_position] = cls.get_current_max_length(
                    current_position,
                    new_string,
                    symmetry_point_position - current_max_left,
                )
            if max_half_length[current_position] + current_position > current_max_center + current_max_half_length:
                current_max_center = current_position
                current_max_half_length = max_half_length[current_position]
            current_position += 1
        return max_half_length

    def countSubstrings(self, s: str) -> int:
        new_string = "#" + "#".join(s) + "#"
        max_half_length = self.get_sub_half_length(new_string)
        return sum([ceil(length / 2) for length in max_half_length])


if __name__ == "__main__":
    test_string = "abc"
    print(Solution().countSubstrings(test_string))
