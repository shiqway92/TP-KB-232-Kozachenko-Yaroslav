
def test_list_methods():
    lst = [1, 2, 3]
    print("Initial list:", lst)
    lst.extend([4, 5])
    print("After extend:", lst)
    lst.append(6)
    print("After append:", lst)
    lst.insert(2, 99)
    print("After insert:", lst)
    lst.remove(99)
    print("After remove:", lst)
    lst.sort()
    print("After sort:", lst)
    lst.reverse()
    print("After reverse:", lst)
    copied_list = lst.copy()
    print("Copied list:", copied_list)
    lst.clear()
    print("After clear:", lst)

if __name__ == "__main__":
    test_list_methods()
