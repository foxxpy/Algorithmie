from sort_dict import print_sort_dict

def test_sort_dict():
    dictionnaire = {"c" : 3, "b" : 10, "a" : 456}
    print_sort_dict(dictionnaire)

    print()
    dictionnaire2 = {"François" : 1000, "Alice" : 2000, "Bob" : 4000}
    print_sort_dict(dictionnaire2)

test_sort_dict()
