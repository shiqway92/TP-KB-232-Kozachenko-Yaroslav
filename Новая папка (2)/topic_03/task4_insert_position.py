
def find_insert_position(sorted_list, value):
    for i, elem in enumerate(sorted_list):
        if value < elem:
            return i
    return len(sorted_list)

if __name__ == "__main__":
    sorted_list = [1, 3, 4, 7, 10]
    value = 5
    print(f"Sorted list: {sorted_list}")
    print(f"Value to insert: {value}")
    print(f"Insert position: {find_insert_position(sorted_list, value)}")
