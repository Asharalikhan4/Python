'''
-> A dictionary is a mutable collection of key-value pairs. As we touched on earlier, it is Python’s native implementation of a hash map.
-> Some key characteristic:
    1. It has key-value structure.
    2. Mutable.
    3. All key's are unique and Immutable.
    4. Flexible Values
    5. Ordered
-> Under the Hood: The Hash Table:
    Just like sets, dictionaries are built on top of hash tables. When you assign a value to a key (e.g., user["age"] = 28), Python passes the string "age" through a math function to generate a hash. That hash tells Python exactly which slot in memory to put the number 28.This gives dictionaries their superpower: $O(1)$ constant time complexity. Whether your dictionary has 10 items or 10 million items, looking up a value by its key takes the exact same amount of time.
-> Method,What it does,Example
keys(),Returns a view of all keys.,"user.keys() → [""name"", ""age""]"
values(),Returns a view of all values.,"user.values() → [""Alice"", 28]"
items(),"Returns tuples of (key, value). Best for loops.","for k, v in user.items():"
update(dict),"Merges another dictionary into this one, overwriting duplicates.","user.update({""role"": ""Admin""})"
pop(key),Removes the key and returns its value.,"role = user.pop(""role"")"
-> If you try to look up a key that doesn't exist using standard bracket notation, your entire program will crash with a KeyError. To build safe, crash-proof code, use the .get() method.
-> Read about collection.defaultdict, collections.counter, most_common
'''

my_dict = {
    "name": "Ashar Ali Khan",
    "laptop": "Macbook",
    "bike": False
}