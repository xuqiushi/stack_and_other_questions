if __name__ == "__main__":
    a = [
        [7, 5, 1, 9, 4],
        [20, 11, 15, 17, 16],
        [23, 21, 24, 25, 30],
        [36, 34, 32, 40, 31],
        [44, 49, 42, 43, 50],
    ]
    dict_words = {"yes": 42, "no": 16, "good morning": 9, "morning sir": 34}
    remap_dict = {value: key for key, value in dict_words.items()}
    a_replaced = [[remap_dict.get(item, item) for item in row] for row in a]
    print(a_replaced)

    remap_dict = {value: key for key, value in dict_words.items()}
    print(remap_dict)
    a_replaced = []
    for row in a:
        new_row = []
        a_replaced.append(new_row)
        for item in row:
            if item in remap_dict:
                new_row.append(remap_dict[item])
            else:
                new_row.append(item)
    print(a_replaced)

    remap_dict = {value: key for key, value in dict_words.items()}
    print(remap_dict)
    for row in a:
        for item_index in range(len(row)):
            if row[item_index] in remap_dict:
               row[item_index] = remap_dict[row[item_index]]

    print(a)
    
