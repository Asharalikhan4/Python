'''
-> Loops are used to execute a block of code repeatedly.
-> There are two type of loops in python.
1. For Loop
2. While Loop
-> Loop control statements.
1. break: Immediately exits the loop
2. continue: Skips to the next iteration
3. pass: Does nothing (placeholder)
4. else: Runs only if the loop finishes normally (not via break)
-> For simple transformations or filtering, Python encourages comprehensions and generators.
-> In python we don't have increment and decrement operator, so we use -=, +=
'''


'''
For Loop
-> Definite Iteration
'''
fruits = ["mango", "apple", "orange", "pineapple"]
rating = [1, 3, 2, 4]

for fruit in fruits:
    print(fruit)

# Using enumerate() to get index + value
for idx, fruit in enumerate(fruits):
    print(f'Index: {idx}, Fruit: {fruit}')

# Using zip() to iterate multiple iterables together
for rating, fruit in zip(rating, fruits):
    print(f'Rating: {rating}, Fruit: {fruit}')


'''
While Loop
-> Indefinite Iteration
'''
count = 10
while count >= 0:
    print(count)
    count -= 1


'''
Loop with else
'''
number = 1
while number <= 10:
    print(number)
    number += 1
else:
    print("Number Printing Finished.")