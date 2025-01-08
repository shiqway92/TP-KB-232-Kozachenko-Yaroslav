
def test_dict_methods():
    d = {'name': 'Alice', 'age': 25}
    print("Initial dictionary:", d)
    d.update({'age': 26, 'city': 'Kyiv'})
    print("After update:", d)
    print("Keys:", list(d.keys()))
    print("Values:", list(d.values()))
    print("Items:", list(d.items()))
    del d['age']
    print("After delete 'age':", d)
    d.clear()
    print("After clear:", d)

if __name__ == "__main__":
    test_dict_methods()
