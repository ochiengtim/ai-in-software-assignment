def sort_dicts_by_key(list_of_dicts, sort_key, reverse=False):
    """
    Sorts a list of dictionaries by a specified key.

    Args:
        list_of_dicts (list): List of dictionaries to sort.
        sort_key (str): The key to sort the dictionaries by.
        reverse (bool): Whether to sort in descending order. Default is False (ascending).

    Returns:
        list: A new list of dictionaries sorted by the specified key.
    """
    return sorted(list_of_dicts, key=lambda x: x.get(sort_key, None), reverse=reverse)

# Example usage:
if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    sorted_data = sort_dicts_by_key(data, "age")
    print(sorted_data)

def manual_sort_dicts_by_key(dict_list, key):
    for i in range(len(dict_list)):
        for j in range(i + 1, len(dict_list)):
            if dict_list[i].get(key, '') > dict_list[j].get(key, ''):
                dict_list[i], dict_list[j] = dict_list[j], dict_list[i]
    return dict_list

sample = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

print("Copilot Suggestion:")
print(sort_dicts_by_key(sample, "age"))

print("Manual Sort:")
print(manual_sort_dicts_by_key(sample.copy(), "age"))
