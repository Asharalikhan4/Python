'''
- List in python is like arrays in other languages.
- Symbol (Square Bracket) []
- List are mutable in nature.
- List are ordered.
- List are indexed.
- You can store any type of data.
'''


list_example = [1, "one", {"first_name": "Ashar"}]
print(list_example)

# Usig list as a constructor
a = list("ashar")
print("a", a)

# Creating list with repated items
b = [5] * 4
print("b", b)

# Accessing the list item
c = [1, "one", {"first_name": "Ashar"}]
print("Accessing list c items")
print(c[0])
print(c[1])
print(c[2])

# Some Methods of list
d = [1, 2, 3, 4, 5]
print("list d", d)

'''
append() -> Add an element at the end
'''
d.append(10)
print("list d after append method", d)


'''
extend() -> Add multiple element at the end of the list, takes a list as an input
'''
d.extend([11, 12, 13])
print("list d after extent method", d)


'''
- insert() -> insert the element at the specific position
- if you give the index greater then the length of the list the it put the element at the last.
- if you give the index less the zero then it will put the item at 0 index.
'''
d.insert(-1, 1)
d.insert(20, 4)
d.insert(4, 10)
print("list d after insert method", d)


'''
clear() -> Removes all the element from the list.
'''
d.clear()
print("list d after clear method", d)


e = [10, 11, 12, 13, 14, 11, 15]
print("List e", e)

'''
- remove() -> remove the first occurence of the element.
- if the element is not in the list then it will through an error.
- return None
'''
e.remove(11)
print("List d after remove", e)


'''
- pop() -> remove the element at the given index and if no index is given then it will take last index by default.
- take index as input and return popped value
- 
'''
poppped_value = e.pop(1)
print("List d after pop", e, "Poppped Value", poppped_value)


'''
- del() -> Delete an element at a specified index
- take index as input, if index is greater then the length of list then it will through error.
- return None
'''
del e[0]
print("List e after del() method", e)


print("\n-----------------------------------Iterating Over List-----------------------------------\n")

f = [1, 2, 3, 4, 5, 6]
for item in f:
    print(item)
    

print("\n-----------------------------------Nested List (Matrix)-----------------------------------\n")
g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(g[1][2])


print("\n-----------------------------------List Comprehension-----------------------------------\n")
'''
List comprehension is a concise way of writing a list using single line of code. it is useful for applying an operation or filter to items in an iterable, such as a list or range.
'''
squares = [x**2 for x in range(1, 6)]
print("Squares", squares)
