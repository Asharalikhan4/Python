"""
- Python Dictionaries store data in a key-value pair. Each key is unique and used to retrieve it's associated value.
"""

data = {"name": "Ashar", "age": 22}
print("dict", data)


'''
Using dict() constructor
'''
a = dict(x = "Ashar", y = "Ali", z = "Khan")
print("creating dict using dict() contructor", a)


print("\n-----------------------------------Accessing dict-----------------------------------\n")
b = {"x": "Ashar", "y":"Ali", "z":"Khan"}
print("Accessing dict b using Square bracket and key", b["x"])
print("Accessing dict b using get method and key", b.get("y"))


print("\n-----------------------------------Adding and Updating Dictionary Items-----------------------------------\n")
b["w"] = "Hamza"
print("Accessing dict b after adding a new key value pair", b)