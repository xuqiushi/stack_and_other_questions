def reverse_dict(final_result, middle_result, normal_dictionary):
    for key, value in normal_dictionary.items():
        if len(value.keys()) == 0:
            final_result[key] = value
            middle_result.append(final_result[key])
        else:
            reverse_dict(final_result, middle_result, value)
            for item in middle_result:
                item[key] = {}
            middle_result = []
            for item in middle_result:
                middle_result.append(item[key])


if __name__ == "__main__":
    test_normal_dictionary = {"a": {"b": {}}, "a1": {"b1": {"c1": {}, "d1": {}}}}
    result_dictionary = {}
    print(f"Origin dict: {test_normal_dictionary}")
    reverse_dict(result_dictionary, [], test_normal_dictionary)
    print(f"Reversed dict: {result_dictionary}")
