'''
1. What is the difference between List and Tuple.
Feature,List,Tuple
Mutability,Mutable (can be changed),Immutable (cannot be changed)
Syntax,Square brackets [],Parentheses ()
Memory,Uses more memory overhead,More memory-efficient
Use Case,Data that changes over time,"Fixed records (e.g., coordinates)"
'''

'''
2. How are Python lists implemented under the hood?
Answer: They are implemented as dynamic arrays (specifically, arrays of pointers), not as linked lists. This means accessing an element by index is $O(1)$ fast, but inserting an element at the beginning is $O(n)$ slow because all subsequent elements must be shifted in memory.
'''

'''
3. What is the difference between a shallow copy and a deep copy of a list?
Answer: A shallow copy (list.copy() or list[:]) creates a new list object but inserts references to the objects found in the original. A deep copy (copy.deepcopy()) recursively creates completely independent copies of all objects found in the original list.
'''

'''
4. How do remove(), pop(), and del differ?
-> remove(value) deletes the first matching value it finds.
-> pop(index) removes and returns the item at the specified index (defaults to the last item).
-> del list[index] deletes the item at a specific index but doesn't return it. It can also delete slices (del list[1:3]).
'''

'''
List Comprehensions: "Write a one-liner to square all even numbers in a list."
(Interviewers want to see: [x2 for x in my_list if x % 2 == 0])

Reversing: "How do you reverse a list without a loop?"
(Using slicing: my_list[::-1] or the in-place method my_list.reverse())

Deduplication: "Remove duplicates from a list while maintaining order."
(Using a dictionary: list(dict.fromkeys(my_list)))

Flattening: "How do you flatten a 2D list into a 1D list?"
'''