'''
1. What is the time complexity of checking if an item exists in a set versus a list?
-> In list it is O(n) because we have to traverse the whole list, while in set it is O(1) cause we have used hashed key's.
'''


'''
2. Why do you get a TypeError if you try to put a list inside a set?
-> You cannot put mutable objects (like lists or dictionaries) inside a set because they are unhashable. A set relies on a fixed hash value to determine exactly where an item lives in memory. If the object could change, its hash would change, breaking the entire data structure
'''


'''
3. How would you use a set as a dictionary key?
-> You can't use a normal set because it's mutable. You must cast it to a frozenset first.
'''