'''
-> A tuple is a built-in data type used to store a collection of items in a single variables.
-> Some key characteristic:
    1. Ordered.
    2. Immutable. (Once tuple is created, you cannot change, add or remove it's elements.)
    3. Heterogeneous.
    4. Allow Duplicates.
-> my_tup = (1, 2, 3, "ashar", "ali", "khan")
-> The Comma Rule (Syntax Quirk):
    - Parentheses () are strongly associated with tuples, but they don't actually create them — commas do. The parentheses are mostly there for grouping and readability.
    - x = (5) creates an integer.
    - x = (5,) creates a tuple with one item.
    - x = 5, 6, 7 creates a tuple without any parentheses at all (called tuple packing).
    - The only time parentheses are strictly required to create a tuple is when creating an empty one: empty_tuple = ().
-> The "Immutability Illusion":
    - Tuples are immutable, but there is a massive catch that interviewers love to test: a tuple only locks its direct contents (the memory references), not nested objects.
    - If a tuple contains a mutable object, like a list, you cannot replace the list with a new object. However, you can modify the contents of the list itself.
-> Feature,List,Tuple
Memory Allocation,Over-allocates (reserves extra blank slots for append),Exact allocation (no wasted space)
Size in Bytes (empty),~56 bytes,~40 bytes
Compilation,Evaluated at runtime,Evaluated at compile-time (Constant Folding)
Hashability,Unhashable (cannot be dictionary keys),Hashable (if all internal elements are hashable)
-> Note: Byte sizes vary by Python version and system architecture, but tuples are universally smaller.
-> Constant Folding: When you write a = (1, 2, 3) in your script, Python's compiler sees it and stores it as a constant right away. When you write b = [1, 2, 3], Python actually executes code at runtime to construct that list every time the script hits that line.
'''

my_tuple = (1, 2, 3, "ashar", "ali", "khan")
print("Original Tuple", my_tuple, type(my_tuple))