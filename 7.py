def remove_element(tup, element):
    return tuple(x for x in tup if x != element)

my_tuple = (1, 2, 3, 4, 5)
result = remove_element(my_tuple, 3)
print(result)