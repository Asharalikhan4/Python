'''
1. Create a list of the squared values of numbers from 0 to 4.
'''
# Using Loop
loop_squares = []
for val in range(5):
    loop_squares.append(val ** 2)

print("Loop Squares", loop_squares)

# Using Comprehensions
comprehensions_squares = [val ** 2 for val in range(5)]
print("Comprehensions Squares", comprehensions_squares)


'''
2. Create a dict where the key is the name, and the value is the name's length
'''
names = ["Alice", "Bob", "Charlie"]
name_length = {name: len(name) for name in names}
print("Name length", name_length)


'''
3. Square the list of numbers and make sure there's no duplicate
'''
numbers = [1, 1, 2, 3, 3, 4]
unique_squares = {x**2 for x in numbers}
print("Unique Squares", unique_squares)


'''
4. Write a list comprehension to flatten a 2D list (a list of lists).
'''
matrix = [[1, 2], [3, 4], [5, 6]]
flatted_matrix = [item for sublist in matrix for item in sublist]
print("Flatten List", flatted_matrix)


'''
5. What is the difference between [x2 for x in range(1000000)] and (x2 for x in range(1000000))
-> The Trap: The first one uses square brackets [] and is a list comprehension. It generates all one million items in memory at once, which could crash your program.
The Answer: The second one uses parentheses () and is a generator expression. It doesn't create a list; it creates an object that generates the numbers one at a time only when asked for them. It uses almost zero memory, making it far superior for massive datasets.
'''