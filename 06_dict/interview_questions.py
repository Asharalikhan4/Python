'''
1. Are Python dictionaries ordered?
-> Yes, as of Python 3.7, the standard dictionary is guaranteed to preserve insertion order. If you insert 'A' then 'B', they will always iterate in that exact order.
'''


'''
2. What happens under the hood when two keys generate the exact same hash?
-> This is called a hash collision. Python handles this using a technique called open addressing (specifically, random probing). If the memory slot for a hash is already taken by a different key, Python uses a secondary formula to jump to a new, empty slot in the memory block and stores it there.
'''


'''
3. Why is dictionary lookup $O(1)$ on average, but $O(n)$ in the worst case?
-> Lookups are O(1) because the hash function points directly to the memory address. However, if there are massive amounts of hash collisions (usually caused by a terrible custom hash function), Python has to search through all the collided items one by one, degrading the performance to a linear O(n) search.
'''


'''
4. How do you merge two dictionaries?
-> dict1 | dict2 (new approach)
(old approach, unpacking) {dict1, dict2}
'''


'''
5. How do you invert a dictionary (make the keys the values, and the values the keys)?
-> Using the dictionary comprehension
{v: k for k, v in my_dict.items()}
'''


'''
6. Two Sum Problem
'''