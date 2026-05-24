'''
-> A comprehension is a concise, readable way to create a new collection (like a list, dictionary, or set) based on an existing sequence.
-> Syntax:
    [expression for item in iterable if condition]
    - expression: What you want the final output to be (e.g., multiply the item, capitalize it, or just keep it as is).
    - item: The current object you are looking at in the loop.
    - iterable: The existing list, tuple, or range you are looping through.
    - condition (optional): A filter so you only include certain items.
-> There are three types of comprehensions:
    1. List Comprehensions.
    2. Dictionary Comprehension.
    3. Set Comprehensions.
-> Why do we use it?
    1. Filter item
    2. Transform Item
    3. Create a new Collection
    4. Cleaner Code
    5. Faster Execution (Internal Mechanism is optimized in C)
'''