import time

'''
1. How does the values are being passed in function, weather it is pass by value or pass by reference?
-> Python uses a mechanism called Call by Object Reference (also known as "Call by Assignment").

To understand this, you have to realize that variables in Python are not buckets that hold data. Instead, variables are just sticky notes (names) attached to objects in memory. When you pass a variable into a function, you aren't passing the bucket, and you aren't passing a pointer. You are taking a new sticky note (the function's parameter name) and attaching it to the exact same object.

How this behaves depends entirely on whether the object you passed is mutable (changeable) or immutable (unchangeable).

Scenario 1: Immutable Objects (Acts like Call by Value)
If you try to change an immutable object inside a function, Python is forced to create a brand new object and move the local sticky note to it. The original object remains untouched.

def try_to_change_string(text):
    # 'text' initially points to the same string as 'my_word'
    # But strings are immutable. Adding to it creates a NEW string object.
    text = text + " World!"
    print("Inside function:", text)

my_word = "Hello"
try_to_change_string(my_word)

# The original sticky note still points to the original string
print("Outside function:", my_word) 

# Output:
# Inside function: Hello World!
# Outside function: Hello


Scenario 2: Mutable Objects (Acts like Call by Reference)
Lists, Dictionaries, and Sets are mutable. You can change them in place without creating a new object.

If you modify a mutable object inside a function (like appending to a list), the original object is updated because both the outside sticky note and the inside sticky note are pointing to the exact same list.

def try_to_change_list(items):
    # 'items' points to the same list as 'my_list'
    # Lists are mutable, so we can change the object directly.
    items.append(4)
    print("Inside function:", items)

my_list = [1, 2, 3]
try_to_change_list(my_list)

# The original list was permanently changed!
print("Outside function:", my_list)

# Output:
# Inside function: [1, 2, 3, 4]
# Outside function: [1, 2, 3, 4]

The "Gotcha" with Mutable Objects
Even with mutable objects, if you use the = operator to assign a completely new value to the parameter, you are just moving the local sticky note to a new object. It breaks the connection to the original object.

def reassign_list(items):
    # This does NOT change the original list.
    # It just points 'items' to a brand new list in memory.
    items = [99, 100] 

my_list = [1, 2, 3]
reassign_list(my_list)
print(my_list) # Still outputs: [1, 2, 3]

Key insight: Python passes the reference to the object by value. You can modify the internals of a mutable object, but you cannot replace the original object entirely.
'''


'''
2. Explain Deep Copy and Shallow Copy?
-> Shallow Copy (copy.copy())
A shallow copy creates a brand new "outer" object, but it populates it with references (sticky notes) to the exact same inner objects.

If you modify the outer shell of the copy (like adding a completely new item), the original is unaffected. But if you modify an item inside one of the nested objects, both the original and the copy will change because they are sharing that inner object.

import copy

original_list = ["Apple", "Banana", ["Carrot", "Celery"]]

# Create a shallow copy
shallow_copy = copy.copy(original_list)

# 1. Modifying the outer list is safe
shallow_copy.append("Orange")
print(original_list)  # Does NOT have "Orange"

# 2. Modifying the inner list affects BOTH
shallow_copy[2].append("Spinach")
print(original_list[2])  # Outputs: ['Carrot', 'Celery', 'Spinach']

Note: Slicing a list (new_list = old_list[:]) or using the list() constructor also creates a shallow copy.

2. Deep Copy (copy.deepcopy())
A deep copy creates a brand new outer object and recursively creates brand new copies of all nested objects inside it.

The original and the deep copy are completely independent. Changing anything in the deep copy—no matter how deeply nested it is—will never affect the original object.

import copy

original_list = ["Apple", "Banana", ["Carrot", "Celery"]]

# Create a deep copy
deep_copy = copy.deepcopy(original_list)

# Modifying the inner list now only affects the copy
deep_copy[2].append("Spinach")

print(original_list[2])  # Outputs: ['Carrot', 'Celery']
print(deep_copy[2])      # Outputs: ['Carrot', 'Celery', 'Spinach']

Feature,        Shallow Copy (copy.copy),       Deep Copy (copy.deepcopy)
Outer Object        ,Creates a new object,      Creates a new object
Nested Objects,     Shares references with the original,        Creates independent copies
Memory Usage,       "Very fast, uses minimal extra memory",     "Slower, uses double the memory"
When to use,        "When the list contains only flat,       immutable items (like numbers/strings)."       ,"When dealing with complex, nested data structures (like a list of dictionaries)."
'''


# 2 - Output Based
def append_to_list(value, my_list = []):
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))

'''
Output:
    [1]
    [1, 2]

    The Explanation: In Python, default arguments are evaluated only once at the time the function is defined, not each time the function is called. Because a list is a mutable object, the exact same list in memory is being used and modified for every subsequent call that doesn't provide its own list.
    
    The Fix: You should always use None for mutable default arguments.
'''


'''
Read about yield vs return
'''


'''
3. How would you write a function that automatically measures and prints the execution time of any other function it is applied to?
'''

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start} seconds.")
        return result
    return wrapper

@timer
def heavy_computation():
    sum([i**2 for i in range(10000)])

heavy_computation()