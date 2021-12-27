def solve(n):
    if n == 1:
        print(f"current_index: {n}, current_value: {1}")
        return 1
    else:
        last_value = solve(n - 1)
        result = last_value + 1 / (last_value ** 2)
        print(f"current_index: {n}, current_value: {result}")
        return result


if __name__ == "__main__":
    print(solve(18))
