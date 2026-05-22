'''
-> Python Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.
-> Some key characteristic:
    1. Uniqueness
    2. Unordered
    3. Mutable
    4. No Indexing
-> my_set = {1, 2, 3}
-> Creating an empty set empty_set = new Set()
-> Sets are incredibly fast because they are implemented using a hash table. When you add an element to a set, Python passes it through a mathematical formula (a hash function) that determines exactly where in memory that item should live.
-> This architecture creates two massive implications for how you code:
    1. Lightning-Fast Lookups: Checking if an item exists in a list (x in my_list) is $O(n)$ because Python has to scan every item. Checking if an item exists in a set (x in my_set) is $O(1)$. Python just runs the hash function and looks directly at that one memory slot.
    2. The "Hashable" Rule: Because items must be processed by a hash function, everything inside a set must be immutable. You can put strings, integers, and tuples inside a set. If you try to put a mutable object like a list or dictionary inside a set, your program will crash with an TypeError: unhashable type.
-> A frozenset is exactly what it sounds like: an immutable version of a Python set. Once you create it, you cannot add, remove, or modify its elements.
-> Earlier, we established a golden rule: you cannot put mutable objects into a hash table. Because normal sets are mutable, they are unhashable. This creates a paradox if you ever need to use a set as a dictionary key, or if you want to create a set of sets. A frozenset solves this by locking the data down, making it hashable.
'''