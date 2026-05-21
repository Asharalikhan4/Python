'''
-> A list is a built-in data structure used to store multiple items in a single variable. think of it like a highly flexible array.
-> Some key characteristic:
    1. Ordered.
    2. Mutable. (Changeable)
    3. Heterogeneous.
    4. Allow Duplicates.
    5. Dynamic Size.
-> my_list = [1, "ashar"]
'''

my_list = [1, 2, 3, "ashar", "ali", "khan", True, False]
print("Original List", my_list)

'''
-> Adding elements in list
'''


'''
-> list_name.append(value): append the value at last.
'''
my_list.append(10)
print("List after append", my_list)


'''
-> list_name.extend(value): takes an iterable an append all the iterable value at last.
'''
my_list.extend((1, 2, "Hamza"))
print("List after extend", my_list)


'''
-> list_name.append(value): append the value at last.
'''
my_list.extend([1, 2, "Hamza"])
print("List after extend", my_list)