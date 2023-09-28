def remove_duplicates(numbers):
    return list(set(numbers))

my_list = [1, 2, 3, 3, 4, 4, 5, 6, 13, 13]
result = remove_duplicates(my_list)
print(result)