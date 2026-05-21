import operator
'''
1. What is difference between List and Tuple?

'''
from 01_basics.List import a


'''
2. Why would you use tuple instead of a list?
-> There are three main reasons:
    - When data should logically not change (e.g., days of the week, coordinate points).
    - When returning multiple values from a function.
    - When you need a composite key for a dictionary (lists cannot be used as dictionary keys because they are unhashable).
'''


'''
3. Is a tuple truly immutable? Can you ever change its contents?
-> Immutability illusion
'''

'''
4. How do you create a tuple with only one element?
-> (1, )
'''


'''
5. if tuples are immutable, why does t = t + (4, 5) work without throwing an error?
-> It works because you aren't modifying the original tuple. The + operator evaluates the two tuples and creates a brand new tuple in memory, which is then reassigned to the variable t. The original tuple is garbage collected.
'''


'''
6. How do you swap two variables in Python without using a temporary third variable?
-> a, b = b, a
it relies on tuple packing and unpacking. Python evaluates the right side first, packing b and a into a hidden tuple, and then unpacks that tuple into the variables on the left
'''


'''
7. How do you unpack the first and last elements of a tuple, but ignore everything in the middle?
-> Using asterisk(*) operator
first, *middle, last = (1, 2, 3, 4, 5). The middle variable becomes a list [2, 3, 4], and first and last get the exact ends.
'''


'''
8. Can all tuples be used as dictionary keys?
-> No. A tuple can only be used as a dictionary key if it is perfectly hashable. If the tuple contains a mutable, unhashable object (like a list or a dictionary), attempting to use it as a key will throw a TypeError
example: {(1, 2): "A"} works perfectly. {(1, [2, 3]): "B"} will crash.
'''