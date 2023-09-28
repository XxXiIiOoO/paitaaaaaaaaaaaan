def find_element(tup, element):
    if element in tup:
        return tup.index(element)
    else:
        return "Элемент не найден"

my_tuple = (1, 2, 3, 4, 5)
result = find_element(my_tuple, 3)
print(result)